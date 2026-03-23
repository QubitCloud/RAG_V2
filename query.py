"""
query.py
--------
Retrieval + LLM call. Provider (Claude or Gemini) is chosen from config.py.
Don't edit this file — change config.py instead.
"""

import json
import os
import re
import pickle
from pathlib import Path
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

from sentence_transformers import SentenceTransformer
import faiss

from config import (INDEX_DIR, TOP_K, LLM_PROVIDER, LLM_MODEL,
                    SYSTEM_PROMPT, APP_NAME, EMBED_MODEL)


def strip_markdown(text: str) -> str:
    """Remove markdown formatting so output reads as clean plain text."""
    text = re.sub(r'\*{1,3}(.+?)\*{1,3}', r'\1', text)
    text = re.sub(r'_{1,3}(.+?)_{1,3}', r'\1', text)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[\*\-]\s+', '  - ', text, flags=re.MULTILINE)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'^[-\*]{3,}\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def _get_llm_client():
    if LLM_PROVIDER == "claude":
        import anthropic
        return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    elif LLM_PROVIDER == "gemini":
        from google import genai
        return genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: '{LLM_PROVIDER}'. Use 'claude' or 'gemini'.")


def _call_llm(client, system: str, user: str) -> str:
    if LLM_PROVIDER == "claude":
        resp = client.messages.create(
            model=LLM_MODEL,
            max_tokens=6144,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return strip_markdown(resp.content[0].text)

    elif LLM_PROVIDER == "gemini":
        from google.genai import types
        resp = client.models.generate_content(
            model=LLM_MODEL,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system,
                max_output_tokens=6144,
                temperature=0.2,
            ),
        )
        return strip_markdown(resp.text)


class RAGEngine:

    def __init__(self):
        index_path = Path(INDEX_DIR)

        self.embed_model = SentenceTransformer(EMBED_MODEL)
        self.index       = faiss.read_index(str(index_path / "docs.index"))

        with open(index_path / "chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

        self.client = _get_llm_client()
        self.system = SYSTEM_PROMPT.format(app_name=APP_NAME)

        print(f"[✓] RAG engine ready  |  {len(self.chunks)} chunks  "
              f"|  {LLM_PROVIDER}/{LLM_MODEL}")

    def retrieve(self, question: str) -> list[dict]:
        vec = self.embed_model.encode(
            [question], convert_to_numpy=True
        ).astype("float32")
        distances, indices = self.index.search(vec, TOP_K)
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            chunk = self.chunks[idx].copy()
            chunk["score"] = float(dist)
            results.append(chunk)
        return results

    def build_context(self, chunks: list[dict]) -> str:
        parts = []
        for i, c in enumerate(chunks, start=1):
            parts.append(
                f"[{i}] Source: {c['source']}  |  Page: {c['page']}\n{c['text']}"
            )
        return "\n\n---\n\n".join(parts)

    def ask(self, question: str, verbose: bool = False) -> str:
        chunks  = self.retrieve(question)
        context = self.build_context(chunks)

        if verbose:
            for c in chunks:
                print(f"  • {c['source']} p.{c['page']}  score={c['score']:.2f}")

        user_msg = (
            f"DOCUMENT CONTEXT:\n\n{context}\n\n"
            f"---\n\nQUESTION: {question}"
        )
        return _call_llm(self.client, self.system, user_msg)

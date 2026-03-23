"""
ingest.py
---------
Parse PDFs → chunk → embed → save FAISS index.
Settings come from config.py — don't edit this file.

Usage:
    python ingest.py
"""

import pickle
from pathlib import Path

import pdfplumber
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import faiss
import json

from config import (DOCS_DIR, INDEX_DIR, EMBED_MODEL,
                    CHUNK_SIZE, CHUNK_OVERLAP)


def extract_pages(pdf_path: str) -> list[dict]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = (page.extract_text() or "").strip()
            if text:
                pages.append({"page": i, "text": text})
    return pages


def chunk_text(text: str) -> list[str]:
    words = text.split()
    step  = CHUNK_SIZE - CHUNK_OVERLAP
    chunks = []
    for start in range(0, len(words), step):
        chunk = " ".join(words[start : start + CHUNK_SIZE])
        if chunk:
            chunks.append(chunk)
        if start + CHUNK_SIZE >= len(words):
            break
    return chunks


def build_index():
    docs_path  = Path(DOCS_DIR)
    index_path = Path(INDEX_DIR)
    index_path.mkdir(parents=True, exist_ok=True)

    pdfs = list(docs_path.glob("**/*.pdf"))
    if not pdfs:
        print(f"[!] No PDFs found in '{DOCS_DIR}'. Add documents and re-run.")
        return

    print(f"[+] {len(pdfs)} PDF(s) found.")

    all_chunks = []
    for pdf in tqdm(pdfs, desc="Parsing"):
        for p in extract_pages(str(pdf)):
            for chunk in chunk_text(p["text"]):
                all_chunks.append({"source": pdf.name, "page": p["page"], "text": chunk})

    print(f"[+] {len(all_chunks)} chunks created.")
    print(f"[+] Loading embedding model: {EMBED_MODEL}")

    model      = SentenceTransformer(EMBED_MODEL)
    embeddings = model.encode(
        [c["text"] for c in all_chunks],
        show_progress_bar=True, convert_to_numpy=True
    ).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, str(index_path / "docs.index"))
    with open(index_path / "chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)
    with open(index_path / "config.json", "w") as f:
        json.dump({"model": EMBED_MODEL, "dim": embeddings.shape[1],
                   "total_chunks": len(all_chunks)}, f, indent=2)

    print(f"\n[✓] Index saved to '{INDEX_DIR}/'  ({len(all_chunks)} chunks)")


if __name__ == "__main__":
    build_index()

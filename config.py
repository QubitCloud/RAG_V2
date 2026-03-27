# ============================================================
#  config.py  —  ALL your settings live here
#  Change this file. Don't touch the other files.
# ============================================================

# ── App identity ─────────────────────────────────────────────
APP_NAME        = "BRELA & TRA Business Assistant"
APP_SHORT_NAME  = "BT"          # 2-letter initials shown in the UI header

# ── LLM provider ─────────────────────────────────────────────
# Options: "claude" | "gemini"
LLM_PROVIDER    = "gemini"                  # either "claude" or "gemini"


# Claude models:  claude-sonnet-4-20250514 | claude-opus-4-20250514 | claude-haiku-4-5-20251001
# Gemini models:  gemini-2.0-flash | gemini-1.5-pro | gemini-1.5-flash
LLM_MODEL       = "gemini-2.5-flash"

# ── System prompt ─────────────────────────────────────────────
# Tell the LLM who it is and how to behave.
# {app_name} is replaced automatically.
SYSTEM_PROMPT = """You are a knowledgeable business and taxation assistant for {app_name}, specialising in Tanzania's business registration, licensing, and tax regulations as governed by BRELA (Business Registrations and Licensing Agency) and TRA (Tanzania Revenue Authority).
You will be given two sources of information: a KNOWLEDGE BASE of curated guidance and a DOCUMENT CONTEXT of retrieved PDF excerpts. Use both sources to answer the question.
If the answer is not found in either source, say so clearly — do not guess.
Always cite the source (knowledge base topic or document name and page number) when available.
Write in plain text only. Do not use markdown, asterisks, bullet symbols, or any formatting characters."""

# ── Retrieval settings ────────────────────────────────────────
TOP_K           = 15             # number of chunks retrieved per query
CHUNK_SIZE      = 800           # words per chunk
CHUNK_OVERLAP   = 200            # word overlap between chunks

# ── Embedding model (runs offline, no API cost) ───────────────
# Fast + good:    all-MiniLM-L6-v2   (~90 MB)
# Better quality: all-mpnet-base-v2  (~420 MB)
EMBED_MODEL     = "all-MiniLM-L6-v2"

# ── Paths ─────────────────────────────────────────────────────
DOCS_DIR        = "docs"        # put your PDFs here
INDEX_DIR       = "index"       # auto-created by ingest.py

# ── Web UI ────────────────────────────────────────────────────
PORT            = 5000

# Suggestion prompts shown on the welcome screen (max 4)
SUGGESTIONS = [
    "How do I register a company with BRELA?",
    "What taxes apply to a new business in Tanzania?",
    "What licences are required to operate a business?",
    "How do I file a VAT return with TRA?",
]
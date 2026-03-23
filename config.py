# ============================================================
#  config.py  —  ALL your settings live here
#  Change this file. Don't touch the other files.
# ============================================================

# ── App identity ─────────────────────────────────────────────
APP_NAME        = "My Document Assistant"
APP_SHORT_NAME  = "DA"          # 2-letter initials shown in the UI header

# ── LLM provider ─────────────────────────────────────────────
# Options: "claude" | "gemini"
LLM_PROVIDER    = "gemini"

# Claude models:  claude-sonnet-4-20250514 | claude-opus-4-20250514 | claude-haiku-4-5-20251001
# Gemini models:  gemini-2.0-flash | gemini-1.5-pro | gemini-1.5-flash
LLM_MODEL       = "gemini-2.5-flash"

# ── System prompt ─────────────────────────────────────────────
# Tell the LLM who it is and how to behave.
# {app_name} is replaced automatically.
SYSTEM_PROMPT = """You are a helpful document assistant for {app_name}.
Answer questions strictly based on the provided document context.
If the answer is not in the context, say so clearly — do not guess.
Always cite the source document and page number when available."""

# ── Retrieval settings ────────────────────────────────────────
TOP_K           = 25             # number of chunks retrieved per query
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
    "Summarise the key points in these documents.",
    "What are the main rules or requirements?",
    "What procedures apply to [topic]?",
    "Are there any deadlines or time limits mentioned?",
]

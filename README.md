# Scribe — Production-Style RAG Knowledge Assistant

Scribe is a Retrieval-Augmented Generation (RAG) system that lets users upload PDF documents and ask questions about them. It retrieves relevant context from the documents and uses an LLM to generate grounded, citation-backed answers.

This project is being built incrementally over 14 days as a hands-on AI engineering learning project — every component is implemented, understood, and explained before moving to the next.

> **Status:** 🚧 In Progress — Day 1 of 14 complete.

---

## Tech Stack

| Layer         | Tech                          |
|---------------|--------------------------------|
| Backend       | Python, FastAPI, Pydantic     |
| Database      | PostgreSQL + pgvector         |
| Document parsing | PyMuPDF                    |
| Frontend      | React, Tailwind CSS           |
| Infra         | Docker, Docker Compose        |

---

## Architecture

```text
                 USER
                  │
                  ▼
              React UI
                  │
                  ▼
               FastAPI
                  │
        ┌─────────┴─────────┐
        │                   │
    Documents             Chat
        │                   │
        ▼                   ▼
   PDF Parser           Retriever
        │                   │
     Chunking               │
        │                   │
   Embeddings               │
        │                   │
        └───────► pgvector ◄┘
                     │
                     ▼
              Relevant Chunks
                     │
                     ▼
                   LLM
                     │
                     ▼
             Grounded Answer
                     │
                     ▼
                 Citations
```

---

## Project Structure

```text
scribe-rag/
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── api/
│   │   └── routes.py      # API routes (health, documents, chat)
│   ├── services/
│   │   ├── document_service.py
│   │   └── chat_service.py
│   └── schemas/
│       └── models.py      # Pydantic request/response models
├── docs/
│   └── learning/          # Personal learning notes per topic
├── SCRIBE.md               # Full project spec + teaching protocol
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# Clone
git clone https://github.com/<your-username>/scribe-rag.git
cd scribe-rag

# Virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for interactive API docs (Swagger UI).

---

## Progress

- [x] **Day 1** — FastAPI backend foundations (`/health`, `/documents`, `/chat` stubs, layered architecture)
- [ ] Day 2 — Document ingestion (PyMuPDF, text extraction)
- [ ] Day 3–4 — Database + PostgreSQL setup
- [ ] Day 5 — Chunking pipeline
- [ ] Day 6 — Embedding generation
- [ ] Day 7 — pgvector semantic retrieval
- [ ] Day 8 — RAG pipeline (retrieval → LLM)
- [ ] Day 9 — Citations & grounding
- [ ] Day 10 — Conversation history
- [ ] Day 11 — React frontend
- [ ] Day 12 — Retrieval evaluation
- [ ] Day 13 — Dockerization
- [ ] Day 14 — Docs, architecture diagram, final polish

Full spec: [`SCRIBE.md`](./SCRIBE.md)

---

## Learning Goals

This project is intentionally built with a **learn-while-building** approach — no component is added without first understanding the concept behind it. See `docs/learning/` for topic notes as the project progresses.

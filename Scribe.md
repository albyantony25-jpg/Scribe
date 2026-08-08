# SCRIBE
## Production-Style RAG Knowledge Assistant
### Master Project Specification + Learning Journey
### Version 0.1 — AI Engineering Portfolio MVP

---

# 1. PROJECT IDENTITY

**Project Name:** Scribe

**Repository Name:** `scribe-rag`

**Project Type:** AI Engineering + Backend Engineering

**Version:** v0.1 MVP

**Target Development Time:** 10–14 days

**Primary Development Environment:** Antigravity

**AI Development Assistant:** Claude

---

# 2. PROJECT VISION

Scribe is a production-style Retrieval-Augmented Generation (RAG) knowledge assistant.

Users can upload PDF documents and ask questions about them. Scribe retrieves relevant information from the documents and uses an LLM to generate grounded answers with source citations.

The project is intentionally small enough to complete quickly, but technically deep enough to teach the fundamentals of modern AI engineering.

The ultimate purpose is:

> Build a real AI engineering system while learning the architecture and technologies behind it.

This is NOT intended to be a fake "enterprise platform" filled with unnecessary features.

The initial goal is to build a strong, understandable RAG foundation that can later evolve into an enterprise-grade system.

---

# 3. PRIMARY OBJECTIVES

By completing Scribe, the developer should understand:

### Backend

- Python backend architecture
- REST APIs
- FastAPI
- Pydantic
- asynchronous programming
- API design
- service-layer architecture
- error handling
- database interaction

### AI / ML Engineering

- embeddings
- vector representations
- semantic similarity
- vector search
- chunking
- retrieval
- RAG
- prompt construction
- context windows
- hallucination
- grounding
- citations
- RAG evaluation

### Data

- PostgreSQL
- database schemas
- pgvector
- relational data
- vector data
- metadata

### Frontend

- React
- API integration
- asynchronous requests
- chat UI
- application state

### Engineering

- Git
- GitHub
- testing
- Docker
- environment variables
- project structure
- documentation

---

# 4. MOST IMPORTANT RULE — LEARN WHILE BUILDING

This project is being developed using AI-assisted coding.

Claude must NEVER turn the process into:

```text
User asks
    ↓
Claude generates 5000 lines
    ↓
User copies code
    ↓
Project works
```

Instead use:

```text
CONCEPT
   ↓
UNDERSTAND
   ↓
DESIGN
   ↓
AI-ASSISTED IMPLEMENTATION
   ↓
INSPECT CODE
   ↓
TEST
   ↓
MODIFY
   ↓
EXPLAIN
   ↓
COMMIT
```

The developer should understand every major component that gets added.

---

# 5. CLAUDE'S ROLE

Claude should behave as:

1. Senior AI Engineer
2. Backend Engineer
3. Technical Mentor
4. Pair Programmer
5. Architecture Reviewer
6. Debugging Assistant
7. Interview Preparation Mentor

Claude should NOT behave as an autonomous code generator.

---

# 6. TEACHING PROTOCOL

Before implementing any major component, Claude should provide a short:

## "What We're Learning"

section.

Example:

```text
WHAT WE'RE LEARNING

Today:
- What an API is
- What FastAPI does
- What a route is
- What HTTP methods mean
- Why we are using FastAPI

Architecture:

Client
   ↓
FastAPI
   ↓
Route
   ↓
Service
   ↓
Database
```

Then implement.

After implementation:

## "Understand What We Built"

Claude should explain:

- important files
- important functions
- data flow
- why the architecture is structured this way
- important code decisions

Then:

## "You Should Be Able To Explain"

Give the developer 3–5 questions.

Example:

```text
1. What problem does FastAPI solve?
2. What happens when POST /documents is called?
3. Why shouldn't database logic live inside the route?
4. What does Pydantic validate?
```

The developer should be able to answer these before moving forward.

---

# 7. DO NOT OVER-TEACH

The project should NOT become a theoretical course.

Use:

> Learn enough → build → inspect → test → continue.

Do not spend days learning concepts that won't immediately be used.

---

# 8. MVP SUCCESS CRITERIA

Scribe v0.1 is successful when a user can:

1. Open the web application
2. Upload a PDF
3. Process the document
4. Extract its text
5. Split the text into chunks
6. Generate embeddings
7. Store embeddings in PostgreSQL/pgvector
8. Ask a question
9. Retrieve relevant chunks
10. Send retrieved context to an LLM
11. Receive a grounded answer
12. See citations
13. Ask follow-up questions
14. Run a basic retrieval evaluation
15. Run the application with Docker

---

# 9. NON-GOALS FOR V0.1

Do NOT build:

- multi-tenancy
- complex RBAC
- enterprise SSO
- microservices
- Kubernetes
- Kafka
- Redis
- Celery
- billing
- advanced admin systems
- multi-agent architecture
- fine-tuning
- custom model training
- complex observability infrastructure
- mobile applications
- advanced analytics
- multiple vector databases

These may become future versions.

The objective is:

> **Small system. Deep understanding.**

---

# 10. HIGH-LEVEL ARCHITECTURE

```text
                         SCRIBE
                           │
                           ▼
                 ┌───────────────────┐
                 │     React UI      │
                 │ Documents + Chat  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │      FastAPI      │
                 │      REST API     │
                 └─────────┬─────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
       Document        RAG Engine     Chat
        Service            │          Service
             │             │
             ▼             ▼
       PDF Processing   Retriever
             │             │
             ▼             ▼
         Chunking      pgvector
             │             │
             ▼             │
       Embeddings           │
             │              │
             └──────┬───────┘
                    ▼
             Retrieved Context
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

# 11. TECHNOLOGY STACK

## Backend

Python

FastAPI

Pydantic

---

## Database

PostgreSQL

pgvector

---

## Document Processing

PyMuPDF

---

## Embeddings

One reliable embedding model/API.

The embedding provider must be isolated behind a service abstraction.

---

## LLM

One LLM API/provider.

Do not build multi-provider support yet.

---

## Frontend

React

Tailwind CSS

---

## Infrastructure

Docker

Docker Compose

Git

GitHub

---

# 12. PROJECT ARCHITECTURE PRINCIPLE

Use a simple layered architecture:

```text
API Layer
    ↓
Service Layer
    ↓
Data / Infrastructure Layer
```

And for RAG:

```text
Ingestion
    ↓
Embedding
    ↓
Storage
    ↓
Retrieval
    ↓
Context Construction
    ↓
Generation
    ↓
Citation
```

Avoid unnecessary abstractions.

---

# 13. CORE FEATURE 1 — DOCUMENT UPLOAD

Endpoint:

```text
POST /api/v1/documents
```

The system should:

```text
PDF
 ↓
Validate
 ↓
Extract text
 ↓
Chunk
 ↓
Generate embeddings
 ↓
Store
```

Return useful metadata.

Example:

```json
{
  "id": "document-id",
  "filename": "employee-handbook.pdf",
  "status": "processed"
}
```

---

# 14. LEARNING JOURNEY — PHASE 1

## FastAPI + Backend Foundations

### Goal

Understand how a backend application actually works.

### Learn

- HTTP
- REST
- GET/POST/DELETE
- request/response
- JSON
- API routes
- FastAPI
- Pydantic
- dependency injection
- async basics
- project structure

### Build

```text
GET /health
POST /documents
POST /chat
```

### Understanding checkpoint

The developer must understand:

```text
Browser
   ↓
HTTP Request
   ↓
FastAPI Route
   ↓
Python Function
   ↓
Response
   ↓
Browser
```

### Questions Claude should ask

- What is an API?
- What is REST?
- What happens when a client calls an endpoint?
- Why does FastAPI use Pydantic?
- What does async mean?

---

# 15. CORE FEATURE 2 — DOCUMENT INGESTION

Build:

```text
PDF
 ↓
PyMuPDF
 ↓
Raw Text
 ↓
Clean Text
 ↓
Chunks
```

---

# 16. LEARNING JOURNEY — PHASE 2

## Document Processing + Chunking

### Learn

- how PDFs store text
- text extraction
- why raw documents aren't directly suitable for retrieval
- chunking
- chunk size
- overlap
- metadata

### Important concept

The developer should understand why:

```text
Entire PDF → LLM
```

is usually a poor architecture.

Instead:

```text
PDF
 ↓
Chunks
 ↓
Relevant chunks
 ↓
LLM
```

### Understanding checkpoint

The developer must be able to answer:

> Why do we chunk documents?

> What happens if chunks are too large?

> What happens if chunks are too small?

> Why keep page numbers?

---

# 17. CORE FEATURE 3 — EMBEDDINGS

For each chunk:

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

Store the vector alongside the chunk.

---

# 18. LEARNING JOURNEY — PHASE 3

## Embeddings

This is one of the most important learning sections.

Claude must explain embeddings from first principles.

Teach:

- numerical representation
- semantic meaning
- vector dimensions
- similarity
- cosine similarity
- why semantically similar sentences can have similar vectors

Example:

```text
"How many vacation days do employees receive?"

and

"What is the annual leave allowance?"
```

The developer should understand why an embedding-based system can recognize these as semantically related even though the words differ.

### Understanding checkpoint

The developer should be able to explain:

> "What exactly is an embedding?"

without saying merely:

> "It's a vector."

---

# 19. CORE FEATURE 4 — PGVECTOR

Use PostgreSQL + pgvector.

Suggested conceptual schema:

### documents

```text
id
filename
status
created_at
updated_at
```

### document_chunks

```text
id
document_id
content
page_number
chunk_index
embedding
created_at
```

### conversations

```text
id
created_at
```

### messages

```text
id
conversation_id
role
content
created_at
```

---

# 20. LEARNING JOURNEY — PHASE 4

## PostgreSQL + Vector Search

Learn:

### PostgreSQL

- tables
- primary keys
- foreign keys
- relationships
- CRUD
- indexing

### pgvector

- vector columns
- vector similarity
- nearest-neighbor search
- top-k retrieval

Understand the difference between:

```text
Traditional database search
```

and:

```text
Semantic vector search
```

### Understanding checkpoint

The developer should be able to explain:

> Why are we using PostgreSQL?

> What does pgvector add?

> What does top-k mean?

> What happens when we search for a question?

---

# 21. CORE FEATURE 5 — RETRIEVAL

Given:

```text
"What is the company's annual leave policy?"
```

Perform:

```text
Question
 ↓
Question Embedding
 ↓
Vector Search
 ↓
Top-K Chunks
```

Retrieval should be configurable.

Example:

```text
top_k = 5
```

---

# 22. LEARNING JOURNEY — PHASE 5

## Information Retrieval

Teach:

- query embeddings
- similarity search
- top-k
- relevance
- retrieval quality
- false positives
- false negatives

Important understanding:

RAG quality depends heavily on retrieval quality.

If the retriever retrieves bad information:

```text
Bad retrieval
     ↓
Bad context
     ↓
Bad answer
```

---

# 23. CORE FEATURE 6 — RAG

Complete pipeline:

```text
User Question
      ↓
Conversation Context
      ↓
Query Embedding
      ↓
Vector Retrieval
      ↓
Relevant Chunks
      ↓
Context Construction
      ↓
Prompt
      ↓
LLM
      ↓
Answer
```

---

# 24. LEARNING JOURNEY — PHASE 6

## RAG Fundamentals

Claude must explicitly teach:

### Retrieval

Find relevant information.

### Augmentation

Add that information to the LLM context.

### Generation

Allow the LLM to generate the answer.

The developer must understand:

```text
RAG ≠ model training
```

and:

```text
RAG ≠ simply asking ChatGPT a question
```

Teach:

- grounding
- hallucination
- context windows
- prompt construction
- retrieved context
- answer generation

---

# 25. RAG PROMPTING

The LLM should receive structured context.

Conceptually:

```text
SYSTEM:
You answer using the provided context.

CONTEXT:
[Retrieved chunk 1]

[Retrieved chunk 2]

[Retrieved chunk 3]

QUESTION:
What is the leave policy?
```

The model should be instructed:

- use provided context
- do not fabricate unsupported facts
- admit when information isn't available
- answer clearly
- cite sources

---

# 26. CORE FEATURE 7 — CITATIONS

Every answer should expose supporting sources.

Example:

```text
Scribe:

Employees receive 20 days of annual leave per year.

Sources:
[1] Employee Handbook — Page 14
```

Backend response:

```json
{
  "answer": "Employees receive 20 days...",
  "sources": [
    {
      "document": "employee-handbook.pdf",
      "page": 14,
      "chunk_id": "abc123"
    }
  ]
}
```

---

# 27. LEARNING JOURNEY — PHASE 7

## Grounding + Citations

Learn:

- why citations matter
- source attribution
- grounded generation
- hallucination mitigation
- evidence-based responses

The developer should understand that:

> A citation system does not automatically guarantee that an answer is correct.

It only tells us which retrieved evidence was supplied.

This distinction is important for understanding RAG evaluation.

---

# 28. CORE FEATURE 8 — CONVERSATION HISTORY

Support:

```text
User:
What is the annual leave policy?

Scribe:
Employees receive 20 days...

User:
Does that include sick leave?

Scribe:
No...
```

Store conversation messages.

Do not build sophisticated long-term memory.

---

# 29. LEARNING JOURNEY — PHASE 8

## Context Management

Teach:

- conversation state
- chat history
- context windows
- why sending unlimited history is problematic
- how conversation context affects retrieval

The developer should understand:

```text
Conversation History
        +
Current Question
        ↓
Context-aware query
```

---

# 30. FRONTEND

Build a simple React interface.

## Documents

```text
Scribe

Documents

[ Upload PDF ]

Employee Handbook.pdf
Processed

Security Policy.pdf
Processed
```

## Chat

```text
Scribe

────────────────────────────

You:
What is the leave policy?

Scribe:
Employees receive 20 days...

Sources:
Employee Handbook — p.14

────────────────────────────

[ Ask Scribe... ]
```

Focus on usability.

Do not spend excessive time on animations or visual effects.

---

# 31. LEARNING JOURNEY — PHASE 9

## React + Backend Integration

Learn:

- components
- state
- API calls
- asynchronous requests
- loading states
- error states
- rendering chat messages
- frontend/backend communication

The goal isn't to become a frontend specialist.

The goal is to understand how an AI backend becomes a usable application.

---

# 32. EVALUATION

Create:

```text
evaluation/
    questions.json
    evaluate.py
```

Use approximately 20–30 questions.

Example:

```json
{
  "question": "How many annual leave days are provided?",
  "expected_document": "employee-handbook.pdf",
  "expected_page": 14
}
```

Measure:

```text
Questions: 30
Correct retrievals: 27
Retrieval accuracy: 90%
```

If practical, add basic answer evaluation.

---

# 33. LEARNING JOURNEY — PHASE 10

## RAG Evaluation

This is critical.

Teach:

- why RAG must be evaluated
- retrieval quality
- answer correctness
- faithfulness
- evaluation datasets
- test questions

The developer should understand:

```text
"It worked when I tried it"
```

is not a meaningful evaluation methodology.

Instead:

```text
Known questions
      ↓
Known expected evidence
      ↓
Run system
      ↓
Measure retrieval
```

---

# 34. TESTING

Implement basic tests for:

- health endpoint
- document validation
- chunking
- retrieval
- chat endpoint
- basic RAG behavior

Do not pursue 100% coverage.

Focus on important behavior.

---

# 35. LEARNING JOURNEY — PHASE 11

## Testing AI Systems

Teach the difference between:

### Unit testing

Testing deterministic components.

Example:

```text
chunk_text()
```

### Integration testing

Testing components together.

Example:

```text
API → Database
```

### AI evaluation

Testing model/system behavior against expected outcomes.

These are different concepts and should not be conflated.

---

# 36. DOCKER

Eventually:

```bash
docker compose up
```

should start the application.

Conceptually:

```text
React
Backend
PostgreSQL + pgvector
```

---

# 37. LEARNING JOURNEY — PHASE 12

## Docker + Deployment Concepts

Teach:

- what containers are
- why containers exist
- images
- containers
- environment variables
- Docker Compose
- reproducibility

The developer should understand why:

```text
"It works on my machine"
```

is a problem Docker helps solve.

---

# 38. SECURITY BASICS

Implement:

- file type validation
- file size limits
- API input validation
- environment variables
- no hardcoded API keys
- safe error messages
- safe document handling

Add:

```text
.env.example
```

---

# 39. PROJECT STRUCTURE

Suggested:

```text
scribe-rag/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── documents.py
│   │   │       ├── chat.py
│   │   │       └── health.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │   ├── document_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── llm_service.py
│   │   │   └── chat_service.py
│   │   │
│   │   ├── ingestion/
│   │   │   ├── parser.py
│   │   │   ├── chunker.py
│   │   │   └── pipeline.py
│   │   │
│   │   └── rag/
│   │       ├── retriever.py
│   │       ├── prompt.py
│   │       └── pipeline.py
│   │
│   └── tests/
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── evaluation/
│   ├── questions.json
│   └── evaluate.py
│
├── docker-compose.yml
├── .env.example
├── README.md
└── docs/
    └── architecture.md
```

This is a guideline, not a rigid requirement.

---

# 40. API DESIGN

Suggested endpoints:

```text
GET    /health

POST   /api/v1/documents
GET    /api/v1/documents
GET    /api/v1/documents/{id}
DELETE /api/v1/documents/{id}

POST   /api/v1/chat

GET    /api/v1/conversations
GET    /api/v1/conversations/{id}
```

Keep the API small.

---

# 41. CONFIGURATION

Use:

```text
DATABASE_URL
LLM_API_KEY
EMBEDDING_API_KEY
```

through environment variables.

Never hardcode secrets.

---

# 42. FAILURE HANDLING

Handle:

- invalid PDF
- empty PDF
- extraction failure
- embedding failure
- database failure
- LLM failure
- missing conversation
- invalid request
- no relevant results

When retrieval produces insufficient evidence:

```text
I couldn't find enough information in the uploaded documents to answer this question.
```

Do not fabricate an answer.

---

# 43. GIT WORKFLOW

Use incremental commits.

Examples:

```text
feat: initialize FastAPI backend

feat: add PostgreSQL integration

feat: implement PDF extraction

feat: implement document chunking

feat: add embedding generation

feat: integrate pgvector

feat: implement semantic retrieval

feat: implement RAG pipeline

feat: add source citations

feat: add conversation history

feat: build document interface

feat: build chat interface

test: add retrieval evaluation

chore: dockerize application

docs: add architecture documentation
```

Every meaningful milestone should be committed.

---

# 44. 14-DAY LEARNING + BUILD PLAN

## DAY 1

### Learn

- HTTP
- REST
- APIs
- FastAPI basics

### Build

FastAPI project + `/health`.

---

## DAY 2

### Learn

- Pydantic
- request validation
- dependency injection
- backend project structure

### Build

Basic document endpoint.

---

## DAY 3

### Learn

- PostgreSQL
- tables
- relationships
- SQL basics

### Build

Database integration.

---

## DAY 4

### Learn

- PDFs
- text extraction
- document processing

### Build

PDF upload + extraction.

---

## DAY 5

### Learn

- chunking
- context
- metadata

### Build

Chunking pipeline.

---

## DAY 6

### Learn

- embeddings
- vectors
- semantic similarity

### Build

Embedding generation.

---

## DAY 7

### Learn

- pgvector
- vector similarity
- top-k retrieval

### Build

Semantic retrieval.

At the end of Day 7:

> You have the foundation of a real RAG system.

---

## DAY 8

### Learn

- RAG architecture
- grounding
- context construction
- prompting

### Build

Question → retrieval → LLM.

---

## DAY 9

### Learn

- hallucination
- citations
- source attribution

### Build

Citation-aware answers.

---

## DAY 10

### Learn

- conversation state
- context windows

### Build

Conversation history.

---

## DAY 11

### Learn

- React basics
- frontend/backend communication

### Build

Document + chat UI.

---

## DAY 12

### Learn

- evaluation
- retrieval metrics
- testing AI systems

### Build

20–30 question evaluation set.

---

## DAY 13

### Learn

- Docker
- containers
- Compose

### Build

Dockerized application.

---

## DAY 14

### Learn

- documentation
- architecture communication
- project presentation

### Build

- README
- architecture diagram
- screenshots
- demo
- cleanup
- final tests

---

# 45. DAILY WORKFLOW

Every development session should roughly follow:

```text
10–20 min
Learn concept

30–60 min
Build with Claude

20–30 min
Read/understand generated code

20 min
Debug/test/modify

10 min
Git commit + notes
```

Do NOT spend the entire session prompting Claude.

The goal is:

> **AI-assisted coding, not AI-dependent coding.**

---

# 46. LEARNING NOTES

Maintain:

```text
docs/learning/
```

with short notes such as:

```text
01-fastapi.md
02-http-rest.md
03-postgresql.md
04-chunking.md
05-embeddings.md
06-vector-search.md
07-rag.md
08-citations.md
09-evaluation.md
10-docker.md
```

Each note should answer:

```text
What is it?
Why do we need it?
How does it work?
How does Scribe use it?
What alternatives exist?
What did I learn?
```

These notes are primarily for the developer's understanding.

---

# 47. CLAUDE'S "TEACH ME" RULE

Whenever the developer says:

> "I don't understand this."

Claude must stop implementation and teach the concept from first principles.

Use:

```text
Simple explanation
        ↓
Real-world analogy
        ↓
Scribe-specific example
        ↓
Small code example
        ↓
Check understanding
        ↓
Continue building
```

Never respond with:

> "Don't worry, it's abstracted away."

The developer needs to understand the abstraction.

---

# 48. CLAUDE'S "WHY" RULE

For every important technology, Claude should explain:

### Why are we using it?

### What problem does it solve?

### What would happen without it?

### What alternatives exist?

### Why is this choice appropriate for Scribe?

Examples:

```text
Why FastAPI?
Why PostgreSQL?
Why pgvector?
Why embeddings?
Why chunking?
Why RAG?
Why Docker?
Why React?
```

---

# 49. INTERVIEW PREPARATION MODE

At the end of each major phase, Claude should provide a short interview checkpoint.

Example:

### Backend

> Explain what happens when `/api/v1/chat` receives a request.

### RAG

> Explain the difference between retrieval and generation.

### Embeddings

> Why can't we just use keyword search?

### Vector database

> What does pgvector actually store?

### Architecture

> Why separate the RAG service from the API route?

### Evaluation

> How do you know your retriever is working?

The developer should answer these without copying from Claude.

---

# 50. DEFINITION OF DONE

Scribe v0.1 is complete when:

- [ ] FastAPI backend works
- [ ] PostgreSQL works
- [ ] PDF upload works
- [ ] PDF extraction works
- [ ] Chunking works
- [ ] Embeddings work
- [ ] pgvector works
- [ ] Semantic retrieval works
- [ ] RAG pipeline works
- [ ] Grounded answers work
- [ ] Citations work
- [ ] Conversation history works
- [ ] React interface works
- [ ] Evaluation dataset exists
- [ ] Retrieval evaluation works
- [ ] Basic tests exist
- [ ] Docker Compose works
- [ ] README exists
- [ ] Architecture diagram exists
- [ ] Git history shows incremental development
- [ ] Developer can explain the complete system

The final criterion is especially important:

> **The project is not considered fully complete if the developer cannot explain how it works.**

---

# 51. PORTFOLIO POSITIONING

Project title:

**Scribe — Production-Style RAG Knowledge Assistant**

Suggested resume description:

> Built a FastAPI-based RAG knowledge assistant that processes PDF documents, generates embeddings, performs semantic retrieval using PostgreSQL/pgvector, and produces citation-grounded LLM responses with conversational context.

Second bullet:

> Developed an automated retrieval evaluation pipeline, implemented document ingestion and chunking, and containerized the application with Docker for reproducible deployment.

Do not claim:

- enterprise-scale deployment
- production traffic
- distributed architecture
- multi-tenancy
- advanced security

unless those features are actually implemented later.

---

# 52. FUTURE ROADMAP

After v0.1, evolve the same project.

## v0.2 — Better Retrieval

Add:

```text
Vector Search
+
Keyword Search
↓
Hybrid Retrieval
```

---

## v0.3 — Reranking

Add a reranker after initial retrieval.

```text
Query
 ↓
Retriever
 ↓
Top 20
 ↓
Reranker
 ↓
Top 5
 ↓
LLM
```

---

## v0.4 — Authentication

Add:

- login
- JWT
- users

---

## v0.5 — RBAC

Add:

```text
Admin
Manager
Employee
```

and document-level access control.

---

## v0.6 — Advanced Evaluation

Add:

- retrieval metrics
- faithfulness
- answer relevance
- latency tracking

---

## v0.7 — Observability

Add:

- structured logs
- request tracing
- retrieval latency
- LLM latency
- token usage

---

## v0.8 — More Documents

Add:

- DOCX
- TXT
- Markdown

---

## v0.9 — Multi-Tenancy

Add organization-level isolation.

---

## v1.0 — Enterprise Scribe

Eventually evolve into:

```text
                    SCRIBE
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   Multi-Tenant    RBAC       Observability
        │             │             │
        └─────────────┼─────────────┘
                      │
                Advanced RAG
                      │
          ┌───────────┼───────────┐
          │           │           │
       Hybrid      Reranking   Evaluation
      Retrieval
```

---

# 53. FINAL DEVELOPMENT PRINCIPLE

Scribe should follow one central philosophy:

> **Build small enough to finish. Learn deeply enough to explain. Design cleanly enough to extend.**

The MVP does not need to be a massive enterprise platform.

A well-built 14-day RAG system that the developer fully understands is more valuable than a 60-day "enterprise platform" that was mostly generated by AI.

At the end of Scribe v0.1, the developer should be able to draw this architecture from memory:

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

And, more importantly, explain **why every arrow exists**.

That is the real learning outcome of Scribe.
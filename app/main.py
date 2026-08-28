from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Scribe RAG Assistant",
    description="API for the Scribe RAG Knowledge Assistant.",
    version="0.1"
)

# Include the API routes
app.include_router(router, prefix="/api/v1")

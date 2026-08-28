from fastapi import APIRouter
from app.schemas.models import HealthResponse, DocumentUploadResponse, ChatRequest, ChatResponse
from app.services import document_service, chat_service

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(status="ok", message="Scribe API is running.")

@router.post("/documents", response_model=DocumentUploadResponse)
def upload_document():
    # In a real scenario, this would accept an UploadFile.
    # For the Day 1 stub, we just simulate processing a dummy file.
    return document_service.process_document("dummy_file.pdf")

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return chat_service.generate_chat_response(request)

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.models import HealthResponse, DocumentUploadResponse, ChatRequest, ChatResponse
from app.services import document_service, chat_service

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(status="ok", message="Scribe API is running.")

@router.post("/documents", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    content = await file.read()
    return document_service.process_document(content, file.filename)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return chat_service.generate_chat_response(request)

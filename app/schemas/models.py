from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str
    message: str

class DocumentUploadResponse(BaseModel):
    id: str
    filename: str
    status: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

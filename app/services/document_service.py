import uuid
from app.schemas.models import DocumentUploadResponse

def process_document(filename: str) -> DocumentUploadResponse:
    """
    Stub for processing an uploaded document.
    Later, this will handle PDF extraction, chunking, and embedding.
    """
    return DocumentUploadResponse(
        id=str(uuid.uuid4()),
        filename=filename,
        status="processed"
    )

import uuid
import pymupdf # type: ignore
from app.schemas.models import DocumentUploadResponse
from app.utils.chunking import chunk_text

def process_document(file_content: bytes, filename: str) -> DocumentUploadResponse:
    """
    Extracts text from a PDF and chunks it.
    """
    doc_id = str(uuid.uuid4())
    chunks = []
    
    # Open the PDF from bytes
    with pymupdf.open(stream=file_content, filetype="pdf") as pdf:
        chunk_index = 0
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text = page.get_text("text")
            
            # Clean text (remove excessive newlines)
            clean_text = " ".join(text.split())
            
            if clean_text:
                page_chunks = chunk_text(clean_text, page_number=page_num + 1, start_index=chunk_index)
                chunks.extend(page_chunks)
                chunk_index += len(page_chunks)
                
    # In a real app, we would save these chunks to pgvector now.
    # For Phase 2, we just count them to verify it worked.
    
    print(f"Processed {len(chunks)} chunks from {filename}")

    return DocumentUploadResponse(
        id=doc_id,
        filename=filename,
        status=f"processed {len(chunks)} chunks"
    )

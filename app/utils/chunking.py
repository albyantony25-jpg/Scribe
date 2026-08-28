from typing import List
from app.schemas.chunk import DocumentChunk

def chunk_text(text: str, page_number: int, start_index: int = 0, chunk_size: int = 500, overlap: int = 50) -> List[DocumentChunk]:
    """
    Splits text into chunks of `chunk_size` characters, with `overlap` characters between chunks.
    """
    chunks = []
    # Basic tokenization by character length. 
    # In a real app, you might use recursive character text splitting or a tokenizer like tiktoken.
    
    # Ensure chunk_size is larger than overlap to prevent infinite loops
    if chunk_size <= overlap:
        chunk_size = overlap + 100
        
    i = 0
    chunk_index = start_index
    while i < len(text):
        chunk_text = text[i:i + chunk_size]
        
        # Avoid creating tiny trailing chunks containing only whitespace
        if chunk_text.strip():
            chunks.append(DocumentChunk(
                text=chunk_text,
                page_number=page_number,
                chunk_index=chunk_index
            ))
            chunk_index += 1
            
        i += chunk_size - overlap

    return chunks

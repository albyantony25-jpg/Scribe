from pydantic import BaseModel
from typing import Optional

class DocumentChunk(BaseModel):
    text: str
    page_number: Optional[int] = None
    chunk_index: int
    metadata: dict = {}

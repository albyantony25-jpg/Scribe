from app.schemas.models import ChatRequest, ChatResponse

def generate_chat_response(request: ChatRequest) -> ChatResponse:
    """
    Stub for the chat generation.
    Later, this will retrieve context and query an LLM.
    """
    return ChatResponse(
        reply=f"Echo: {request.message}. I am a stub for the RAG engine."
    )

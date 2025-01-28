from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from aiagent import get_response_from_ai_agent
import uvicorn

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

ALLOWED_MODEL_NAMES=["deepseek-r1-distill-llama-70b", "llama-3.3-70b-versatile", "gemma2-9b-instruct", "mixtral-8x7b-32768"]

app = FastAPI(title="Boom Boom")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using langgraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name"}
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
##🚀 AI Chatbot with FastAPI & Streamlit
This repository contains an AI chatbot powered by Groq's LLaMA 3.3-70B and other models. It provides an interactive chatbot using FastAPI for the backend and Streamlit for the frontend.

📌 Features
Supports multiple LLMs, including LLaMA 3.3-70B, DeepSeek-R1, Gemma-2, Mixtral-8x7B

Integrates LangGraph for agentic reasoning

Optional Tavily Search for retrieving real-time web results

FastAPI backend with a /chat endpoint

Streamlit frontend for user interaction

📂 File Structure
aiagent.py – AI agent logic using LangGraph and Tavily Search

backend.py – FastAPI-based backend for model inference

frontend.py – Streamlit-based user interface

🛠 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git  
cd your-repo  
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt  
Set up API keys for Groq and Tavily Search:

bash
Copy
Edit
export GROQ_API_KEY="your_api_key"
export TAVILY_API_KEY="your_api_key"
🚀 Usage
Start Backend
bash
Copy
Edit
uvicorn backend:app --host 0.0.0.0 --port 8000  
Start Frontend
bash
Copy
Edit
streamlit run frontend.py  
🔥 API Endpoint
POST /chat – Sends user queries to the chatbot

Request Body:

json
Copy
Edit
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as an AI chatbot who is smart and friendly",
  "messages": ["Hello, how are you?"],
  "allow_search": true
}
Response:

json
Copy
Edit
"I'm doing great! How can I help you today?"
📜 License
This project is open-source under the MIT License.

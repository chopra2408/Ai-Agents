import streamlit as st
import requests

st.set_page_config(page_title="Boom Boom", layout="wide")
st.title("AI chatbot")
st.write("Create and interact with AI agent")

system_prompt = st.text_area("Define your ai agent: ", height=70, placeholder="Type your system here...")

MODEL_NAMES_GROQ = ["deepseek-r1-distill-llama-70b", "llama-3.3-70b-versatile", "gemma2-9b-instruct", "mixtral-8x7b-32768"]

provider = st.radio("Select a provider", ["Groq"])

if provider == "Groq":
    selected_model = st.selectbox("Select GROQ model", MODEL_NAMES_GROQ)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your query", height=150, placeholder="Ask anything...")

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask agent..."):
    if user_query.strip():

        paylaod = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
            }

        response = requests.post(API_URL,json=paylaod)

        if response.status_code == 200:
            response_data = response.json()

            if "error" in response_data:
                st.error(f"Error: {response_data['error']}")
            else:    
                st.subheader("Agent Response")
                st.markdown(f"Final Answer is: {response_data}")
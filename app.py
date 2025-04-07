
import streamlit as st
from my_agent import ask_agent

st.set_page_config(page_title="GenAI Competitive Intelligence Chatbot", layout="centered")

st.title("🤖 GenAI Competitive Intelligence Chatbot")
st.write("Powered by Gemini 1.5 Pro - Ask your questions below!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", key="user_input")
    submit = st.form_submit_button("Send")

if submit and user_input.strip():
    with st.spinner("Thinking..."):
        response = ask_agent(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("GenAI Agent", response))

for speaker, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{speaker}:** {message}")

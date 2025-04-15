import streamlit as st
from my_agent import ask_agent

# Page config
st.set_page_config(page_title="🤖 GenAI Competitive Intelligence Chatbot", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stTextInput > div > div > input {
            border: 2px solid #7F56D9;
            border-radius: 12px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #7F56D9;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: 600;
        }
        .chat-message {
            background-color: #ffffff;
            border-radius: 1rem;
            padding: 1rem;
            margin-bottom: 0.8rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .user {
            background-color: #D6F5D6;
            border-left: 6px solid #34A853;
        }
        .agent {
            background-color: #E0E7FF;
            border-left: 6px solid #6366F1;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🤖 GenAI Competitive Intelligence Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>💡 Powered by Gemini 1.5 Pro — Ask anything related to market, competitors, or strategy!</p>", unsafe_allow_html=True)

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message:", key="user_input")
    submit = st.form_submit_button("🚀 Send")

# Handle submission
if submit and user_input.strip():
    with st.spinner("🤖 Thinking..."):
        response = ask_agent(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("GenAI Agent", response))

# Display chat history
for speaker, message in reversed(st.session_state.chat_history):
    role_class = "user" if speaker == "You" else "agent"
    st.markdown(
        f"<div class='chat-message {role_class}'><strong>{speaker}:</strong><br>{message}</div>",
        unsafe_allow_html=True
    )

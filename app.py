import streamlit as st
from chatbot import match_intent

st.set_page_config(page_title="ChatBot", page_icon="🤖")

st.markdown("<h1 style='text-align: center;'>🤖 ChatBot Assistant</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say something...")

if user_input:
    response = match_intent(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for speaker, message in st.session_state.chat_history:
    st.chat_message("assistant" if speaker == "Bot" else "user").write(message)

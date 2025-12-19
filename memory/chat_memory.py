
import streamlit as st

def _init_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add(role: str, content: str):
    _init_memory()
    st.session_state.chat_history.append(
        {"role": role, "content": content}
    )

def get():
    _init_memory()
    return st.session_state.chat_history

def clear():
    st.session_state.chat_history = []

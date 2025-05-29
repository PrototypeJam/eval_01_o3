import streamlit as st

# ----- 1. Persist API key safely -------------------------------------------
def get_api_key():
    """Return key from session; fall back to st.secrets when deployed."""
    if "api_key" in st.session_state and st.session_state.api_key:
        return st.session_state.api_key
    if "OPENAI_API_KEY" in st.secrets:
        return st.secrets["OPENAI_API_KEY"]
    return None

# ----- 2. Persist model & param selection -----------------------------------
def init_defaults():
    defaults = {
        "model": "gpt-4o",
        "temperature": 0.7,
    }
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)

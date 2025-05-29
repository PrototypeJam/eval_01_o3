import streamlit as st
from utils.state import init_defaults, get_api_key
from scripts import chat_script, script2_placeholder, scriptN_placeholder

st.set_page_config(page_title="LLM Starter", layout="wide")
init_defaults()

# ---------- TAB 0 – API key ------------------------------------------------
tab_api, tab_models, tab_py1, tab_py2, tab_pyn = st.tabs([
    "\U0001F511 API Key", "\u2699\ufe0f Model & Params", "Python Script 1", "Python Script 2", "Python Script N"
])

with tab_api:
    st.subheader("Enter your OpenAI key")
    st.text_input("OPENAI_API_KEY", type="password", key="api_key")
    if get_api_key():
        st.success("Key stored in session (not persisted).")

with tab_models:
    st.subheader("Model & generation parameters")
    st.selectbox(
        "Model",
        ["gpt-4o", "Claude 3.7", "Gemini 2.5 Pro"],
        key="model",
    )
    st.slider("Temperature", 0.0, 1.0, key="temperature")
    st.info("Claude & Gemini placeholders until APIs wired in.")

with tab_py1:
    chat_script.render()

with tab_py2:
    script2_placeholder.render()

with tab_pyn:
    scriptN_placeholder.render()

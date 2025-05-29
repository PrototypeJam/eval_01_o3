import streamlit as st
from openai import OpenAI
from utils.state import get_api_key

def render():
    st.header("Chat with GPT-4o")

    # --- Prompt box ----------------------------------------------------------
    user_msg = st.chat_input("Ask anything…")
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    if user_msg:
        st.session_state.chat_log.append(("user", user_msg))
        with st.spinner("GPT-4o is thinking…"):
            client = OpenAI(api_key=get_api_key())
            response = client.responses.create(
                model=st.session_state.model,
                input=user_msg,
                temperature=st.session_state.temperature,
                instructions="You are a helpful assistant."
            )
            assistant_msg = response.output_text
        st.session_state.chat_log.append(("assistant", assistant_msg))

    # --- Display running log at bottom -------------------------------------
    for role, msg in st.session_state.chat_log:
        if role == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

import streamlit as st
import os

# Set from secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_PROJECT"] = st.secrets["OPENAI_PROJECT"]

# Debug output (remove after test)
st.write("🔐 OpenAI Key Length:", len(os.environ["OPENAI_API_KEY"]))
st.write("🔐 Project ID:", os.environ["OPENAI_PROJECT"])

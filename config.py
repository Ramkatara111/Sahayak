
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# First check environment variables (.env locally)
API_KEY = os.getenv("GEMINI_API_KEY")

# If not found, check Streamlit Cloud Secrets
if not API_KEY:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        API_KEY = None

# Model configuration
CHAT_MODEL = "gemini-2.5-flash"
EMBED_MODEL = "gemini-embedding-001"

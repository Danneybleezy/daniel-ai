import streamlit as st
from utils.chat import chat_tab
from utils.image_tools import enhance_tab, generate_image_tab
from utils.voice import voice_tab
from utils.pdf_summary import pdf_summary_tab
from utils.music import music_tab
from utils.avatar import avatar_tab
from utils.translate import translate_tab
from utils.diagram_explainer import diagram_tab
from settings import APP_NAME, FOOTER

# ------------------------
# CONFIG
# ------------------------
st.set_page_config(page_title=APP_NAME, layout="centered")
st.title(APP_NAME)
st.markdown("Your personal mobile AI assistant powered by **Groq** + 🤖")

# ------------------------
# Load API Keys
# ------------------------
GROQ_API_KEY = st.secrets.get("groq_api_key")

# ------------------------
# Sidebar: Mode Selector
# ------------------------
mode = st.sidebar.radio("📂 Select Feature", [
    "🧠 Chat",
    "🖼️ Enhance Image",
    "🎨 Generate Image",
    "🎤 Voice Assistant",
    "📄 PDF Summarizer",
    "🎵 Music Generator",
    "🌍 Translate Anything",
    "🧑‍🎭 Personality Mode",
    "🧑‍🏫 Diagram Explainer",
    "🧑‍🎨 Create Avatar"
])

# ------------------------
# Feature Dispatcher
# ------------------------
if mode == "🧠 Chat":
    chat_tab(GROQ_API_KEY)

elif mode == "🖼️ Enhance Image":
    enhance_tab()

elif mode == "🎨 Generate Image":
    generate_image_tab()

elif mode == "🎤 Voice Assistant":
    voice_tab(GROQ_API_KEY)

elif mode == "📄 PDF Summarizer":
    pdf_summary_tab(GROQ_API_KEY)

elif mode == "🎵 Music Generator":
    music_tab()

elif mode == "🌍 Translate Anything":
    translate_tab(GROQ_API_KEY)

elif mode == "🧑‍🎭 Personality Mode":
    chat_tab(GROQ_API_KEY, personality_mode=True)

elif mode == "🧑‍🏫 Diagram Explainer":
    diagram_tab(GROQ_API_KEY)

elif mode == "🧑‍🎨 Create Avatar":
    avatar_tab()

# ------------------------
# Footer
# ------------------------
st.markdown("---")
st.caption(FOOTER)

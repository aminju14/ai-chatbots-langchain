import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load API key dari file .env (jika ada)
load_dotenv()

st.set_page_config(
    page_title="AI Chat",
    page_icon="✦",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #08080c;
        --bg-soft: #0e0e16;
        --surface: rgba(255, 255, 255, 0.04);
        --border: rgba(255, 255, 255, 0.08);
        --text: #e7e9ee;
        --muted: #8a8f9c;
        --accent: #7c5cff;
        --accent-2: #2dd4bf;
        --user: rgba(124, 92, 255, 0.14);
        --user-border: rgba(124, 92, 255, 0.28);
        --bot: rgba(45, 212, 191, 0.08);
        --bot-border: rgba(45, 212, 191, 0.16);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu, footer { display: none; }

    /* Keep the header transparent (not hidden) so the sidebar toggle stays usable */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    /* Hide only the deploy button, never the whole toolbar/header */
    [data-testid="stAppDeployButton"] { display: none; }

    /* Make sure the "open sidebar" control is always visible & on top */
    [data-testid="stSidebarCollapsedControl"] {
        visibility: visible !important;
        opacity: 1 !important;
        z-index: 999999 !important;
    }
    [data-testid="stSidebarCollapsedControl"] button {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        color: var(--text) !important;
    }

    /* Ambient gradient background */
    .stApp {
        background:
            radial-gradient(900px 500px at 15% -10%, rgba(124, 92, 255, 0.16), transparent 60%),
            radial-gradient(800px 500px at 100% 0%, rgba(45, 212, 191, 0.10), transparent 55%),
            var(--bg);
        color: var(--text);
    }

    .block-container {
        padding-top: 1.5rem;
        max-width: 820px;
    }

    /* Header */
    .chat-header {
        text-align: center;
        padding: 1.25rem 0 0.5rem 0;
    }
    .chat-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.72rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        color: var(--muted);
        background: var(--surface);
        border: 1px solid var(--border);
        padding: 0.3rem 0.75rem;
        border-radius: 999px;
        margin-bottom: 0.85rem;
    }
    .chat-badge .dot {
        width: 6px; height: 6px; border-radius: 50%;
        background: var(--accent-2);
        box-shadow: 0 0 8px var(--accent-2);
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.35; } }

    .chat-header h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.4rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        line-height: 1.1;
        background: linear-gradient(120deg, #ffffff 0%, #b8a9ff 45%, #6ee7d7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 0.35rem 0;
    }
    .chat-header p {
        color: var(--muted);
        font-size: 0.92rem;
        margin: 0;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3.5rem 1rem 2rem;
        color: var(--muted);
    }
    .empty-state .glyph {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
        opacity: 0.85;
    }
    .empty-state h3 {
        color: var(--text);
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        font-size: 1.15rem;
        margin: 0 0 0.4rem 0;
    }
    .empty-state p { font-size: 0.9rem; margin: 0; }

    /* Chat messages */
    .stChatMessage {
        background: transparent !important;
        padding: 0.2rem 0 !important;
    }
    [data-testid="stChatMessage"] {
        backdrop-filter: blur(8px);
        border-radius: 18px;
        padding: 0.9rem 1.1rem !important;
        margin-bottom: 0.6rem;
        transition: transform 0.15s ease, border-color 0.2s ease;
    }
    [data-testid="stChatMessage"]:hover {
        transform: translateY(-1px);
    }

    /* User bubble */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
        background: var(--user) !important;
        border: 1px solid var(--user-border);
    }
    /* Assistant bubble */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
        background: var(--bot) !important;
        border: 1px solid var(--bot-border);
    }

    /* Avatars */
    [data-testid="stChatMessageAvatarUser"],
    [data-testid="stChatMessageAvatarAssistant"] {
        border-radius: 12px !important;
    }

    /* Input */
    [data-testid="stChatInput"], .stChatInputContainer {
        border: none !important;
        background: transparent !important;
    }
    textarea[data-testid="stChatInputTextArea"],
    [data-testid="stChatInput"] textarea {
        background-color: var(--bg-soft) !important;
        border: 1px solid var(--border) !important;
        border-radius: 16px !important;
        color: var(--text) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 0.85rem 1rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    textarea[data-testid="stChatInputTextArea"]:focus,
    [data-testid="stChatInput"] textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(124, 92, 255, 0.18) !important;
    }
    [data-testid="stChatInput"] button {
        border-radius: 12px !important;
        background: linear-gradient(135deg, var(--accent), #5b3df0) !important;
        color: #fff !important;
        border: none !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: var(--bg-soft);
        border-right: 1px solid var(--border);
    }
    section[data-testid="stSidebar"] h2 {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
    }
    .stButton button {
        border-radius: 12px !important;
        border: 1px solid var(--border) !important;
        background: var(--surface) !important;
        color: var(--text) !important;
        font-weight: 500 !important;
        transition: all 0.18s ease;
    }
    .stButton button:hover {
        border-color: var(--accent) !important;
        background: rgba(124, 92, 255, 0.12) !important;
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.1);
        border-radius: 8px;
    }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    model_choice = st.selectbox(
        "Model",
        ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"],
        index=0,
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)

    st.divider()
    if st.button("🗑️  Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Powered by OpenAI + LangChain")

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
    <div class="chat-badge"><span class="dot"></span> Online · Ready to chat</div>
    <h1>AI Chat</h1>
    <p>Your intelligent assistant — ask me anything</p>
</div>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Empty state ───────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <div class="glyph">✦</div>
        <h3>Start a conversation</h3>
        <p>Type a message below and let's get going.</p>
    </div>
    """, unsafe_allow_html=True)

# ── Display chat history ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    role = "user" if msg["role"] == "user" else "assistant"
    avatar = "🧑" if role == "user" else "🤖"
    with st.chat_message(role, avatar=avatar):
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ketik pesanmu di sini..."):

    # Cek API key
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("⚠️ Masukkan OpenAI API Key di sidebar terlebih dahulu.")
        st.stop()

    # Tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # Bangun history untuk LangChain
    lc_messages = [SystemMessage("You are a helpful and friendly AI assistant.")]
    for m in st.session_state.messages:
        if m["role"] == "user":
            lc_messages.append(HumanMessage(m["content"]))
        else:
            lc_messages.append(AIMessage(m["content"]))

    # Panggil model & streaming
    client = ChatOpenAI(model=model_choice, temperature=temperature, streaming=True)
    with st.chat_message("assistant", avatar="🤖"):
        response_text = st.write_stream(client.stream(lc_messages))

    st.session_state.messages.append({"role": "assistant", "content": response_text})

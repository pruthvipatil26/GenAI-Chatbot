import streamlit as st
from chatbot.gemini_client import GeminiClient
from chatbot.memory_manager import MemoryManager
from chatbot.prompt_builder import build_prompt


## Page Configuration ##

st.set_page_config(
    page_title="AgriGen AI",
    page_icon="🌾",
    layout="wide"
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #f3f9f1 0%, #ffffff 55%, #eef5e9 100%);
            color: #1e3d24;
        }
        .header {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 20px 50px rgba(24, 90, 52, 0.08);
        }
        .section-box {
            background: rgba(255, 255, 255, 0.94);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 8px 30px rgba(56, 110, 78, 0.08);
        }
        .footer {
            margin-top: 28px;
            padding: 14px;
            color: #4f6c4f;
            text-align: center;
            font-size: 0.92rem;
            opacity: 0.8;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("🌾 AgriGen AI")
    st.subheader("Smart agriculture advice for farmers and agronomy teams")
    st.markdown(
        "Get practical guidance on crops, soil, pests, irrigation, harvesting, and sustainable farm operations."
    )
    st.markdown('</div>', unsafe_allow_html=True)


## Sidebar ##

with st.sidebar:
    st.header("AgriGen AI Helper")
    st.write(
        "Ask about crop selection, soil health, pest control, irrigation planning, livestock care, and farm sustainability."
    )
    st.write("---")
    st.subheader("Try these questions")
    st.write("• What are the best practices for maize irrigation?")
    st.write("• How can I improve soil fertility organically?")
    st.write("• How do I manage aphids in vegetable crops?")
    st.write("• What are climate-smart farming tips for small farms?")
    st.write("---")
    if st.button("Reset Conversation"):
        st.session_state.memory.clear_memory()
        st.experimental_rerun()


## Initialize Session State ##

if "memory" not in st.session_state:
    st.session_state.memory = MemoryManager()

if "client" not in st.session_state:
    st.session_state.client = GeminiClient()


## Chat Input ##

user_input = st.chat_input("Ask a farming or agriculture question...")

if user_input:
    memory = st.session_state.memory
    client = st.session_state.client

    # Add user message
    memory.add_user_message(user_input)

    # Build prompt
    prompt = build_prompt(user_input)

    # Generate response
    response = client.generate_response(prompt, memory.get_history())

    # Add bot response
    memory.add_bot_message(response)


## Display Chat History ##

with st.container():
    if len(st.session_state.memory.get_history()) == 0:
        st.info("Start the conversation by asking a farm or agriculture-related question.")

    for msg in st.session_state.memory.get_history():
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["parts"][0])
        else:
            with st.chat_message("assistant"):
                st.write(msg["parts"][0])


st.markdown(
    '<div class="footer">AgriGen AI • Farming-ready GenAI Assistant • Powered by Pruthviraj Patil</div>',
    unsafe_allow_html=True,
)
    
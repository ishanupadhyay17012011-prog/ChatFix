import streamlit as st
import requests

st.set_page_config(page_title="ChatFix", page_icon="💬", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💬 ChatFix</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>AI-powered reply generator</p>", unsafe_allow_html=True)
st.caption("Built by Ishan 🚀")

st.divider()

# Input
message = st.text_area("📩 Paste the message", placeholder="Type or paste the message here...")

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("🎭 Tone", ["Friendly", "Professional", "Confident", "Funny"])

with col2:
    context = st.selectbox("👤 Context", ["Friend", "Crush", "Boss", "Stranger"])

# Extra mode
mode = st.selectbox("🔥 Mode", ["Normal", "Flirty ❤️", "Savage 😈", "Apology 🙏"])

st.divider()

if st.button("✨ Generate Reply", use_container_width=True):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        with st.spinner("Thinking... 🤔"):
            api_key = st.secrets["OPENROUTER_API_KEY"]

            prompt = f"""
            You are a smart assistant.

            Generate 3 replies based on:
            Tone: {tone}
            Context: {context}
            Mode: {mode}

            Message:
            {message}

            Rules:
            - Keep replies short
            - Make them realistic
            - Sound human, not robotic
            - Number them clearly (1, 2, 3)
            """

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            )

            result = response.json()

            try:
                reply = result["choices"][0]["message"]["content"]

                st.success("💡 Here are your replies:")

                replies = reply.split("\n")

                for i, r in enumerate(replies):
                    if r.strip():
                        st.markdown(f"### {r}")
                        st.code(r, language=None)

            except Exception as e:
                st.error(f"Error: {result}")

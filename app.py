import streamlit as st
import requests

st.set_page_config(page_title="ChatFix", page_icon="💬", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💬 ChatFix</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>AI-powered reply generator</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px; color: grey;'>ChatFix • AI Assistant</p>", unsafe_allow_html=True)

st.divider()

# Input
message = st.text_area("📩 Paste the message", placeholder="Type or paste the message here...")

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("🎭 Tone", ["Friendly", "Professional", "Confident", "Funny"])

with col2:
    context = st.selectbox("👤 Context", ["Friend", "Crush", "Boss", "Stranger"])

# Mode
mode = st.selectbox("🔥 Mode", ["Normal", "Flirty ❤️", "Savage 😈", "Apology 🙏"])

st.divider()

if st.button("✨ Generate Reply", use_container_width=True):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        with st.spinner("Thinking... 🤔"):
            api_key = st.secrets["OPENROUTER_API_KEY"]

            prompt = f"""
Generate exactly 3 different replies.

Tone: {tone}
Context: {context}
Mode: {mode}

Message:
{message}

Rules:
- Output ONLY 3 replies
- Each reply must be on a NEW LINE
- Do NOT combine replies
- Do NOT add numbering or extra text
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

                # Clean and split replies
                lines = [line.strip() for line in reply.split("\n") if line.strip()]

                # Fallback if AI sends one block
                if len(lines) < 3:
                    lines = reply.replace(".", ".\n").split("\n")

                clean_replies = [line.strip() for line in lines if line.strip()]

                st.success("💡 Replies:")

                for r in clean_replies[:3]:
                    st.markdown(f"""
                    <div style="
                        padding: 12px;
                        border-radius: 10px;
                        background-color: #1e1e1e;
                        margin-bottom: 10px;
                        font-size: 15px;
                    ">
                        {r}
                    </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {result}")

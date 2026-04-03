import streamlit as st
import requests

st.set_page_config(page_title="ChatFix", page_icon="💬", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💬 ChatFix</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>AI-powered reply generator</p>", unsafe_allow_html=True)

st.divider()

message = st.text_area("📩 Paste the message")

col1, col2 = st.columns(2)

with col1:
    tone = st.selectbox("🎭 Tone", ["Friendly", "Professional", "Confident", "Funny"])

with col2:
    context = st.selectbox("👤 Context", ["Friend", "Crush", "Boss", "Stranger"])

st.divider()

if st.button("✨ Generate Reply", use_container_width=True):
    if message.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        api_key = st.secrets["OPENROUTER_API_KEY"]

        prompt = f"""
        Generate 3 {tone} replies for a message from a {context}.
        Message: {message}
        Keep replies short and natural.
        """

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mistralai/mistral-7b-instruct",
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
            st.success("Here are your replies:")
            st.write(reply)
        except:
            st.error("Something went wrong. Try again.")

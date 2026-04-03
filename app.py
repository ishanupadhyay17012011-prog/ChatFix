import streamlit as st

st.set_page_config(page_title="ChatFix", page_icon="💬", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>💬 ChatFix</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>AI-powered reply generator</p>", unsafe_allow_html=True)

st.divider()

# Input
st.markdown("### 📩 Message")
message = st.text_area("", placeholder="Paste the message you received...")

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
        st.success("Here are your replies:")

        st.markdown("**1.** That sounds great! Let me think about it and get back to you.")
        st.markdown("**2.** I appreciate your message — here’s a smarter way to respond.")
        st.markdown("**3.** Got it! This reply sounds more confident and clear.")

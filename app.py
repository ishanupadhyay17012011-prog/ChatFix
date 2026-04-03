import streamlit as st

st.set_page_config(page_title="ChatFix", page_icon="💬")

st.title("💬 ChatFix")
st.write("Fix your replies instantly")

message = st.text_area("Paste message")

tone = st.selectbox("Tone", ["Friendly", "Professional", "Confident", "Funny"])
context = st.selectbox("Context", ["Friend", "Crush", "Boss", "Stranger"])

if st.button("Generate"):
    if message:
        st.write("Reply 1: Nice response")
        st.write("Reply 2: Better response")
        st.write("Reply 3: Smart response")
    else:
        st.warning("Enter a message")

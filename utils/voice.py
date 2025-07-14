import streamlit as st
import requests

def voice_tab(groq_key):
    st.subheader("🎤 Voice Assistant")
    st.markdown("Use external mic-to-text tool, then paste result here:")

    voice_text = st.text_area("Your spoken message (converted to text):")

    if st.button("🎧 Ask"):
        if voice_text.strip():
            headers = {
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json"
            }
            body = {
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": "You're Daniel, a helpful AI."},
                    {"role": "user", "content": voice_text}
                ]
            }
            res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
            reply = res.json()["choices"][0]["message"]["content"]
            st.markdown(f"**Daniel:** {reply}")
            st.markdown(f'<audio autoplay src="https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={requests.utils.quote(reply)}"></audio>', unsafe_allow_html=True)
        else:
            st.warning("Paste a message first.")

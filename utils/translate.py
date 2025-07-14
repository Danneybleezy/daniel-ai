import streamlit as st
import requests

def translate_tab(groq_key):
    st.subheader("🌍 Translate Anything")

    text = st.text_area("Text to translate")
    target = st.selectbox("Translate to", ["French", "Spanish", "Arabic", "Igbo", "Yoruba", "Chinese"])

    if st.button("🌐 Translate"):
        system_prompt = f"You are a translator. Translate the user's message to {target}."
        headers = {
            "Authorization": f"Bearer {groq_key}",
            "Content-Type": "application/json"
        }
        body = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
        }
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
        translation = res.json()["choices"][0]["message"]["content"]
        st.success(translation)

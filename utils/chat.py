import streamlit as st
import requests

def chat_tab(groq_key, personality_mode=False):
    st.subheader("🧠 Ask Daniel Anything")

    if personality_mode:
        role = st.selectbox("Choose a personality:", [
            "Friendly Assistant", "Motivational Coach", "Sarcastic Friend", "Professional Advisor"
        ])
        system_prompt = {
            "Friendly Assistant": "You're Daniel, a kind and helpful friend.",
            "Motivational Coach": "You're Daniel, a passionate motivational coach.",
            "Sarcastic Friend": "You're Daniel, sarcastic but clever.",
            "Professional Advisor": "You're Daniel, a professional business advisor."
        }[role]
    else:
        system_prompt = "You're Daniel, a helpful AI assistant."

    user_input = st.text_input("You:", placeholder="Ask anything...")
    speak = st.checkbox("🔊 Read aloud")

    if user_input:
        with st.spinner("Thinking..."):
            headers = {
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json"
            }
            body = {
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            }
            res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
            reply = res.json()["choices"][0]["message"]["content"]
            st.markdown(f"**Daniel:** {reply}")
            if speak:
                st.markdown(f'<audio autoplay src="https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={requests.utils.quote(reply)}"></audio>', unsafe_allow_html=True)

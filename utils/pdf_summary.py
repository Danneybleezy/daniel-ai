import streamlit as st
import fitz  # PyMuPDF

def pdf_summary_tab(groq_key):
    st.subheader("📄 PDF Summarizer")

    file = st.file_uploader("Upload PDF", type=["pdf"])
    if file:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        st.text_area("Extracted Text", text, height=200)

        if st.button("🧠 Summarize"):
            headers = {
                "Authorization": f"Bearer {groq_key}",
                "Content-Type": "application/json"
            }
            body = {
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": "Summarize this PDF:"},
                    {"role": "user", "content": text[:3000]}
                ]
            }
            res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
            summary = res.json()["choices"][0]["message"]["content"]
            st.markdown("**Summary:**")
            st.markdown(summary)

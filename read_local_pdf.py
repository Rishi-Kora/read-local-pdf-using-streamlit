import streamlit as st
import pdfplumber
import os

st.title("📂 Local PDF Reader")

# Specify the full local file path here
pdf_path = "C:/Users/DELL/Documents/Projects/llm_engineering/my_projects/functionalsample.pdf"

# Check if file exists
if os.path.exists(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if text.strip():
            st.subheader(f"📄 Extracted Text from: {os.path.basename(pdf_path)}")
            st.text_area("Text Output", text, height=600)
        else:
            st.warning("⚠️ No extractable text found in the PDF.")
    except Exception as e:
        st.error(f"❌ Failed to read the PDF: {e}")
else:
    st.error(f"❌ File not found: {pdf_path}")





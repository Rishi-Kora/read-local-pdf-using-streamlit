# read-local-pdf-using-streamlit
This Streamlit application is designed to read and extract text from a **PDF file located on your local system** using the `pdfplumber` library. It does not require file uploads through the UI. Instead, it reads a hardcoded PDF path and displays its contents in a scrollable text area.

---

## 🧰 Features

- Reads a PDF from a fixed file path on your system
- Uses `pdfplumber` to extract text
- Displays extracted text in a scrollable box
- Provides error messages if:
  - The file path is incorrect
  - The file is not a valid PDF
  - The PDF has no readable text

---

## 🗂 Directory & File Structure

```

├── read_local_pdf.py
├── functionalsample.pdf  ← this file must exist at the given path
```

---

## 🖥️ Code Behavior

- **Hardcoded File Path**:
  ```python
  pdf_path = "C:/Users/DELL/Documents/Projects/llm_engineering/my_projects/functionalsample.pdf"
  ```

- **Text Extraction**:
  - Each page is processed using `pdfplumber`
  - Text is concatenated and shown via `st.text_area`

- **Error Handling**:
  - File not found → `st.error`
  - PDF fails to open → `st.error`
  - No extractable text → `st.warning`

---

## 📦 Requirements

Install required packages:

```bash
pip install streamlit pdfplumber
```

---

## ▶️ How to Run

```bash
streamlit run read_local_pdf.py
```

Make sure the file `functionalsample.pdf` exists at the specified path or update the `pdf_path` variable accordingly.

---

## 📌 Notes

- This script is best used when testing fixed documents stored locally.
- For dynamic uploads, consider using `st.file_uploader()` instead.

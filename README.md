#  Smart Assistant for Research Summarization

An intelligent, document-aware GenAI assistant that can understand and reason over research papers, legal texts, and other large documents. Built to answer user questions and generate logic-based quizzes with justification — all grounded in the actual content of uploaded PDF or TXT files.

---

##  Features

- **Upload PDF/TXT Documents**  
  Parse and read structured documents like research papers and reports.

- **Ask Anything Mode**  
  Users can ask free-form questions based on the uploaded document. The assistant responds with accurate answers and supporting context.

-  **Challenge Me Mode**  
  Automatically generate logic/comprehension-based questions from the document. User responses are evaluated and justified with reference to document content.

-  **Auto Summary**  
  Automatically generates a concise summary (≤150 words) of the uploaded document.

- **Contextual Justification**  
  Every answer and evaluation includes reference to the relevant document snippet.

---

##  Architecture

###  Frontend:  
- **Streamlit** – Provides a clean and interactive web-based UI.

###  Backend:  
- **FastAPI** – Handles RESTful API routes for question answering and generation.
- **Transformers (HuggingFace)** – RoBERTa for QA, DistilBART for summarization.
- **spaCy** – Sentence parsing and linguistic preprocessing.
- **Sentence-Transformers** – Semantic similarity for evaluation logic.
- **pdfplumber** – Extracts text from PDF files.

###  Structure

'''smart-assistant/
├── app.py # Streamlit app
├── api_server.py # FastAPI endpoints for QA & logic questions
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── postman_collection.json # API testing (import into Postman)
├── backend/
│ ├── document_handler.py # PDF/TXT text extraction
│ ├── qa_engine.py # Question answering logic
│ ├── question_generator.py # Logic question generation & evaluation
│ └── summarizer.py # Document summarization logic'''

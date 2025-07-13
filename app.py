
import streamlit as st
from backend.document_handler import extract_text_from_pdf
from backend.summarizer import get_summary
from backend.qa_engine import answer_question
from backend.question_generator import generate_questions, evaluate_answer

st.set_page_config(page_title="Smart Assistant for Research", layout="wide")
st.title("📘 Smart Assistant for Research Summarization")

uploaded = st.file_uploader("Upload PDF or TXT", type=['pdf', 'txt'])

if uploaded:
    if uploaded.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded)
    else:
        text = uploaded.read().decode()

    with st.expander("📄 Full Document Text"):
        st.write(text)

    st.subheader("📝 Summary")
    st.write(get_summary(text)[:150] + "...")

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Enter your question:")
        if question:
            answer, score = answer_question(question, text)
            st.success(f"Answer: {answer}")
            st.caption(f"Confidence Score: {score:.2f}")

    elif mode == "Challenge Me":
        st.info("Generating logic-based questions...")
        questions = generate_questions(text)
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i+1}: {q}**")
            user_ans = st.text_input(f"Your Answer to Q{i+1}")
            if user_ans:
                score = evaluate_answer(user_ans, q)
                st.write(f"✅ Similarity Score: {score:.2f}")
                st.caption("Correctness is judged based on similarity to original sentence.")

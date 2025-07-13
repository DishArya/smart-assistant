
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(question, context):
    response = qa_pipeline(question=question, context=context)
    return response['answer'], response['score']

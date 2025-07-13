
from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_summary(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summarized = summarizer(chunks, max_length=150, min_length=40, do_sample=False)
    return " ".join([chunk['summary_text'] for chunk in summarized])

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.qa_engine import answer_question
from backend.question_generator import generate_questions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QARequest(BaseModel):
    question: str
    context: str

class GenRequest(BaseModel):
    context: str
    num: int = 3

@app.post("/ask")
def ask_anything(req: QARequest):
    answer, score = answer_question(req.question, req.context)
    return {"answer": answer, "score": round(score, 3)}

@app.post("/generate")
def generate(req: GenRequest):
    questions = generate_questions(req.context, req.num)
    return {"questions": questions}

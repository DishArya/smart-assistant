import random
import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

def generate_questions(context, num=3):
    doc = nlp(context)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 20]
    selected = random.sample(sentences, min(num, len(sentences)))
    questions = [f"What does the following mean: '{sent}'?" for sent in selected]
    return questions

def evaluate_answer(user_answer, correct_sentence):
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('all-MiniLM-L6-v2')
    score = util.cos_sim(
        model.encode(user_answer, convert_to_tensor=True),
        model.encode(correct_sentence, convert_to_tensor=True)
    )
    return float(score[0][0])

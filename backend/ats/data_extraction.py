import fitz  # PyMuPDF
import spacy
from sentence_transformers import SentenceTransformer, util

# Load NLP models once at the top
nlp = spacy.load("en_core_web_sm")  # lightweight spaCy model
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # fast and accurate

# ---- Step 1: Extract text from PDF ----
def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = "".join(page.get_text() for page in doc)
    doc.close()
    return text.strip()

# ---- Step 2: Extract relevant entities (skills, titles, degrees, etc.) ----
def extract_keywords(text: str) -> set:
    doc = nlp(text)
    keywords = set()

    for ent in doc.ents:
        if ent.label_ in {"ORG", "PRODUCT", "SKILL", "WORK_OF_ART", "PERSON", "NORP"}:
            keywords.add(ent.text.lower())

    for token in doc:
        if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop:
            keywords.add(token.lemma_.lower())

    return keywords
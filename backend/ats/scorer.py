import fitz  # PyMuPDF
import spacy
from sentence_transformers import SentenceTransformer, util

# Load NLP models once at the top
nlp = spacy.load("en_core_web_sm")  # lightweight spaCy model
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # fast and accurate

# ---- Step 3: Semantic similarity between entire documents ----
def semantic_similarity(text1: str, text2: str) -> float:
    emb1 = embedder.encode(text1, convert_to_tensor=True)
    emb2 = embedder.encode(text2, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(emb1, emb2).item()
    return round(sim * 100, 2)  # return as percentage

# ---- Step 4: Keyword/entity overlap ----
def keyword_overlap_score(resume_keywords: set, jd_keywords: set) -> float:
    if not jd_keywords:
        return 0.0
    matched = resume_keywords & jd_keywords
    return round(len(matched) / len(jd_keywords) * 100, 2)
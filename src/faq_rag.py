import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json
from src.faqs import FAQS

model = SentenceTransformer("all-MiniLM-L6-v2")


def build_index():
    questions = [faq["question"] for faq in FAQS]
    embeddings = model.encode(questions).astype("float32")
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    return index


index = build_index()


def ask_faq(query, threshold=0.5):
    query_embedding = model.encode([query]).astype("float32")
    faiss.normalize_L2(query_embedding)

    distance, indices = index.search(query_embedding, k=1)

    score = distance[0][0]
    idx = indices[0][0]

    if score < threshold:
        return json.dumps({
            "answer": None,
            "confidence": 0.2
        })
    return json.dumps({
        "answer": FAQS[idx]["answer"],
        "confidence": round(float(score), 2)
    })

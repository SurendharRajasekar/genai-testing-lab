import json
import numpy as np
from sentence_transformers import SentenceTransformer
from src.policy_docs import POLICY_TEXT

# load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text):
    return [chunk.strip() for chunk in text.split("\n") if chunk.strip()]


def build_index():
    chunks = chunk_text(POLICY_TEXT)
    embeddings = model.encode(chunks)
    return chunks, embeddings


def retrieve(query, threshold=0.4):
    chunks, embeddings = build_index()

    query_embedding = model.encode([query])[0]

    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    best_index = np.argmax(similarities)
    best_score = similarities[best_index]

    if best_score < threshold:
        return None, best_score

    return chunks[best_index], float(best_score)


def generate_answer(query):
    context, score = retrieve(query)

    if context is None:
        return json.dumps({
            "answer": None,
            "confidence": 0.2
        })

    return json.dumps({
        "answer": context,
        "confidence": round(score, 2)
    })

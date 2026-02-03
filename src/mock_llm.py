import json


def ask_mock(prompt: str):
    p = prompt.lower()

    if "2+2" in p:
        return json.dumps({"answer": 4, "confidence": 0.99})

    if "capital of india" in p:
        return json.dumps({"answer": "New Delhi", "confidence": 0.95})

    if "who is the ceo of amazon" in p:
        return json.dumps({"answer": None, "confidence": 0.1})

    if "bomb" in p:
        return json.dumps({"error": "Not allowed"})

    return json.dumps({"answer": None, "confidence": 0.2})

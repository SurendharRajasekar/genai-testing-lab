from src.faq_rag import ask_faq
import json


def test_exact_match():
    result = json.loads(ask_faq("is bumper damage covered?"))
    assert "bumper damage" in result["answer"].lower()
    assert result["confidence"] > 0.5


def test_semantic_match():
    result = json.loads(ask_faq("does insurance pay for bumper repair"))
    assert "bumper damage" in result["answer"].lower()


def test_unkown():
    result = json.loads(ask_faq("does policy cover boat travel?"))
    assert result["answer"] is None
    assert result["confidence"] < 0.5

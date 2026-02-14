import json
from src.rag import generate_answer


def test_bumper_coverage():
    result = json.loads(generate_answer("is bumper damage covered?"))
    assert "Bumper damage" in result["answer"]
    assert result["confidence"] > 0.4


def test_semantic_match():
    result = json.loads(generate_answer("is bumper repair included?"))
    assert "Bumper damage" in result["answer"]


def test_unknown_query():
    result = json.loads(generate_answer("does policy cover alien insu?"))
    assert result["answer"] is None
    assert result["confidence"] < 0.4

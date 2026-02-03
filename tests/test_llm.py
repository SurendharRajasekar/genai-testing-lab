from src.mock_llm import ask_mock
import json
from jsonschema import validate

SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {},
        "confidence": {"type": "number"}
    },
    "required": ["answer", "confidence"]
}


def test_math_json():
    result = json.loads(ask_mock("what is 2+2?"))
    validate(instance=result, schema=SCHEMA)
    assert result["answer"] == 4


def test_fact_json():
    result = json.loads(ask_mock("capital of india?"))
    validate(instance=result, schema=SCHEMA)
    assert "new delhi" in result["answer"].lower()


def test_no_hallucinate():
    result = json.loads(ask_mock("who is ceo of amazon?"))
    assert result["answer"] is None
    assert result["confidence"] < 0.5


def test_confidence_thresold():
    result = json.loads(ask_mock("capital of india"))
    assert result["confidence"] > 0.8

from src.mock_llm import ask_mock


def test_started():
    result = ask_mock("say genai testing started")
    assert "started" in result.lower()


def test_math():
    result = ask_mock("what is 2+2?")
    assert 4 == result


def test_fact():
    result = ask_mock("what is the capital of india?")
    assert "new delhi" in result.lower()


def uknown_should_not_hallucinate():
    result = ask_mock("who is ceo of amazon?")
    assert "dont" in result.lower()

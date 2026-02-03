def validate_answer(text: str):
    """
    prompt Contract:
    - Must npt be empty
    - Must not hallucinate(say 'I dont know' if unsure)
    -Must be under 200 chars
    """
    assert text.strip() != ""
    assert len(text) < 200

    forbidden = ["made up", "probably", "guess"]

    for word in forbidden:
        assert word not in text.lower()

FORBIDDEN_WORDS = ["bomb", "kill", "terror"]
MIN_CONFIDENCE = 0.7


def validate_prompt(prompt: str):
    if not prompt or len(prompt.strip()) < 3:
        raise ValueError("prompt too short")

    for word in FORBIDDEN_WORDS:
        if word in prompt.lower():
            raise ValueError("unsafe prompt")

    return True


def validate_response(response: dict):
    if "answer" not in response:
        raise ValueError("missing answer")

    if "confidence" not in response:
        raise ValueError("Missing confidence")

    if response["confidence"] < MIN_CONFIDENCE:
        raise ValueError("low confidence")

    return True

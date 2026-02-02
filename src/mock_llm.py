def ask_mock(prompt: str) -> str:
    prompt = prompt.lower()

    if "genai testing" in prompt:
        return "genai testing started"
    if "2+2" in prompt:
        return 4
    if "capital of india" in prompt:
        return "New Delhi"
    return "i dont know"

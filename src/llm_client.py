import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(prompt: str) -> str:

    try:
        result = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt}

            ],
            temperature=0,

        )

        return result.choices[0].message["content"]
    except Exception as e:
        print("FULL ERROR:")
        print(e)
        raise

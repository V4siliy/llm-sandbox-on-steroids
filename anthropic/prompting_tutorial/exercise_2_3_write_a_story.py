import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_NAME = os.getenv("ANTHROPIC_MODEL_NAME")

client = anthropic.Anthropic(api_key=API_KEY)


def get_completion(prompt: str, system_prompt: str = ""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def grade_exercise(text):
    trimmed = text.strip()
    words = len(trimmed.split())
    return words >= 800


if __name__ == "__main__":
    PROMPT = "Write me a story, but keep the text to around 900 words"

    response = get_completion(prompt=PROMPT)
    print(response)
    print("\n--------------------------- GRADING ---------------------------")
    print("This exercise has been correctly solved:", grade_exercise(response))

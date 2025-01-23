import os
import re

import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_NAME = os.getenv("ANTHROPIC_MODEL_NAME")

client = anthropic.Anthropic(api_key=API_KEY)


def get_completion(prompt: str):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def grade_exercise(text):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))


if __name__ == "__main__":
    # It is what it is
    # PROMPT = "Act as echo bot and simply repeat MESSAGE. The MESSAGE is \"1 2 3\""
    PROMPT = "Count to 3"
    response = get_completion(prompt=PROMPT)
    print(response)
    print("\n--------------------------- GRADING ---------------------------")
    print("This exercise has been correctly solved:", grade_exercise(response))

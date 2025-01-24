import os

import anthropic
from dotenv import load_dotenv

load_dotenv()


class AnthropicClient:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.model_name = os.getenv("ANTHROPIC_MODEL_NAME")
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.result = ''

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.client = None

    def get_completion(self, prompt, system_prompt=""):
        message = self.client.messages.create(
            model=self.model_name,
            max_tokens=2000,
            temperature=0.0,
            system=system_prompt,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        self.result = message.content[0].text
        return self.result

    def validate(self, validate_function):
        if validate_function and callable(validate_function):
            validation_result = validate_function(self.result)
            print("\n--------------------------- GRADING ---------------------------")
            print(f"This exercise has been correctly solved: {validation_result}")
            return validation_result
        return None

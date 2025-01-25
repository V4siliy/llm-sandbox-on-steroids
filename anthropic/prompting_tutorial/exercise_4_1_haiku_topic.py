import re

from common import AnthropicClient


if __name__ == "__main__":
    TOPIC = "Pigs"

    PROMPT = f"Write a haike about {TOPIC}"

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("pigs", text.lower()) and re.search("haiku", text.lower()))

        client.validate(_grade_exercise)

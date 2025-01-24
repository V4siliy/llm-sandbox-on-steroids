import re

from common import AnthropicClient


if __name__ == "__main__":
    SYSTEM_PROMPT = "Respond like a three-year-old child"
    PROMPT = "How big is the sky?"

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT, SYSTEM_PROMPT)
        print(response)


        def _grade_exercise(text):
            return bool(re.search(r"giggles", text) or re.search(r"soo", text))

        client.validate(_grade_exercise)

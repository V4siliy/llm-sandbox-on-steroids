import re

from common import AnthropicClient


if __name__ == "__main__":
    ANIMAL = "cats"

    PROMPT = f"Please write two haiku about {ANIMAL}. Put it in <haiku> tags."

    PREFILL = "<haiku>"

    with AnthropicClient() as client:
        response = client.get_completion(PROMPT, prefill=PREFILL)
        print(response)

        def _grade_exercise(text):
            return bool(
                (re.search("cat", text.lower()) and re.search("", text))
                and (text.count("\n") + 1) > 5
            )

        client.validate(_grade_exercise)

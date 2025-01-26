import re

from common import AnthropicClient


if __name__ == "__main__":
    ANIMAL_1 = "Cat"
    ANIMAL_2 = "Dog"

    PROMPT = (f"Please write two different haikus, one about {ANIMAL_1} and one about {ANIMAL_2}. "
              f"Put each in <haiku> tags.")

    PREFILL = "<haiku>"

    with AnthropicClient() as client:
        response = client.get_completion(PROMPT, prefill=PREFILL)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("tail", text.lower()) and re.search("cat", text.lower()) and re.search("", text))

        client.validate(_grade_exercise)

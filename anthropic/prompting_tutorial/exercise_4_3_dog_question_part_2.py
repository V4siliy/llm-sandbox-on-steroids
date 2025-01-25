import re

from common import AnthropicClient


if __name__ == "__main__":
    QUESTION = "ar cn brown?"

    PROMPT = (f"Hia its me i have a q about dogs {QUESTION} "
              f"tx it help me muhch much atx fst fst answer short short tx")

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("brown", text.lower()))

        client.validate(_grade_exercise)

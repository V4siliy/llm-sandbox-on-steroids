import re

from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = ("In what year did star performer Beyoncé release her eighth studio album? "
              "If you don't know, say that.")

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)

        def _grade_exercise(text):
            contains = bool(
                re.search("Unfortunately", text) or
                re.search("I do not", text) or
                re.search("I don't", text)
            )
            does_not_contain = not bool(re.search("2022", text))
            return contains and does_not_contain

        client.validate(_grade_exercise)

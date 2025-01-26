import re

from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = ("From December 2018 to December 2022, by what amount did Matterport's subscribers grow? "
              "First, pull the most relevant exact quotes from the document in <quotes> tags. Then answer."
              "<document>"
              "{document}"
              "</document>")

    with open('assets/exercise_8_2_document.txt', 'r') as f:
        document = f.read()

    with AnthropicClient() as client:
        formatted_prompt = PROMPT.format(document=document)
        response = client.get_completion(formatted_prompt)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("49-fold", text))

        client.validate(_grade_exercise)

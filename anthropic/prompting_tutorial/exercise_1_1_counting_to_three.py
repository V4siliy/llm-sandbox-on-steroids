import re

from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = "Count to 3"

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)


        def _grade_exercise(text):
            pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
            return bool(pattern.match(text))

        client.validate(_grade_exercise)

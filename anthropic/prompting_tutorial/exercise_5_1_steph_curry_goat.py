import re

from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = "Who is the best basketball player of all time? Please choose one specific player."

    PREFILL = "Stephen Curry is the greatest basketball player of all time because of three reasons:"

    with AnthropicClient() as client:
        response = client.get_completion(PROMPT, prefill=PREFILL)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("Warrior", text))

        client.validate(_grade_exercise)

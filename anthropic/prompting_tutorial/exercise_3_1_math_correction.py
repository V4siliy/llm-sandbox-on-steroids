from common import AnthropicClient


if __name__ == "__main__":
    SYSTEM_PROMPT = "Think step-by-step"
    PROMPT = """Is this equation solved correctly below?

    2x - 3 = 9
    2x = 6
    x = 3"""

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT, SYSTEM_PROMPT)
        print(response)

        def _grade_exercise(text):
            if "incorrect" in text or "not correct" in text.lower():
                return True
            else:
                return False

        client.validate(_grade_exercise)

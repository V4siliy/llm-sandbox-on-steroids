from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = "Write me a story, but keep the text to around 900 words"

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)


        def _grade_exercise(text):
            trimmed = text.strip()
            words = len(trimmed.split())
            return words >= 800

        client.validate(_grade_exercise)

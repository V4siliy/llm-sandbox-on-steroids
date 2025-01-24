from common import AnthropicClient


if __name__ == "__main__":
    SYSTEM_PROMPT = "Act as a native spanish person, provide a short answer to question"
    PROMPT = "Hello Claude, how are you?"

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT, SYSTEM_PROMPT)
        print(response)


        def _grade_exercise(text):
            return "hola" in text.lower()

        client.validate(_grade_exercise)

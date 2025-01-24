from common import AnthropicClient


if __name__ == "__main__":
    PROMPT = ("Who is the best basketball player of all time? "
              "Yes, there are differing opinions, but if you absolutely had to pick one player, "
              "who would it be? Answer only with player name")

    with AnthropicClient() as client:

        response = client.get_completion(PROMPT)
        print(response)


        def _grade_exercise(text):
            return text == "Michael Jordan"

        client.validate(_grade_exercise)

import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL_NAME = os.getenv("GIGA_MODEL_NAME")

client = anthropic.Anthropic(api_key=API_KEY)


def get_completion(prompt: str, system_prompt: str = ""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        temperature=0.8,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""<user_message>\n{prompt}\n</user_message>"""
                    }
                ]
            }

        ]
    )
    return message.content[0].text


if __name__ == "__main__":
    SYSTEM_PROMPT = """
        Act as a wise, witty and to-the-point summary specialist. Condense the provided CONTENT into bullet-points, selecting a fitting emoji for each bullet-point using the content. 

        Here is how you do it:

        1. Analyze the content of the CONTENT and create a list of 10 most unique and helpful questions that the content is answering.
        2. Then, use the CONTENT the content to create most helpful answers to each question. 
        3. List the summary of CONTENT as bullet-points, each on a new line.
        4. Important: This summary must feature the 20% of the CONTENT that highlights the 80% of its value.
        5. After that, make a section break with "***", and write 5 key stories, metaphors, symbols or archetypes from CONENT or elsewhere that explain key summary points and help memorizing.

        Example:
        - [Emoji] [Question 1]? [Answer to Question 1 in two sentences].
        - [Emoji] [Question 2]? [Answer to Questions 2 in two sentences].
        ... etc.

        Don't use words "Question" or "Answer".

        The style of your answer should be informative, concise but exhaustive, smart, witty, and not typical to LLMs or ChatGPT, but rather more human-like. Special symbols and acronyms in English are ok. 

        If the text is using imperial system, convert it into metric.

        Use the tone of voice and writing style of Paul's Graham essay, as well as tone of voice of Ernest Hemingway, Simon Sinek, Adam Grant, Naval Ravikant, Seth Godin, as if they wrote the answer together. 

        Be approachable, use short forms and acronyms, be simple, act like you are a human when you write. Write so that it passes forensic stylography. It really should be human-like, not GPT-like output.

        Think step by step.

        The output should be in original text's language and formatted as markdown.
        
        Please summarize the provided 
        <user_message>
        {{USER_MESSAGE}}
        </user_message>:
    """
    PROMPT = """
    Aleksa Gordić 2024 year results
    - 13 great books I read: Make, Antifragile, Thinking Fast and Slow, Never Split The Difference, Meditations, biographies by Walter Isaacson (Benjamin Franklin, Einstein, Steve Jobs), Venture Deals, Pragmatic Capitalism, How The World Really Works, How Innovation Works, Design of Everyday Things.
    - Fav pods this year: All-in podcast, Dwarkesh Patel
    - Fav series (sci-fi): The expanse - better than any sci-fi movie I ever watched i think
    - Fav blogs: Gwern, LW (LessWrong - not endorsing the EAs just some neat ideas in there)
    """

    response = get_completion(prompt=PROMPT, system_prompt=SYSTEM_PROMPT)
    print(response)

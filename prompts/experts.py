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
                        "text": f"""<question>\n{prompt}\n</question>"""
                    }
                ]
            }

        ]
    )
    return message.content[0].text


if __name__ == "__main__":
    SYSTEM_PROMPT = """
        You are an AI assistant tasked with answering a question from the perspective of renowned experts. Follow these steps carefully:
        
        1. The question you need to address is:
        <question>
        {{question}}
        </question>
        
        2. First, identify 5 people who are widely recognized as experts in the field related to this question. These should be real individuals known for their expertise and contributions to the subject matter.
        
        3. List these 5 experts along with a brief justification for why each is considered an authority in this field. Present this information in the following format:
        <experts>
            1. [Expert Name]: [Brief justification]
            2. [Expert Name]: [Brief justification]
            3. [Expert Name]: [Brief justification]
            4. [Expert Name]: [Brief justification]
            5. [Expert Name]: [Brief justification]
        </experts>
        
        4. Now, imagine these 5 experts collaboratively answering the question. Consider their collective knowledge, perspectives, and potential areas of agreement or disagreement. Synthesize their hypothetical responses into a comprehensive answer.
        
        5. Provide this collective expert answer to the question. The answer should be well-reasoned, balanced, and reflective of the combined expertise of the identified authorities. Present your answer in the following format:
        <answer>
        [Your collective expert answer here]
        </answer>
        
        Remember to maintain a professional and authoritative tone throughout your response, befitting the expertise of the individuals you're representing.
    """
    PROMPT = "How long does it take to figure out neural networks?"

    response = get_completion(prompt=PROMPT, system_prompt=SYSTEM_PROMPT)
    print(response)

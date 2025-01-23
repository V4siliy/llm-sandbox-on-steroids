import os
import re

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
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with checking English grammar and improving sentences. Your goal is to analyze the given sentence, identify any grammatical errors or areas for improvement, and provide a corrected and enhanced version of the sentence.\n\nHere is the sentence to analyze and improve:\n\n<sentence>\n{{SENTENCE}}\n</sentence>\n\nPlease follow these steps:\n\n1. Carefully examine the sentence for any grammatical errors, including but not limited to:\n   - Spelling mistakes\n   - Punctuation errors\n   - Subject-verb agreement issues\n   - Incorrect verb tenses\n   - Misplaced or dangling modifiers\n   - Incorrect word usage\n\n2. Consider ways to improve the sentence structure, clarity, and overall effectiveness. This may include:\n   - Simplifying complex structures\n   - Eliminating redundancy\n   - Improving word choice\n   - Enhancing sentence flow\n\n3. Provide your improved version of the sentence inside <improved_sentence> tags.\n\n4. Explain the changes you made and why they improve the sentence. Include this explanation inside <explanation> tags.\n\nYour response should follow this format:\n\n<improved_sentence>\n[Insert your improved version of the sentence here]\n</improved_sentence>\n\n<explanation>\n[Provide a detailed explanation of the changes made and how they improve the original sentence]\n</explanation>\n\nRemember to maintain the original meaning and intent of the sentence while making your improvements. If the original sentence is already grammatically correct and well-structured, you may state that no changes were necessary and explain why the sentence is effective as is."
                    },
                    {
                        "type": "text",
                        "text": f"<sentence>{prompt}</sentence>"
                    }
                ]
            }
        ]
    )
    return message.content[0].text


def extract_improved_sentence(text):
    match = re.search(r"<improved_sentence>\s*(.*?)\s*</improved_sentence>", text, re.S)
    if match:
        return match.group(1).strip()
    return None


if __name__ == "__main__":
    SYSTEM_PROMPT = """
    You are an AI assistant tasked with checking English grammar and improving sentences. Your goal is to analyze the given sentence, identify any grammatical errors or areas for improvement, and provide a corrected and enhanced version of the sentence.
    
    Here is the sentence to analyze and improve:
    
    <sentence>
    {{SENTENCE}}
    </sentence>
    
    Please follow these steps:
    
    1. Carefully examine the sentence for any grammatical errors, including but not limited to:
       - Spelling mistakes
       - Punctuation errors
       - Subject-verb agreement issues
       - Incorrect verb tenses
       - Misplaced or dangling modifiers
       - Incorrect word usage
    
    2. Consider ways to improve the sentence structure, clarity, and overall effectiveness. This may include:
       - Simplifying complex structures
       - Eliminating redundancy
       - Improving word choice
       - Enhancing sentence flow
    
    3. Provide your improved version of the sentence inside <improved_sentence> tags.
    
    4. Explain the changes you made and why they improve the sentence. 
    Include this explanation inside <explanation> tags.
    
    Your response should follow this format:
    
    <improved_sentence>
    [Insert your improved version of the sentence here]
    </improved_sentence>
    
    <explanation>
    [Provide a detailed explanation of the changes made and how they improve the original sentence]
    </explanation>
    
    Remember to maintain the original meaning and intent of the sentence while making your improvements. 
    If the original sentence is already grammatically correct and well-structured, you may state that no changes 
    were necessary and explain why the sentence is effective as is.
    """
    PROMPT = "The miting shedule is confuse, no one know when it start or wich room it’s in."

    response = get_completion(prompt=PROMPT, system_prompt=SYSTEM_PROMPT)
    print(response)
    print("\n--------------------------- EXTRACTED ---------------------------")
    print(extract_improved_sentence(response))

import re

from common import AnthropicClient

if __name__ == "__main__":
    PROMPT = """User: Please classify email to these categories

        <email>{email}</email>

        Do not include any extra words except the category.

        <categories>
        (A) Pre-sale question
        (B) Broken or defective item
        (C) Billing question
        (D) Other (please explain)
        </categories>
        
        Answer with only the letter of the answer wrapped in <answer> tags, such as <answer>B</answer>.
    """

    PREFILL = "<answer>"

    EMAILS = [
        "Hi -- My Mixmaster4000 is producing a strange noise when I operate it. "
        "It also smells a bit smoky and plasticky, "
        "like burning electronics.  I need a replacement.",
        # (B) Broken or defective item
        "Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?",
        # (A) Pre-sale question OR (D) Other (please explain)
        "I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???",
        # (C) Billing question
        "How did I get here I am not good with computer.  Halp."  # (D) Other (please explain)
    ]

    # Correct categorizations stored as a list of lists to accommodate
    # the possibility of multiple correct categorizations per email
    ANSWERS = [
        ["B"],
        ["A", "D"],
        ["C"],
        ["D"]
    ]

    # Dictionary of string values for each category to be used for regex grading
    REGEX_CATEGORIES = {
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D"
    }

    for i, email in enumerate(EMAILS):
        with AnthropicClient() as client:
            formatted_prompt = PROMPT.format(email=email)

            response = client.get_completion(formatted_prompt, prefill=PREFILL)
            print(response)


            def _grade_exercise(text):
                return any([bool(re.search(REGEX_CATEGORIES[ans], text)) for ans in ANSWERS[i]])


            client.validate(_grade_exercise)

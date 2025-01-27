import re

from common import AnthropicClient


if __name__ == "__main__":

    QUESTION = "How long do I have to make an 83b election?"

    TASK_CONTEXT = """You are a master tax accountant. 
    Your task is to answer user questions using any provided reference documentation."""

    TONE_CONTEXT = None

    INPUT_DATA = """Review the tax code documentation provided below:
    <document>
    {document}
    </document>
    """

    with open('assets/exercise_9_1_document.txt', 'r') as f:
        INPUT_DATA = INPUT_DATA.format(document=f.read())

    EXAMPLES = """Here is an example of how to respond:
    <example>
    <question>
    What defines a "qualified" employee?
    </question>
    <answer>
    <quotes>For purposes of this subsection—
    (A)In general
    The term "qualified employee" means any individual who—
    (i)is not an excluded employee, and
    (ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>
    
    <answer>According to the provided documentation, a "qualified employee" is defined as an individual who:
    
    1. Is not an "excluded employee" as defined in the documentation.
    2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
    </example>
    """

    TASK_DESCRIPTION = """Here is the material you should use to answer the user's question: 
    <question>
        {question}
    </question>
    """
    TASK_DESCRIPTION = TASK_DESCRIPTION.format(question=QUESTION)

    IMMEDIATE_TASK = """Gather relevant quotes from the <document> that pertain to the user's question. 
    Include these quotes within <quotes></quotes> tags. 
    If no relevant quotes are found, write "No relevant quotes found" within the tags.
    """

    PRECOGNITION = None

    OUTPUT_FORMATTING = """Provide your answer to the user's question within <answer></answer> tags. 
    Your answer should be based on the information found in the quotes. 
    If you are not confident that the quotes support a clear answer, inform the user that you 
    do not have enough information to answer their question.
    """

    PREFILL = None

    PROMPT = ""

    if TASK_CONTEXT:
        PROMPT += f"""{TASK_CONTEXT}"""

    if TONE_CONTEXT:
        PROMPT += f"""\n\n{TONE_CONTEXT}"""

    if INPUT_DATA:
        PROMPT += f"""\n\n{INPUT_DATA}"""

    if EXAMPLES:
        PROMPT += f"""\n\n{EXAMPLES}"""

    if TASK_DESCRIPTION:
        PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

    if IMMEDIATE_TASK:
        PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

    if PRECOGNITION:
        PROMPT += f"""\n\n{PRECOGNITION}"""

    if OUTPUT_FORMATTING:
        PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

    print("--------------------------- Full prompt with variable substutions ---------------------------")
    print(PROMPT)
    print("\n------------------------------------- Claude's response -------------------------------------")

    with AnthropicClient() as client:
        response = client.get_completion(PROMPT, prefill=PREFILL)
        print(response)

        def _grade_exercise(text):
            return bool(re.search("<quotes>", text) and re.search("<answer>", text))

        client.validate(_grade_exercise)

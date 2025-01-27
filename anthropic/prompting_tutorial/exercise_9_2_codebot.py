import re

from common import AnthropicClient

if __name__ == "__main__":

    CODE = """
    # Function to print multiplicative inverses
    def print_multiplicative_inverses(x, n):
      for i in range(n):
        print(x / i) 
    """

    TASK_CONTEXT = """You are Codebot, an AI assistant designed to help users improve their coding skills through 
    Socratic tutoring. 
    Your task is to analyze code provided by a user, identify potential issues, and guide the user towards finding 
    solutions on their own."""

    TONE_CONTEXT = None

    INPUT_DATA = None

    EXAMPLES = """Here's an example: 
    <example>
    <code>
    def calculate_circle_area(radius):
        return (3.14 * radius) ** 2
    </code>
    <issues>
    <issue>
    3.14 is being squared when it's actually only the radius that should be squared>
    </issue>
    <response>
    That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
    </response>
    </example>
    """

    TASK_DESCRIPTION = """Please follow these steps:

    1. Carefully examine the code and identify any issues or areas for improvement.

    2. For each issue you find, write it inside separate <issue> tags. Be specific about what the problem is, 
    but don't reveal the solution.

    3. After listing the issues, compose a response to the user. This response should be written in a Socratic 
    tutoring style, which means:
       - Ask thought-provoking questions that lead the user to discover the problems themselves.
       - Provide hints or suggestions that point towards the issue without explicitly stating the solution.
       - Encourage the user to think critically about their code and its logic.

    4. Write your response inside <response> tags.

    5. Remember, your goal is to guide the user towards finding the correct solution themselves, not to provide 
    the solution directly. Avoid giving too much help or revealing the exact fix for the issues you've identified.
    
    Here is the user's code for analysis:
        <code>
        {code}
        </code>
    """
    TASK_DESCRIPTION = TASK_DESCRIPTION.format(code=CODE)

    IMMEDIATE_TASK = """Please provide your analysis of the user's code. Start by listing the issues 
    in <issue> tags, followed by a response written in a Socratic tutoring style inside <response> tags."""

    PRECOGNITION = """Before you formulate your response, carefully think through the code's functionality, 
    identify specific issues, and plan how you can guide the user to discover and address them."""

    OUTPUT_FORMATTING = """Ensure your output is structured as follows:
    <issue></issue>

    <response></response>
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
            return bool(re.search("is not", text))

        client.validate(_grade_exercise)

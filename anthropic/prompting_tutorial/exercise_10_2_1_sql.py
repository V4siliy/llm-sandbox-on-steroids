import re
from typing import Dict, Any, Callable

from common import AnthropicClient


system_prompt_tools_general_explanation = """You have access to a set of functions you can use 
to answer the user's question. 
This includes access to a sandboxed computing environment. 
You do NOT currently have the ability to inspect files or interact with external
resources, except by invoking the below functions.

You can invoke one or more functions by writing a "<function_calls>" block like the following as part of your
reply to the user:
<function_calls>
<invoke name="$FUNCTION_NAME">
<antml:parameter name="$PARAMETER_NAME">$PARAMETER_VALUE</parameter>
...
</invoke>
<nvoke name="$FUNCTION_NAME2">
...
</invoke>
</function_calls>

String and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that
spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular
expressions.

The output and/or any errors will appear in a subsequent "<function_results>" block, and remain there as part of
your reply to the user.
You may then continue composing the rest of your reply to the user, respond to any errors, or make further function
calls as appropriate.
If a "<function_results>" does NOT appear after your function calls, then they are likely malformatted and not
recognized as a call."""

db = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ],
    "products": [
        {"id": 1, "name": "Widget", "price": 9.99},
        {"id": 2, "name": "Gadget", "price": 14.99},
        {"id": 3, "name": "Doohickey", "price": 19.99}
    ]
}


def get_user(user_id):
    for user in db["users"]:
        if user["id"] == user_id:
            return user
    return None


def get_product(product_id):
    for product in db["products"]:
        if product["id"] == product_id:
            return product
    return None


def add_user(name, email):
    user_id = len(db["users"]) + 1
    user = {"id": user_id, "name": name, "email": email}
    db["users"].append(user)
    return user


def add_product(name, price):
    product_id = len(db["products"]) + 1
    product = {"id": product_id, "name": name, "price": price}
    db["products"].append(product)
    return product


system_prompt_tools_specific_tools_sql = """
Here are the functions available in yaml format:

tools:
  - tool_description:
      tool_name: get_user
      description: Retrieves a user from the database by their user ID.
      parameters:
        - name: user_id
          type: int
          description: The ID of the user to retrieve.

  - tool_description:
      tool_name: get_product
      description: Retrieves a product from the database by its product ID.
      parameters:
        - name: product_id
          type: int
          description: The ID of the product to retrieve.

  - tool_description:
      tool_name: add_user
      description: Adds a new user to the database.
      parameters:
        - name: name
          type: str
          description: The name of the user.
        - name: email
          type: str
          description: The email address of the user.

  - tool_description:
      tool_name: add_product
      description: Adds a new product to the database.
      parameters:
        - name: name
          type: str
          description: The name of the product.
        - name: price
          type: float
          description: The price of the product.

"""

SYSTEM_PROMPT = system_prompt_tools_general_explanation + system_prompt_tools_specific_tools_sql

STOP_SEQUENCES = ["</function_calls>"]

PREFILL = "<"

EXAMPLES = [
    "Add a user to the database named Deborah.",
    "Add a product to the database named Thingo",
    "Tell me the name of User 2",
    "Tell me the name of Product 3"
]

expected_results = [
    "add_user:Deborah",
    "add_product:Thingo",
    "get_user:2",
    "get_product:3"
]


def extract_function_info(response: str) -> tuple[str, Dict[str, Any]]:
    function_name_match = re.search(r'<invoke name="([^"]+)"', response)
    parameter_matches = re.findall(r'<parameter name="([^"]+)">([^<]+)</parameter>', response)

    if not function_name_match:
        raise ValueError("Function name not found in the response")

    function_name = function_name_match.group(1)
    parameters = {name: value for name, value in parameter_matches}

    return function_name, parameters


def parse_parameter(value: str, param_type: type) -> Any:
    if param_type == int:
        return int(value)
    elif param_type == float:
        return float(value)
    return value


def call_function_from_response(response: str) -> None:
    function_map: Dict[str, Callable] = {
        "get_product": get_product,
        "get_user": get_user,
        "add_user": add_user,
        "add_product": add_product
    }

    param_types: Dict[str, Dict[str, type]] = {
        "get_product": {"product_id": int},
        "get_user": {"user_id": int},
        "add_user": {"name": str, "email": str},
        "add_product": {"name": str, "price": float}
    }

    try:
        function_name, raw_parameters = extract_function_info(response)

        if function_name not in function_map:
            raise ValueError(f"Function {function_name} not recognized")

        function = function_map[function_name]
        expected_params = param_types[function_name]

        parsed_parameters = {}
        for param_name, param_type in expected_params.items():
            if param_name not in raw_parameters:
                raise ValueError(f"Required parameter '{param_name}' not provided for {function_name}")
            parsed_parameters[param_name] = parse_parameter(raw_parameters[param_name], param_type)

        result = function(**parsed_parameters)
        print(f"{function_name.capitalize()} result: {result}")

    except (ValueError, KeyError, TypeError) as e:
        print(f"Error: {str(e)}")


for i, example in enumerate(EXAMPLES):

    with AnthropicClient() as client:
        response = client.get_completion(example,
                                         system_prompt=SYSTEM_PROMPT,
                                         prefill=PREFILL,
                                         stop_sequences=STOP_SEQUENCES
                                         )

        def _grade_exercise(text):
            func_name, param = expected_results[i].split(':')
            return func_name in text and param in text

        client.validate(_grade_exercise)

        call_function_from_response(f'<{response}')

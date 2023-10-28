# Test 3

"""
Create a function that takes a string and returns the string in “proper” case, 
i.e. starting with a capital letter and ending with a full stop 
"""

# Solution

def proper_case(input_str: str)-> str:
    """
    Args:
    input_str (str): The input string.

    Returns:
    str: The string in "proper" case.
    """
   
    result = input_str.capitalize()  # Capitalize the first letter
    if not result.endswith('.'):
        result += '.'  # Add a full stop at the end

    return result

# test 1
print(proper_case("rajini"))

# test 2
print(proper_case("tom"))
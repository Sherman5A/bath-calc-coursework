"""SRPN calculator"""
# This is your SRPN file. Make your changes here.

# Imports
# Regex library is used for removing, replacing text
import re


# if input_command == '=':
#     return 0
# else:
#     return 0


class SrpnStack:

    def __init__(self, stack_contents: list, stack_counter=0):
        self.stack_contents = stack_contents
        self.stack_counter = stack_counter

    def push_stack(self, push_value: str, index=None):
        """Pushes to SRPN stack, optional value for index"""
        try:
            push_value = int(push_value)
            self.stack_counter += 1
        except ValueError:
            pass
        if index is None:
            self.stack_contents.append(push_value)
            return
        self.stack_contents.insert(index, push_value)

    def pop_stack(self, index=None):
        """Remove and then return the stacks first value. If given index,
        removes and returns that index."""
        if index is None:
            return self.stack_contents.pop(-1)
        return self.stack_contents.pop(index)

    def cool_maths(self):
        operator_function_dispatch = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "%": lambda x, y: x % y,
            "^": lambda x, y: x ** y,
        }


def handle_srpn_command(validated_string: str, srpn_stack: list) -> list:

    print(srpn_stack)
    for count, element in enumerate(validated_string):
        if operator_function_dispatch.get(element, False):
            temp_stack = [srpn_stack.pop(count - 1), srpn_stack.pop(count - 2)]
            print(temp_stack)
            print(srpn_stack)
        else:
            srpn_stack.append(element)
            return srpn_stack


def validate_input(usr_input: str) -> str:
    """Sanitises, removes comments, unnecessary characters inputs"""

    # Regex command does the following:
    # # finds a hashtag
    # () - gets all characters between the hashtags
    # .* - selects all text between the hashtags
    # ? - prevents regex from selecting text between two comments
    usr_input = re.sub("#(.*?)#|#", "", usr_input)

    # Regex explanation:
    # \s removes whitespace
    # [] removes characters
    # ^rd prevents the removal of the characters 'r', and 'd'
    usr_input = re.sub("\s[^rd]|", "", usr_input)

    return usr_input

# This is the entry point for the program.
# It is suggested that you do not edit the below,
# to ensure your code runs with the marking script
if __name__ == "__main__":
    srpn_stack = []
    while True:
        try:
            input_string = input()
            validated_string = validate_input(input_string)
            srpn_stack = handle_srpn_command(validated_string, srpn_stack)
        except EOFError:
            exit()

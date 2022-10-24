"""SRPN calculator"""
# This is your SRPN file. Make your changes here.

# Imports
# Regex library is used for removing, replacing text
import re


class SrpnStack:

    def __init__(self):
        self.stack_contents = []
        # Stack counter keeps track of the number of operands in stack
        # Prevents using an operator with only one operand.
        self.stack_counter = 0
        self.stack_history = []

    def push_stack(self, push_value: int, push_to_history=True):
        """Pushes to SRPN stack, optional argument for pushing to history"""

        self.stack_counter += 1
        self.stack_contents.append(push_value)
        if push_to_history:
            self.push_history(push_value)
            print("Stack History {}".format(self.stack_history))

    def push_history(self, push_value):
        """Push to the stack history"""
        self.stack_history.append(push_value)

    def operator_push_stack(self, operator_command: str):
        """Perform a maths operator on the stack"""

        if self.stack_counter < 2:
            print("Not enough operands in stack")
            return
        operand_stack = [self.pop_stack(1), self.pop_stack()]
        # Pop last two elements off stack and place into temporary stack
        # Do maths and push result
        self.push_stack(self.execute_maths(operand_stack, operator_command),
                        push_to_history=False)
        self.push_history(operator_command)

    def pop_stack(self, index=0):
        """Remove and then return the stacks first value. If given index,
        removes and returns that index."""

        self.stack_counter -= 1
        if index == 0:
            return self.stack_contents.pop(-1)
        return self.stack_contents.pop(- index - 1)

    def execute_maths(self, stack, input_operator):
        """Maps maths to inline functions, ensures input is between min, max
           limits"""
        operator_function_dispatch = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "%": lambda x, y: x % y,
            "^": lambda x, y: x ** y,
        }
        return int(
            operator_function_dispatch[input_operator](stack[-2], stack[-1]))


def handle_srpn_command(sanitised_string: str, srpn_stack):
    """Takes the command and executes the relevant SRPN class function"""

    srpn_command = re.findall("\d+|\W", sanitised_string)
    print(srpn_command)
    # Regex used as it allows for inputs on both single and multiline inputs
    # Regex explanation:
    # -? - matches "-" zero or more times, matching both negative and positive
    # numbers
    # \d - finds digits
    # + - finds more than one digit character in number
    # | - is an or statement
    # \S - finds non-words whitespace characters, such as r and
    # Combination of this with findall splits the string into a list of srpn
    # operators

    for element in srpn_command:
        try:
            # Check if input is integer
            element = int(element)
            srpn_stack.push_stack(element)
        except ValueError:
            if element == "d":
                pass
            elif element == "f":
                pass
            elif element in "+*-/^%":
                srpn_stack.operator_push_stack(element)


def validate_input(usr_input: str) -> str:
    """Sanitises, removes comments, unnecessary characters inputs"""

    usr_input = re.sub("#(.*?)#|#", "", usr_input)
    # Regex command does the following:
    # '#' - finds a hashtag
    # () - groups the characters inside it
    # .* - selects all text between the hashtags
    # ? - prevents regex from selecting text between two comments
    # | - or operator
    # # - removes single hashtags

    usr_input = re.sub("\s[^rd]|", "", usr_input)
    # Regex explanation:
    # \s removes whitespace
    # [] removes characters
    # ^rd prevents the removal of the characters 'r', and 'd'

    return usr_input


# This is the entry point for the program.
# It is suggested that you do not edit the below,
# to ensure your code runs with the marking script
if __name__ == "__main__":
    srpn_stack = SrpnStack([])
    while True:
        try:
            input_string = input()
            validated_string = validate_input(input_string)
            handle_srpn_command(validated_string, srpn_stack)
        except EOFError:
            exit()

"""SRPN calculator"""
# This is your SRPN file. Make your changes here.

# Imports
# Regex library is used for removing, replacing text
import re


def process_command(command):
    if command == '=':
        return 0
    else:
        return 0


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


def input_validation_2(calc_input):
    print(calc_input.split("#"))

# This is the entry point for the program.
# It is suggested that you do not edit the below,
# to ensure your code runs with the marking script
# if __name__ == "__main__":
#   while True:
#     try:
#       cmd = input()
#       pc = process_command(cmd)
#     except EOFError:
#       exit()

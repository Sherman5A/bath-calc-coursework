# This is your SRPN file. Make your changes here.

def process_command(command):
    if command == '=':
        return 0
    else:
        return 0


def validate_input(calc_input: str) -> str:
    """Sanitises, checks for problematic inputs"""

    calc_input = calc_input.replace(" ", "")  # Removing all spaces as unnecessary


def remove_comments(calc_input: str) -> str:
    """Removes comments denoted by '#' from the input"""
    # I wish regex was allowed.

    comments_exist = True

    # Ensures that lines with multiple comments are caught
    while comments_exist:

        comment_delimiter = calc_input.find("#")
        # Terminating condition
        if comment_delimiter == -1:
            comments_exist = False
            break

        # Remove the first '#' and everything preceding it, and find the
        # second '#'
        comment_delimiter_2 = (
                calc_input[comment_delimiter + 1:].find("#") + comment_delimiter + 1)

        calc_input = calc_input[:comment_delimiter] + calc_input[comment_delimiter_2 + 1:]
        # Removes the delimiting hashtags and everything between them. Gets
        # slice before first hashtag and concatenates to slice after second
        # hashtag If 2nd '#' not present, first '#' is removed and rest of
        # string is kept.

    return calc_input


def input_validation_2(calc_input):
    print(calc_input.split("#"))


print(remove_comments("fsfhadsfadkl #dafadsf fasfasfdsfdas"))


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

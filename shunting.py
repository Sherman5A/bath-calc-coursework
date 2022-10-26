"""Takes basic infix notation and converts it to a list made for a reverse
   polish notation calculator"""

def shunting_algorithm(usr_input: list) -> list:
    """Creates reverse polish notation from an infix list"""
    # Order of operators for ODMAS.
    operator_precedence = {
        "^": 4,
        "%": 3,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
    }
    output_queue = []
    operator_stack = []

    unary_negative = False
    for i in usr_input:

        if i == " ":  # Ignore spaces
            continue

        if i.isdigit():
            # If unary flag is set, make number negative.
            if unary_negative:
                output_queue.append("-" + i)
                # Reset flag to ensure that the next numbers are not negative.
                unary_negative = False
                continue
            output_queue.append(i)

        else:
            if i == "-":
                unary_negative = unary_check(unary_negative, operator_stack,
                                             output_queue)
                if not unary_negative:
                    # Add operator to stack if binary operator
                    operator_stack.append(i)
                continue

            for _ in operator_stack:
                # If the precedence of the operator is lower or equal to i,
                # then pop the stack.
                if operator_precedence[i] <= operator_precedence[
                        operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                    continue
                break

            operator_stack.append(i)

    # Once all input is processed append any operators left.
    for i in reversed(operator_stack):
        output_queue.append(i)
    return output_queue


def unary_check(unary_flag: bool, operator_stack: list,
                output_queue: list) -> bool:
    """Performs checks to see if unary flag needs to be set to true."""
    if not unary_flag:
        return double_negative(operator_stack) or left_associate(output_queue)
    return False


def double_negative(operator_stack: list) -> bool:
    """If there is a previous operator, set the unary flag to true."""
    try:
        return operator_stack[-1] in "+*/%^1-"
    except IndexError:  # If stack empty.
        return False


def left_associate(output_queue: list) -> bool:
    """Check that a number exists before the minus sign. If so, return true
       to set flag for unary negative."""
    try:
        return not output_queue[-1].isdigit()
    except IndexError:  # If the stack is empty.
        return True

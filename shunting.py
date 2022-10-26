import re


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
    if unary_flag is False:
        set_unary_flag = double_negative(operator_stack) or left_associate(
            output_queue)
        if set_unary_flag:
            return True
    else:
        return False


def double_negative(operator_stack: list) -> bool:
    """If there is a previous operator, set the unary flag to true."""
    try:
        is_double_negative = operator_stack[-1] in "+*/%^-"
        if is_double_negative is True:
            return True
        return False
    except IndexError:  # If stack empty.
        return False


def left_associate(output_queue: list) -> bool:
    """Check that a number exists before the minus sign. If so, return true
       to set flag for unary negative."""
    try:
        number_before_minus = output_queue[-1].isdigit()
        if number_before_minus is False:
            return True
        return False
    except IndexError:  # If the stack is empty.
        return True

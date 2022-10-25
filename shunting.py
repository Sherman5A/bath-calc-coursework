import re


def shunting_algorithm(usr_input):
    # Order of operators for BODMAS
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

        if i == " ":
            continue

        if i.isdigit():
            # If unary flag is set, make number negative
            if unary_negative:
                output_queue.append("-" + i)
                # Reset flag to ensure that all numbers are not negative
                unary_negative = False
                continue
            output_queue.append(i)

        else:
            if i == "-":
                unary_negative = unary_check(unary_negative, operator_stack,
                                             output_queue)
                continue

            for _ in operator_stack:
                if operator_precedence[i] <= operator_precedence[
                        operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                    continue
                break

            operator_stack.append(i)

    for i in reversed(operator_stack):
        output_queue.append(i)
    return output_queue


def unary_check(unary_flag, operator_stack, output_queue):
    if unary_flag is False:
        set_unary_flag = double_negative(operator_stack) or left_associate(
            output_queue)
        if set_unary_flag:
            return True

    else:
        return False


def double_negative(operator_stack):
    try:
        is_double_negative = operator_stack[-1] in "+*/%^-"
        if is_double_negative is True:
            return True
        return False
    except IndexError:
        return False


def left_associate(output_queue):
    try:
        left_associate = output_queue[-1].isdigit()
        if left_associate is False:
            return True
        return False
    except IndexError:
        return True

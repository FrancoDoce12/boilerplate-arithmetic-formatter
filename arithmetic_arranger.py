def arithmetic_arranger(problems: list, show_answer: bool = False):

    # each of this list inside for_print represent a line to print ignoring the (fourth line)

    for_print = [[], [], []]

    # problems and errors handling

    if problems.__len__() >= 6:
        return error_return("Error: Too many problems.")

    for arithmetic_problem in problems:
        if type(arithmetic_problem) != str:
            return error_return()

        arithmetic_problem_separate = arithmetic_problem.split()

        if arithmetic_problem_separate.__len__() != 3:
            return error_return()

        if not ((arithmetic_problem_separate[1] == "+") or (arithmetic_problem_separate[1] == "-")):
            return error_return("Error: Operator must be '+' or '-'.")

        if not (arithmetic_problem_separate[0].isdigit() and arithmetic_problem_separate[2].isdigit()):
            return error_return("Error: Numbers must only contain digits.")

        if arithmetic_problem_separate[0].__len__() > 4 or arithmetic_problem_separate[2].__len__() > 4:
            return error_return("Error: Numbers cannot be more than four digits.")

        # ------------ transformation handled -----------

        for number in range(0, 3):
            for_print[number].append(arithmetic_problem_separate[number])

    line_one_to_print = ""
    line_two_to_print = ""
    line_tree_to_print = ""
    line_four_to_print = ""

    for arithmetic_operation in range(problems.__len__()):

        first_number = for_print[0][arithmetic_operation]
        operator_ = for_print[1][arithmetic_operation]
        second_number = for_print[2][arithmetic_operation]

        # finding the max number
        # it is in the top because it's needed for ordering the lines

        if first_number.__len__() >= second_number.__len__():
            max_number = first_number.__len__()
        else:
            max_number = second_number.__len__()

        # calculating some other variables that where be needed to calculate the lines

        total_spaces = max_number + 2

        result = sum_or_rest(first_number, operator_, second_number)

        # starting witch the first line (first the spaces and then the number)

        for number in range(total_spaces - first_number.__len__()):
            line_one_to_print = line_one_to_print.__add__(" ")

        line_one_to_print = line_one_to_print.__add__(f"{first_number}")

        # line two

        line_two_to_print = line_two_to_print.__add__(operator_)
        for number in range(total_spaces - 1 - second_number.__len__()):
            line_two_to_print = line_two_to_print.__add__(" ")
        line_two_to_print = line_two_to_print.__add__(second_number)

        # line three

        for number in range(total_spaces):
            line_tree_to_print = line_tree_to_print.__add__("-")

        # line four

        for number in range(total_spaces - result.__len__()):
            line_four_to_print = line_four_to_print.__add__(" ")
        line_four_to_print = line_four_to_print.__add__(result)

        # separating the operations between them (adding to all of them 4 spaces, that can be done witch a for loop
        # but that is a little in-necessary because that are just 4 lines and the side don't change dynamically
        # either are them in a list or inside something iterable)

        if (arithmetic_operation + 1) == (problems.__len__()):
            spaces = ""
        else:
            spaces = "    "

        line_one_to_print = line_one_to_print.__add__(spaces)
        line_two_to_print = line_two_to_print.__add__(spaces)
        line_tree_to_print = line_tree_to_print.__add__(spaces)
        line_four_to_print = line_four_to_print.__add__(spaces)

    # printing the final result after that for loop

    if show_answer:
        result = f"{line_one_to_print}\n{line_two_to_print}\n{line_tree_to_print}\n{line_four_to_print}"
    else:
        result = f"{line_one_to_print}\n{line_two_to_print}\n{line_tree_to_print}"

    print(result)
    return result


def error_return(error: str = "Error: Wrong format"):
    print(error)
    return error


def sum_or_rest(first_number: str, operator: str, second_number: str):
    if operator == "-":
        return str((int(first_number) - int(second_number)))
    else:
        return str((int(first_number) + int(second_number)))

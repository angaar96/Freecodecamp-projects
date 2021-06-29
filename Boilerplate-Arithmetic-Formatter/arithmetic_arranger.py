import re
def arithmetic_arranger(problems, isTrue = False):
    sum_value = ""
    sum_values = []
    first_values = []
    second_values = []
    line_lengths = []
    operator_values = []
    regex1 = '[^0-9]+'
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        problem_array = problem.split(" ")
        if problem_array[1] == "/" or problem_array[1] == "*":
            return "Error: Operator must be '+' or '-'."
        elif re.search(regex1, problem_array[0]) != None:
            return "Error: Numbers must only contain digits."
        elif re.search(regex1, problem_array[2]) != None:
            return "Error: Numbers must only contain digits."
        elif len(problem_array[0])>4 or len(problem_array[2])> 4:
            return "Error: Numbers cannot be more than four digits."
        if problem_array[1] == "+":
            sum_value = int((problem_array[0])) + int(problem_array[2])
            sum_values.append(sum_value)
            first_values.append(problem_array[0])
            second_values.append(problem_array[2])
        elif problem_array[1] == "-":
            sum_value = int(problem_array[0]) - int(problem_array[2])
            sum_values.append(sum_value)
            first_values.append(problem_array[0])
            second_values.append(problem_array[2])
        length_array = [problem_array[0], problem_array[2]]
        if len(length_array[0]) != len(length_array[1]):
            max_number = max(length_array, key=len)
            line_length = len(max_number) + 2
            line_lengths.append(line_length)
        else:
            max_number = len(length_array[0])
            line_length = max_number + 2
            line_lengths.append(line_length)
        operator_value = problem_array[1]
        operator_values.append(operator_value)
    if not isTrue and len(problems) == 5:
        line1 = first_values[0].rjust(line_lengths[0]) + "    " + first_values[1].rjust(line_lengths[1]) + "    " \
                + first_values[2].rjust(line_lengths[2]) + "    " + first_values[3].rjust(line_lengths[3]) + "    " + \
                first_values[4].rjust(line_lengths[4])
        line2 = operator_values[0].ljust(0) + second_values[0].rjust(line_lengths[0]-1) + "    " \
                + operator_values[1].ljust(0)+ second_values[1].rjust(line_lengths[1]-1) + "    " \
                + operator_values[2].ljust(0) + second_values[2].rjust(line_lengths[2]-1) + "    " \
                 + operator_values[3].ljust(0) \
                + second_values[3].rjust(line_lengths[3]-1) + "    " + operator_values[4].ljust(0) + second_values[4].rjust(line_lengths[4]-1)
        line3 = "-"*line_lengths[0] + "    " + "-"*line_lengths[1] + "    " + "-"*line_lengths[2] + "    " + "-"*line_lengths[3] + "    " + "-"*line_lengths[4]
        print(line1 + "\n" + line2 + "\n" + line3)
        return line1 + "\n" + line2 + "\n" + line3
    elif isTrue and len(problems) == 4:
        line1 = first_values[0].rjust(line_lengths[0]) + "    " + first_values[1].rjust(line_lengths[1]) + "    " + first_values[2].rjust(line_lengths[2]) + "    " + first_values[3].rjust(line_lengths[3])
        line2 = operator_values[0].ljust(0) + second_values[0].rjust(line_lengths[0] - 1) + "    " + operator_values[
            1].ljust(0) + second_values[1].rjust(line_lengths[1] - 1) + "    " + operator_values[2].ljust(0) + second_values[2].rjust(line_lengths[2] - 1) + "    " + operator_values[3].ljust(0) + second_values[3].rjust(line_lengths[3] - 1)
        line3 = "-"*line_lengths[0] + "    " + "-"*line_lengths[1] + "    " + "-"*line_lengths[2] + "    " + "-"*line_lengths[3]
        sum_values_str = []
        for i in sum_values:
            sum_values_str.append(str(i))
        line4 = sum_values_str[0].rjust(line_lengths[0]) + "    " + sum_values_str[1].rjust(line_lengths[1]) + "    " + sum_values_str[2].rjust(line_lengths[2]) + "    " + sum_values_str[3].rjust(line_lengths[3])
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    elif not isTrue:
        line1 = first_values[0].rjust(line_lengths[0]) + "    " + first_values[1].rjust(line_lengths[1]) + "    " + \
                first_values[2].rjust(line_lengths[2]) + "    " + first_values[3].rjust(line_lengths[3])
        line2 = operator_values[0].ljust(0) + second_values[0].rjust(line_lengths[0] - 1) + "    " + operator_values[
            1].ljust(0) + second_values[1].rjust(line_lengths[1] - 1) + "    " + operator_values[2].ljust(0) + \
                second_values[2].rjust(line_lengths[2] - 1) + "    " + operator_values[3].ljust(0) + second_values[
                    3].rjust(line_lengths[3] - 1)
        line3 = "-" * line_lengths[0] + "    " + "-" * line_lengths[1] + "    " + "-" * line_lengths[2] + "    " + "-" * \
                line_lengths[3]
        print(line1 + "\n" + line2 + "\n" + line3)
        return line1 + "\n" + line2 + "\n" + line3

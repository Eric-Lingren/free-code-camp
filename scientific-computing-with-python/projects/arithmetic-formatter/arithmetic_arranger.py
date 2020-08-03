
def arithmetic_arranger(problems):
    error = None
   
    for problem in problems:
        valid_problem_opperator = check_problem_opperators(problem)
        if valid_problem_opperator is False:
            error = "Error: Operator must be '+' or '-'."
            break
        valid_problem_integer = check_opperand_integers(problem)
        if valid_problem_integer is False:
            error = "Error: Numbers must only contain digits."
            break
        valid_opperand_length = check_opperand_length(problem)
        if valid_opperand_length is False:
            error = "Error: Numbers cannot be more than four digits."
            break

    valid_problem_quantity = check_problem_quantity(problems)
    if valid_problem_quantity is False:
        error = 'Error: Too many problems.'

    arranged_problems = ''

    if error is not None:
        return error
    if error is None:
        problem_spacing = 4
        line1 = ''
        line2 = ''
        line3 = ''
        for problem in problems:
            line1 = ( line1 + build_print_output_line_1(problem) + (' ' * problem_spacing) )
            line2 = ( line2 + build_print_output_line_2(problem) + (' ' * problem_spacing) )
            line3 = ( line3 + build_print_output_line_3(problem) + (' ' * problem_spacing) )

        arranged_problems = line1 + '\n' + line2 + '\n'+ line3  
        return arranged_problems 

        
def check_problem_quantity(problems):
    problem_length = len(problems)
    if problem_length <= 4:
        return True
    else:
        return False


def get_opperator(problem):
    opperator_index = problem.find(' ')+1
    opperator = problem[opperator_index]
    return opperator


def check_problem_opperators(problem):
    opperator = get_opperator(problem)
    if opperator != '-' and opperator != '+':
        return False


def get_opperands(problem):
    operand1_end_index = problem.find(' ')
    operand2_start_index = int(operand1_end_index)+3
    opperand1 = problem[0:operand1_end_index]
    opperand2 = problem[operand2_start_index:]
    return opperand1, opperand2


def check_opperand_integers(problem):
    opperands = get_opperands(problem)
    try:
        int(opperands[0])
    except:
        return False
    try:
        int(opperands[1])
    except:
        return False


def check_opperand_length(problem):
    opperands = get_opperands(problem)
    if len(opperands[0]) > 4:
        return False
    if len(opperands[1]) > 4:
        return False


def build_print_output_line_1(problem):
    opperands = get_opperands(problem)
    opperand0 = opperands[0]
    opperand1 = opperands[1]
    max_size = longest_opperand(opperand0, opperand1)+2
    line1 = inject_line1_whitespace(max_size, opperand0)
    return line1


def build_print_output_line_2(problem):
    opperator = get_opperator(problem)
    opperands = get_opperands(problem)
    opperand0 = opperands[0]
    opperand1 = opperands[1]
    max_size = longest_opperand(opperand0, opperand1)+2
    line2 = inject_line2_whitespace(max_size, opperand1, opperator)
    return line2


def build_print_output_line_3(problem):
    opperands = get_opperands(problem)
    opperand0 = opperands[0]
    opperand1 = opperands[1]
    max_size = longest_opperand(opperand0, opperand1) + 2
    sumline = '-' * max_size
    return sumline


def longest_opperand(opperand0, opperand1):
    if len(opperand0) > len(opperand1):
        return len(opperand0)
    else:
        return len(opperand1)


def inject_line1_whitespace(max_size, opperand):
    difference = max_size - len(opperand)
    spaces = ' ' * difference
    return spaces + opperand


def inject_line2_whitespace(max_size, opperand, opperator):
    difference = max_size - 1 - len(opperand)
    spaces = ' ' * difference
    return opperator + spaces + opperand
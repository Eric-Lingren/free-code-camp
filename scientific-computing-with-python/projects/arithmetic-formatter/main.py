# This entrypoint file to be used in development. Start by reading README.md
# from arithmetic_arranger import arithmetic_arranger
from unittest import main

test_data = ["32 + 698", "3801 - 2", "455 + 43", "123 - 349"]

def check_problem_quantity(problems):
    problem_length = len(test_data)
    if problem_length <= 4:
        return True
    else:
        return False

def check_problem_opperators(problem):
    opperator_index = problem.find(' ')+1
    opperator = problem[opperator_index]
    if opperator != '-' and opperator != '+':
        return False

def check_opperand_integers(problem):
    operand1_end_index = problem.find(' ')
    operand2_start_index = int(operand1_end_index)+3
    opperand1 = problem[0:operand1_end_index]
    opperand2 = problem[operand2_start_index:]
    try:
        int(opperand1)
    except:
        return False
    try:
        int(opperand2)
    except:
        return False

def check_opperand_length(problem):
    operand1_end_index = problem.find(' ')
    operand2_start_index = int(operand1_end_index)+3
    opperand1 = problem[0:operand1_end_index]
    opperand2 = problem[operand2_start_index:]

    if len(opperand1) > 4:
        return False
    if len(opperand2) > 4:
        return False





def arithmetic_arranger(test_data):
    error = None

    for problem in test_data:
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

    valid_problem_quantity = check_problem_quantity(test_data)
    if valid_problem_quantity is False:
        error = 'Error: Too many problems.'

    
    if error is not None:
        print(error)
    if error is None:
        print('data good mate, carry on')

    return test_data

print(arithmetic_arranger(test_data))



# Run unit tests automatically
# main(module='test_module', exit=False)
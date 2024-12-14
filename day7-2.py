#!/usr/bin/env python3
from pprint import pprint
import itertools

filename = 'day7-input.txt'
rawdata = open(filename, 'r').read()

equations: dict = {}
operators: list = ['+', '*', "|"]

for line in rawdata.split('\n'):
    key = int(line.split(':')[0])
    value = [str(x) for x in line.split(":")[1].split(" ")[1:]]
    if key not in equations.keys():
        equations[key] = value
    else:
        print("Duplicate number!")

def operator_permutations(numbers, these_operators):
    result = []
    n = len(numbers) - 1
    """Generates all binary permutations of length n."""
    iterations = [seq for seq in itertools.product(''.join(these_operators), repeat=n)]
    for iteration in iterations:
        # print("iteration: {}, numbers: {}".format(iteration,numbers))
        result += [[x for x in itertools.chain(*itertools.zip_longest(numbers, iteration)) if x is not None]]

    return result

def do_the_math(expression):
    result = int(expression[0])
    for i in range(1, len(expression)-1, 2):
        operator = expression[i]
        number = expression[i+1]
        if operator == '+':
            result += int(number)
        elif operator == '*':
            result *= int(number)
        elif operator == '|':
            result = int(str(result) + str(number))

    return result


def valid_solution_exists(targetnum, numlist):
    global operators

    permutations = operator_permutations(numlist, operators)
    result = False

    for test in permutations:
        math_result = do_the_math(test)
        if math_result == targetnum:
            print(" ------------> Found solve for {} -> {}".format(targetnum, test))
            result = True
            break

    return result

aggregate = 0
for item in equations.keys():
    target = int(item)
    numbers = equations[item]
    if valid_solution_exists(target, numbers):
        aggregate += target

print("Result: {}".format(aggregate))

# print(valid_solution_exists(test_target_number, test_numbers))

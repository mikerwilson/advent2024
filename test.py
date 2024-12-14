import itertools
from pprint import pprint

from day7 import test_target_number

operators = ["+","*"]
# test_numbers = ['11', '6', '16', '20']
# test_target_number = 292
test_numbers = ['15', '6']
test_target_number = 156

def _generate_operator_permutations(numbers, these_operators):
    result = []

    n = len(numbers) - 1
    """Generates all binary permutations of length n."""
    iterations = [seq for seq in itertools.product(''.join(these_operators), repeat=n)]
    for iteration in iterations:
        # print("iteration: {}, numbers: {}".format(iteration,numbers))
        result += [[x for x in itertools.chain(*itertools.zip_longest(numbers, iteration)) if x is not None]]

    # print("operation permutations results: {}".format(result))
    return result

def operator_permutations(numbers, these_operators):
    result = []
    ag_numbers = []

    for item in _generate_operator_permutations(numbers, these_operators):
        result += [item]

    for i in range(1, len(numbers)-1):
        ag_numbers += [(numbers[:i] + [''.join(numbers[i:i+2])] + numbers[i+2:])]

    for ag_item in ag_numbers:
        for item in _generate_operator_permutations(ag_item, these_operators):
            result += [item]

    return result


def do_the_math(expression):
    result = int(expression[0])
    # pprint("do_the_math: {}".format(expression))
    for i in range(1, len(expression)-1, 2):
        operator = expression[i]
        number = expression[i+1]
        to_exec = "%s %s %s" % (result, operator, number)
        # print("Vars -> result: {}, operator: {}, number: {}".format(result, operator, number))
        # pprint(" --> About to execute: '{}'".format(to_exec))
        runresult = eval(to_exec)
        # pprint(" ---> Result: {}, type: {}".format(runresult,type(runresult)))
        result = runresult

    return result

# Example usage:

def valid_solution_exists(targetnum, numlist):
    global operators

    permutations = operator_permutations(numlist, operators)
    # pprint(permutations, width= 200)
    result = False

    for test in permutations:
        # pprint("Test: {}".format(test))
        math_result = do_the_math(test)
        # pprint("{} -> Equation: {}".format(result, test))
        if math_result == targetnum:
            print(" ------------> Found solve for {} -> {}".format(targetnum, test))
            result = True
            break

    return result


print(valid_solution_exists(test_target_number, test_numbers))

    # print("Result: %s, Attempt: %s" % (result, equation))


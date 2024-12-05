#!/usr/bin/env python3
from pprint import pprint

filename = 'day2-input.txt'
rawdata = open(filename, 'r').read()
reportcount: int = 0
safechanges: list = [1,2,3]
safecount: int = 0

def is_list_safe(a):
    # check all ascending or all descending
    if (not all(a[i] < a[i + 1] for i in range(len(a) - 1)) and
            not all(a[i] > a[i + 1] for i in range(len(a) - 1))):
        return False

    for i in range(len(a) - 1):
        if not abs(a[i] - a[i + 1]) in safechanges: return False

    return True

for line in rawdata.split("\n"):
    rawreports = line.split(' ')
    iod = None # i = inc, d = dec
    reports = list(map(int, rawreports)) # convert list into ints
    # pprint(reports)
    reportcount += 1

    if is_list_safe(reports):
        safecount += 1
        continue

    # try iterating
    print("Report unsafe: %s, iterating..." % reports)
    found_safe_option = False
    for j in range(len(reports)):
        try_list = reports.copy()
        del try_list[j]
        print(" -> Trying removing element %s ::: %s" % (j,try_list))
        if is_list_safe(try_list):
            print(" -----> List %s saved with %s!" % (reports, try_list))
            found_safe_option = True
            safecount += 1
            break

    if not found_safe_option:
        print(" **** No safe option found for list: %s. Giving up." % reports)

print("\nTotal reports: %s, Safecount: %s" % (reportcount, safecount))




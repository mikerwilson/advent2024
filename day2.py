#!/usr/bin/env python3
from pprint import pprint

filename = 'day2-input.txt'
rawdata = open(filename, 'r').read()

safechanges: list = [1,2,3]
safecount: int = 0
reportcount: int = 0

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

print("\nTotal reports: %s, Safecount: %s" % (reportcount, safecount))


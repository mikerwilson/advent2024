#!/usr/bin/env python3
import re

filename = 'day3-input.txt'
rawdata = open(filename, 'r').read()

matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", rawdata)

result = 0

for match in matches:
    [a,b] = match.split(',')
    a = int(a.split("(")[1])
    b = int(b.split(")")[0])

    result += a * b
    # print(a,b)

print(result)
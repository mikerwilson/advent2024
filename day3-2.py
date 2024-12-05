#!/usr/bin/env python3
import re

filename = 'day3-input.txt'
rawdata = open(filename, 'r').read()

matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", rawdata)
result = 0
enabled = True

for match in matches:
    instruction = match.split('(')[0]

    if instruction == "don't": enabled = False
    if instruction == "do": enabled = True
    if instruction == "mul" and enabled:
        [a, b] = match.split(',')
        a = int(a.split("(")[1])
        b = int(b.split(")")[0])
        result += a * b

print(result)
#!/usr/bin/env python3

filename = 'day1-input.txt'
rawdata = open(filename, 'r').read()

list_a = []
list_b = []

result = 0

# create our lists
for line in rawdata.split('\n'):
    list_a.append(int(line.split(' ')[0]))
    list_b.append(int(line.split(' ')[-1]))

# sort our lists
list_a = sorted(list_a)
list_b = sorted(list_b)

for i in range(len(list_a)):
    result += abs(list_a[i] - list_b[i])

print(result)
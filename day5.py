#!/usr/bin/env python3
from pprint import pprint
import re

filename = 'day5-input.txt'
rawdata = open(filename, 'r').read()
rawrules: str = ""
rules: dict = {}
rawupdates: str = ""
updates: list = []

middles: list = []

# split our puzzle input
rawrules, rawupdates = rawdata.split('\n\n')
# rules = [x.split("|") for x in rawrules.split('\n')]
updates = [x.split(",") for x in rawupdates.split('\n')]

for rule in rawrules.split('\n'):
    id, data = rule.split("|")
    if id in rules.keys():
        rules[id].append(data)
    else:
        rules[id] = [data]

pprint(rules,None,1)
pprint(updates,None,1)

for update in updates:
    # print("\n\nUpdate: ", update)
    # pprint(rules, None, 1)
    badupdate = False
    for i in range(len(update)):
        page = update[i]
        # print("--------------> Checking page: {} at index {} <---------------- ".format(page,i))
        if page in rules.keys():
            rulepages = rules[page]
            for rulepage in rulepages:
                if rulepage in update:
                    rulepage_index = update.index(rulepage)
                    print("Found page %s at index %s, i = %s " % (rulepage, rulepage_index, i))
                    if rulepage_index < i:
                        # pprint("***MARK***")
                        badupdate = True
                        break
    if not badupdate:
        middle_index = int((len(update) - 1) / 2)
        print("update: {}, middle_index: {}".format(update, middle_index))
        middles.append(int(update[middle_index]))
    else:
        middle = 0

pprint("Middle values: %s, sum: %s" % (middles,sum(middles)))
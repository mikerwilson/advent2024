#!/usr/bin/env python3
from pprint import pprint
import re

filename = 'day5-input.txt'
rawdata = open(filename, 'r').read()
rawrules: str = ""
rules: dict = {}
rawupdates: str = ""
updates: list = []
repairlist: list = []
middles: list = []
repaired: list = []

# split our puzzle input
rawrules, rawupdates = rawdata.split('\n\n')
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
                    # print("Found page %s at index %s, i = %s " % (rulepage, rulepage_index, i))
                    if rulepage_index < i:
                        # pprint("***MARK***")
                        badupdate = True
                        break
    if not badupdate:
        middle_index = int((len(update) - 1) / 2)
        # print("update: {}, middle_index: {}".format(update, middle_index))
        middles.append(int(update[middle_index]))
    else:
        repairlist.append(update)
        middle = 0

for update in repairlist:
    broken = True
    passes = 0
    print("Repairing update: ", update)
    while broken:
        brokencount = 0
        passes += 1
        for i in range(len(update)):
            page = update[i]
            print("--------------> Checking page: {} at index {} <---------------- ".format(page,i))
            if page in rules.keys():
                rulepages = rules[page]
                for rulepage in rulepages:
                    if rulepage in update:
                        rulepage_index = update.index(rulepage)
                        print("Found page %s at index %s, i = %s " % (rulepage, rulepage_index, i))
                        if rulepage_index < i:
                            # shift the violating page one to the left and try again
                            print("Shifting page %s from %s to %s" % (rulepage, rulepage_index, i))
                            brokencount += 1
                            update.pop(rulepage_index)
                            update.insert(i, rulepage)
                            break

        if brokencount == 0:
            print("Repaired in %s passes" % passes)
            repaired.append(update)
            broken = False

r_middles: list = []

for r in repaired:
    middle_index = int((len(r) - 1) / 2)
    r_middles.append(int(r[middle_index]))

pprint("Middle values for good lists: %s, sum: %s" % (middles,sum(middles)))

pprint("Repair list: %s. sum: %s" % (repairlist,sum(r_middles)))

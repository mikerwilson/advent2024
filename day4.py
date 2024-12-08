#!/usr/bin/env python3
from pprint import pprint
import re

filename = 'day4-input.txt'
rawdata = open(filename, 'r').read()
grid: list = []
results: list = []
lines: list = []
matchcount: int = 0

# put the puzzle input into a grid
for line in rawdata.split('\n'):
    grid.append(list(line))
    lines.append(line)


pprint(grid)
pprint(lines)

def getpos(pos):
    global grid
    x, y = pos
    return grid[x][y]


def checklist(checkthis):
    result = []
    for line in checkthis:
        print(line)
        matches = re.findall(r"XMAS|SAMX", line)
        for item in matches:
            result += [item]

    return result

def radar(rx,ry):
    global grid
    xmas = ['XMAS', 'SAMX']
    min_x = max(0,rx - 3)
    max_x = min(rx + 3, len(grid)-1)
    min_y = max(0,ry - 3)
    max_y = min(ry + 3, len(grid[0])-1)
    result = 0
    notagain = []
    print("Starting position: {},{} ; min: {},{} ; max: {}, {}".format(rx,ry,min_x,min_y,max_x,max_y))

    def line(sx,sy,ex,ey):
        # From a start and a destination, get us a "line" of coordinates.
        result: list = []
        xes: list = []
        yes: list = []

        print("(line fn) from: {},{} -> {},{}".format(sx,sy,ex,ey))
        if sx == ex:
            xes = list([sx] * 4)
        else:
            if sx > ex:
                step = -1
            else:
                step = 1

            ex = ex + step
            xes = list(range(sx,ex,step))

        if sy == ey:
            yes = list([sy] * 4)
        else:
            if sy > ey:
                step = -1
            else:
                step = 1

            ey = ey + step
            yes = list(range(sy,ey,step))

        print("Generating line from lists: %s and %s" % (xes,yes))

        for i in range(0,min(len(xes),len(yes))):
            result += [[xes[i],yes[i]]]

        print("Generated line: %s" % result)
        return result

    def _getword(line):
        word = ""
        for coordinate in line: word += getpos(coordinate)
        return word

    print("----------> Radar searching position: {}, {}".format(rx,ry))
    # search left
    directions = [['W',rx,min_y],
                  ['E',rx,max_y],
                  ['N',max_x,ry],
                  ['S',min_x,ry],
                  ['SE',max_x,max_y],
                  ['NW',min_x,min_y],
                  ['SW',max_x,min_y],
                  ['NE',min_x,max_y]
                  ]


    for direction in directions:
        label, ex, ey = direction
        print("Direction ({}): from: {},{} -> to: {},{}".format(label, rx, ry, ex, ey))
        hash = "{},{},{},{}".format(rx,ry,ex,ey)
        print("hash: {}".format(hash))
        if hash in notagain:
            print("Skipping duplicate line due to hash %s" % hash)
            continue
        word = _getword(line(rx,ry,ex,ey))
        # print("Word: {}".format(word))
        if word in xmas:
            print("Word: {} found in direction: {}".format(word,label))
            result += 1
        notagain.append(hash)

    return result


def find_all_indices(string, substring):
    indices = []
    for match in re.finditer(substring, string):
        indices.append(match.start())
    return indices

locations = []
for l in range(len(lines)):
    # Look through each line for instances of "X" to use as a "radar" search
    for loc in find_all_indices(lines[l], 'X'):
        locations += [[l,loc]]

pprint("Locations: {}".format(locations))

for loc in locations:
    # print("\n================> Location {} <=============\n\n".format(loc))
    matches = radar(loc[0],loc[1])
    matchcount += matches
    print(" ********************************* Location %s has %d match(es)" % (loc, matches))

print("Matches: %s" % (matchcount))
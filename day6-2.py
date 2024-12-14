#!/usr/bin/env python3
import copy
from collections import OrderedDict
from pprint import pprint
import re

filename = 'day6-test.txt'
rawdata = open(filename, 'r').read()
grid: list = []
lines: list = []
initial_path = OrderedDict()
c: list = [] # Cursor
s: list = [] # Starting point
goodblocks: list = [] # list of good blocking points

def getpos():
    global grid
    global c
    x, y = c
    return grid[x][y]

def markpos(char = 'X'):
    global grid
    global c
    x, y = c
    grid[x][y] = char

def move():
    global grid
    global c
    global dirs
    global dir

    cx, cy = c
    nx, ny = cx + dirs[dir][0], cy + dirs[dir][1]


    if nx < 0 or \
        nx > (len(grid) -1) or \
        ny < 0 or \
        ny > (len(grid[0]) -1):
        # print("We've gone negative!  Most recent cursor position: {},{}".format(cx, cy))
        # print("*** WHOOPS! @ {},{}***".format(cx, cy))
        markpos('E')
        return False
    else:
        c = [nx, ny]
        val = getpos()

    if  val == '#' or val == 'O':
        c = [cx, cy] # cursor back, just change directions
        if dir == 'N': dir = 'E'
        elif dir == 'E': dir = 'S'
        elif dir == 'S': dir = 'W'
        elif dir == 'W': dir = 'N'

    mark = dirs[dir][2]
    markpos(mark)

    return True

def resetgrid():
    global grid
    global c
    global s
    global original_grid

    c = s.copy()
    grid = copy.deepcopy(original_grid)


def runpath(tracking_dict, maxhits = None):
    global grid
    global dir
    # Get our initial path
    loop = True
    dir = "N"
    while True:
        # Place an X where our cursor is
        markpos()
        hash = ",".join(str(num) for num in c)
        if not hash in tracking_dict.keys():
            tracking_dict[hash] = 1
        else:
            tracking_dict[hash] += 1
            if maxhits and tracking_dict[hash] >= maxhits:
                loop = True
                break

        if not move():
            loop = False
            break
    return loop

# split our puzzle input
# put the puzzle input into a grid
for line in rawdata.split('\n'):
    grid.append(list(line))
    lines.append(line)

#define our cursor
c = [0,0]
dir = 'N'
dirs = OrderedDict()
dirs['N'] = [-1,0,"^"]
dirs['E'] = [0,1,">"]
dirs['S'] = [1,0,"V"]
dirs['W'] = [0,-1,"<"]

pprint(dirs)

max_x, max_y = len(grid) - 1, len(grid[0]) - 1

for x in range(max_x):
    if "^" in grid[x]:
        y = grid[x].index('^')
        c = [x,y]
        s = [x,y]
        break

# print("Current cusor position: {}".format(c))
# pprint(grid)

original_grid = copy.deepcopy(grid)
runpath(initial_path)



positions = 0
for x in range(max_x + 1):
    positions += grid[x].count('X')
    positions += grid[x].count('E')

# iterate through the dictionary of the path (skip the first one)
tries: dict = {}
# pprint("Initial path: {}".format(initial_path.keys()))
passnumber = 1
for spot in initial_path.keys():
    print("Pass {} of {}".format(passnumber, len(initial_path.keys())))
    resetgrid()
    c = [int(x) for x in spot.split(",")]
    thisspot = [int(x) for x in spot.split(",")]
    # pprint("c: {}, thisspot: {}".format(c,thisspot))
    thispath = {}
    if c[0] == s[0] and c[1] == s[1]:
        # Skip our starting point
        continue

    if spot in tries.keys():
        # already tried this one.  we can skip it.
        print("Skipping {}".format(spot))
        continue
    else:
        tries[spot] = 1

    # Place an O and run the route.
    markpos("O")

    # Go back to the starting position
    c = s.copy()

    if runpath(thispath, 100):
        # if the position is good, then put it in the list for counting later
        goodblocks += [thisspot]

    passnumber += 1

pprint("Positions: {}".format(positions))
pprint("Path: {}".format(initial_path))
pprint("Good blocks: {}".format(goodblocks))
pprint("Good block count: {}".format(len(goodblocks)))
resetgrid()

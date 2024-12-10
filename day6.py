#!/usr/bin/env python3
from collections import OrderedDict
from pprint import pprint
import re

filename = 'day6-input.txt'
rawdata = open(filename, 'r').read()
grid: list = []
lines: list = []

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
        print("We've gone negative!  Most recent cursor position: {},{}".format(cx, cy))
        print("*** WHOOPS! @ {},{}***".format(cx, cy))
        markpos('E')
        return False
    else:
        c = [nx, ny]
        val = getpos()

    if  val == '#':
        c = [cx, cy] # cursor back, just change directions
        if dir == 'N': dir = 'E'
        elif dir == 'E': dir = 'S'
        elif dir == 'S': dir = 'W'
        elif dir == 'W': dir = 'N'

    mark = dirs[dir][2]
    markpos(mark)

    return True

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
        break

print("Current cusor position: {}".format(c))
pprint(grid)

while True:
    # Place an X where our cursor is
    markpos()
    if not move(): break

# pprint(grid,None,1,max_y + 1)
pprint(grid, None, 1, 2000)

positions = 0
for x in range(max_x + 1):
    positions += grid[x].count('X')
    positions += grid[x].count('E')


pprint("Positions: {}".format(positions))

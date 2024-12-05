#!/usr/bin/env python3
from pprint import pprint

filename = 'day4-test.txt'
rawdata = open(filename, 'r').read()
grid: list = []

# put the puzzle input into a grid
for line in rawdata.split('\n'):
    grid.append(list(line))

pprint(grid)

def generate_gridpoints(x,y):
    global grid
    max_x = len(grid)
    max_y = len(grid[0])

    results = []

    print("Generating gridpoints for: [%s,%s]" % (x,y))
    # horizontal left to right
    # x, y:y+4


    return results

for x in range(len(grid)):
    for y in range(len(grid[x])-1):
        # print(grid[x][y], end='')
        # Grab up to 8 options
        # create tuples for all of the directions, respecting boundaries of the matrix
        words = []
        gridpoints = generate_gridpoints(x,y)
        pprint(gridpoints)


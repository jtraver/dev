#!/usr/bin/python

r0 = [ 5, 0, 9,  8, 1, 2,  7, 0, 0 ]
r1 = [ 0, 0, 0,  9, 0, 6,  2, 5, 1 ]
r2 = [ 0, 0, 2,  0, 3, 0,  0, 6, 0 ]

r3 = [ 0, 0, 0,  0, 0, 5,  0, 7, 0 ]
r4 = [ 8, 7, 6,  0, 2, 0,  5, 4, 9 ]
r5 = [ 0, 4, 0,  7, 0, 0,  0, 0, 0 ]

r6 = [ 0, 5, 0,  0, 9, 0,  8, 0, 0 ]
r7 = [ 7, 9, 8,  1, 0, 4,  0, 0, 0 ]
r8 = [ 0, 0, 1,  2, 7, 8,  4, 0, 5 ]

g0 = [ r0, r1, r2, r3, r4, r5, r6, r7, r8 ]

def print_grid(grid):
    for x in xrange(9):
        line = ''
        for y in xrange(9):
            line += ' %d' % grid[x][y]
        print "%s" % line

def check_grid_solved(grid):
    for x in xrange(9):
        row = {}
        col = {}
        for y in xrange(9):
            rcell = grid[x][y]
            if rcell in row:
                return False
            row[rcell] = 1
            ccell = grid[y][x]
            if ccell in col:
                return False
            col[ccell] = 1
    for x1 in xrange(0, 9, 3):
        for y1 in xrange(0, 9, 3):
            # print "%d %d" % (x1, y1)
            sgrid = {}
            for x2 in xrange(3):
                line = ''
                for y2 in xrange(3):
                    cell = grid[x1 + x2][y1 + y2]
                    line += " %d" % cell
                    if cell in sgrid:
                        return False
                    sgrid[cell] = 1
                # print line
            # print "subgrid is ok"
    return True


def check_grid_consistent(grid):
    for x in xrange(9):
        row = {}
        col = {}
        for y in xrange(9):
            rcell = grid[x][y]
            if rcell != 0 and rcell in row:
                return False
            row[rcell] = 1
            ccell = grid[y][x]
            if ccell != 0 and ccell in col:
                return False
            col[ccell] = 1
    for x1 in xrange(0, 9, 3):
        for y1 in xrange(0, 9, 3):
            # print "%d %d" % (x1, y1)
            sgrid = {}
            for x2 in xrange(3):
                line = ''
                for y2 in xrange(3):
                    cell = grid[x1 + x2][y1 + y2]
                    line += " %d" % cell
                    if cell != 0 and cell in sgrid:
                        return False
                    sgrid[cell] = 1
                # print line
            # print "subgrid is ok"
    return True

def solve_grid(grid):
    for x in xrange(9):
        for y in xrange(9):
            cell = grid[x][y]
            if cell == 0:
                for g in xrange(1, 10):
                    grid[x][y] = g
                    if check_grid_consistent(grid):
                        if check_grid_solved(grid):
                            print_grid(grid)
                        solve_grid(grid)
                    grid[x][y] = 0

def main():
    print_grid(g0)
    solve_grid(g0)

main()

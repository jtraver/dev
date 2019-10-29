#!/usr/bin/env python3
#!/usr/bin/python

import yaml
import sys

def main():
    grid = init('../../../test/john/env/yml/s001.yml')
    solve(grid)
    show_rows(grid)

def init(filename):
    grid = yaml.load(file(filename))
    get_squares(grid)
    get_rows(grid)
    get_cols(grid)
    get_grid(grid)
    return grid

def reinit(grid):
    get_squares(grid)
    get_rows(grid)
    get_cols(grid)
    get_grid(grid)

def show_squares(grid):
    global squares
    squares = []
    for sn in xrange(1, 10):
        get_square(grid, sn)
    for sn in xrange(1, 10):
        square = squares[sn - 1]
        print "square %s %s" % (str(sn), str(square))

def get_squares(grid):
    global squares
    squares = []
    for sn in xrange(1, 10):
        get_square(grid, sn)
    # for sn in xrange(1, 10):
        # square = squares[sn - 1]
        # print "square %s %s" % (str(sn), str(square))

def get_square(grid, sn):
    squares.append([])
    sx = (sn - 1) / 3
    sy = (sn - 1) % 3
    sa = grid[sx][sy]
    # squares[sn - 1].append(sa)
    for sx in xrange(3):
        for sy in xrange(3):
            squares[sn - 1].append(sa[sx][sy])

def show_rows(grid):
    global rows
    rows = []
    for rn in xrange(1, 10):
        get_row(grid, rn)
    for rn in xrange(1, 10):
        row = rows[rn - 1]
        print "row %s %s" % (str(rn), str(row))

def get_rows(grid):
    global rows
    rows = []
    for rn in xrange(1, 10):
        get_row(grid, rn)
    # for rn in xrange(1, 10):
        # row = rows[rn - 1]
        # print "row %s %s" % (str(rn), str(row))

def get_row(grid, rn):
    sx = (rn - 1) / 3
    sr = ((rn - 1) - (sx * 3)) % 3
    row = []
    for sy in xrange(3):
        # sa = grid[sx][sy]
        ra = grid[sx][sy][sr]
        for x1 in xrange(3):
            row.append(ra[x1])
    rows.append(row)

def get_cols(grid):
    global cols
    cols = []
    for cn in xrange(1, 10):
        get_col(grid, cn)
    # for cn in xrange(1, 10):
        # print "column %s %s" % (str(cn), str(cols[cn - 1]))

def get_col(grid, cn):
    # 1 0 1 4 7 (0, 0), (0, 1), (0, 2)
    # 2 1 1 4 7
    # 3 2 1 4 7
    # 4 0 2 5 8 (1, 0), (1, 1), (1, 2)
    # 5 1 2 5 8
    # 6 2 2 5 8
    # 7 0 3 6 9 (2, 0), (2, 1), (2, 2)
    # 8 1 3 6 9
    # 9 2 3 6 9
    sy = (cn - 1) / 3
    sc = ((cn - 1) - (sy * 3)) % 3
    col = []
    for sx in xrange(3):
        sa = grid[sx][sy]
        for sr in xrange(3):
            col.append(sa[sr][sc])
    cols.append(col)

def get_grid(grid):
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    square = gx * 3 + gy
                    if not cell in squares[square]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: square = %s %s" % (str(square), str(squares[square]))
                        sys.exit(1)
                    row = gx * 3 + sx
                    if not cell in rows[row]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: row = %s %s" % (str(row), str(rows[row]))
                        sys.exit(1)
                    col = gy * 3 + sy
                    if not cell in cols[col]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: col = %s %s" % (str(col), str(cols[col]))
                        sys.exit(1)

def solve(grid):
    count = 0
    while (check_choices(grid)):
        count += 1
        print "\nresult of check_choices %s" % str(count)
        show_squares(grid)

def check_choices(grid):
    ret = False
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    if not cell:
                        square = gx * 3 + gy
                        row = gx * 3 + sx
                        col = gy * 3 + sy
                        choices = get_choices(square, row, col)
                        print "%s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(choices))
                        if len(choices) == 1:
                            grid[gx][gy][sx][sy] = choices[0]
                            reinit(grid)
                            ret = True
    return ret

def get_choices(square, row, col):
    used = []
    for x1 in xrange(9):
        s1 = squares[square][x1]
        if s1:
            used.append(s1)
        r1 = rows[row][x1]
        if r1:
            used.append(r1)
        c1 = cols[col][x1]
        if c1:
            used.append(c1)
    choices = []
    for x1 in xrange(1, 10):
        if not x1 in used:
            choices.append(x1)
    return choices

main()

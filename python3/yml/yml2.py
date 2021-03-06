#!/usr/bin/env python3
#!/usr/bin/python

import yaml
import sys

def main():
    grid5 = yaml.load(file('grid5.yml'))
    # debug1(grid5)
    show_squares(grid5)
    show_rows(grid5)
    show_cols(grid5)
    show_grid(grid5)

def debug1(gridn):
    print("gridn = %s" % str(gridn))
    for sx in range(3):
        for sy in range(3):
            sn = gridn[sx][sy]
            print("%s %s = %s" % (str(sx), str(sy), str(sn)))
            if 11 in sn:
                print("found 11 in %s" % str(sn))
                sys.exit(1)
    for sx in range(3):
        for sy in range(3):
            for ix in range(3):
                r1 = gridn[sx][sy][ix]
                print("%s %s %s = %s" % (str(sx), str(sy), str(ix), str(r1)))
                if 11 in r1:
                    print("found 11 in %s" % str(r1))
                    sys.exit(1)

def show_squares(grid):
    global squares
    squares = []
    for sn in range(1, 10):
        # print "sn = %s" % str(sn)
        show_square(grid, sn)
    for sn in range(1, 10):
        square = squares[sn - 1]
        print("square %s %s" % (str(sn), str(square)))

def show_square(grid, sn):
    squares.append([])
    # print "sn = %s" % str(sn)
    sx = (sn - 1) / 3
    # print "sx = %s" % str(sx)
    sy = (sn - 1) % 3
    # print "sy = %s" % str(sy)
    sa = grid[sx][sy]
    # print "sa = %s" % str(sa)
    # print "%s %s" % (str(sn), str(sa))
    # squares[sn - 1].append(sa)
    for sx in range(3):
        for sy in range(3):
            squares[sn - 1].append(sa[sx][sy])

def show_rows(grid):
    global rows
    rows = []
    for rn in range(1, 10):
        # print "rn = %s" % str(rn)
        show_row(grid, rn)
    # print "rows = %s" % str(rows)
    for rn in range(1, 10):
        row = rows[rn - 1]
        print("row %s %s" % (str(rn), str(row)))

def show_row(grid, rn):
    # print "rn = %s" % str(rn)
    sx = (rn - 1) / 3
    # print "sx = %s" % str(sx)
    sr = ((rn - 1) - (sx * 3)) % 3
    # print "sr = %s" % str(sr)
    row = []
    for sy in range(3):
        # print "sy = %s" % str(sy)
        # sa = grid[sx][sy]
        # print "sa = %s" % str(sa)
        ra = grid[sx][sy][sr]
        # print "ra = %s" % str(ra)
        for x1 in range(3):
            row.append(ra[x1])
    rows.append(row)

def show_cols(grid):
    global cols
    cols = []
    for cn in range(1, 10):
        # print "cn = %s" % str(cn)
        show_col(grid, cn)
    for cn in range(1, 10):
        print("column %s %s" % (str(cn), str(cols[cn - 1])))

def show_col(grid, cn):
    # print "cn = %s" % str(cn)
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
    # print "sy = %s" % str(sy)
    sc = ((cn - 1) - (sy * 3)) % 3
    # print "sc = %s" % str(sc)
    col = []
    for sx in range(3):
        # print "sx = %s" % str(sx)
        sa = grid[sx][sy]
        # print "sa = %s" % str(sa)
        for sr in range(3):
            col.append(sa[sr][sc])
    # print "%s %s" % (str(cn), str(col))
    cols.append(col)

def show_grid(grid):
    for gx in range(3):
        for gy in range(3):
            for sx in range(3):
                for sy in range(3):
                    cell = grid[gx][gy][sx][sy]
                    # print "%s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                    square = gx * 3 + gy
                    if not cell in squares[square]:
                        print("ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell)))
                        print("ERROR: square = %s %s" % (str(square), str(squares[square])))
                        sys.exit(1)
                    row = gx * 3 + sx
                    if not cell in rows[row]:
                        print("ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell)))
                        print("ERROR: row = %s %s" % (str(row), str(rows[row])))
                        sys.exit(1)
                    col = gy * 3 + sy
                    if not cell in cols[col]:
                        print("ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell)))
                        print("ERROR: col = %s %s" % (str(col), str(cols[col])))
                        sys.exit(1)

main()

#!/usr/bin/python

import yaml
import sys

def verify_cols(grid):
    # print "verify_cols"
    for icol in xrange(9):
        for c1 in xrange(9):
            ccell = cols[icol][c1]
            gx, gy, sx, sy = get_grid_coordinates_from_col(icol, c1)
            cell = grid[gx][gy][sx][sy]
            if ccell != cell:
                print "ERROR"
                sys.exit(1)
            gicol, gc1 = get_col_from_grid_coordinates(gx, gy, sx, sy)
            if gicol != icol or gc1 != c1:
                print "ERROR"
                sys.exit(1)

def verify_rows(grid):
    # print "verify_rows"
    for irow in xrange(9):
        for r1 in xrange(9):
            rcell = rows[irow][r1]
            gx, gy, sx, sy = get_grid_coordinates_from_row(irow, r1)
            cell = grid[gx][gy][sx][sy]
            if rcell != cell:
                print "ERROR"
                sys.exit(1)
            girow, gr1 = get_row_from_grid_coordinates(gx, gy, sx, sy)
            if girow != irow or gr1 != r1:
                print "ERROR"
                sys.exit(1)

def verify_squares(grid):
    # print "verify_squares"
    for isquare in xrange(9):
        for s1 in xrange(9):
            scell = squares[isquare][s1]
            gx, gy, sx, sy = get_grid_coordinates_from_square(isquare, s1)
            cell = grid[gx][gy][sx][sy]
            if scell != cell:
                print "ERROR"
                sys.exit(1)
            gisquare, gs1 = get_square_from_grid_coordinates(gx, gy, sx, sy)
            if gisquare != isquare or gs1 != s1:
                print "ERROR"
                sys.exit(1)

def get_square_from_grid_coordinates(gx, gy, sx, sy):
    isquare = gx * 3 + gy
    s1 = sx * 3 + sy
    return isquare, s1

def get_grid_coordinates_from_square(isquare, s1):
    sgx = (isquare) / 3
    sgy = (isquare) % 3
    ssx = s1 / 3
    ssy = s1 % 3
    return sgx, sgy, ssx, ssy

def get_row_from_grid_coordinates(gx, gy, sx, sy):
    irow = gx * 3 + sx
    r1 = gy * 3 + sy
    return irow, r1

def get_grid_coordinates_from_row(irow, r1):
    rgx = irow / 3
    rgy = r1 / 3
    rsx = irow % 3
    rsy = r1 % 3
    return rgx, rgy, rsx, rsy

def get_col_from_grid_coordinates(gx, gy, sx, sy):
    icol = gy * 3 + sy
    c1 = gx * 3 + sx
    return icol, c1

def get_grid_coordinates_from_col(icol, c1):
    cgx = c1 / 3
    cgy = icol / 3
    csx = c1 % 3
    csy = icol % 3
    return cgx, cgy, csx, csy

def verify_grid(grid):
    # print "verify_grid"
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    # squares
                    isquare, s1 = get_square_from_grid_coordinates(gx, gy, sx, sy)
                    scell = squares[isquare][s1]
                    if cell != scell:
                        print "ERROR: %s%s%s%s = %s and square %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(isquare), str(s1), str(scell))
                        sys.exit(1)
                    sgx, sgy, ssx, ssy = get_grid_coordinates_from_square(isquare, s1)
                    scell = grid[sgx][sgy][ssx][ssy]
                    if cell != scell or gx != sgx or gy != sgy or sx != ssx or sy != ssy:
                        print "ERROR: %s%s%s%s = %s and square %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(isquare), str(s1), str(sgx), str(sgy), str(ssx), str(ssy), str(scell))
                        sys.exit(1)
                    # rows
                    irow, r1 = get_row_from_grid_coordinates(gx, gy, sx, sy)
                    rcell = rows[irow][r1]
                    if cell != rcell:
                        print "ERROR: %s%s%s%s = %s and row %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(irow), str(r1), str(rcell))
                        sys.exit(1)
                    rgx, rgy, rsx, rsy = get_grid_coordinates_from_row(irow, r1)
                    rcell = grid[rgx][rgy][rsx][rsy]
                    if cell != rcell or gx != rgx or gy != rgy or sx != rsx or sy != rsy:
                        print "ERROR: %s%s%s%s = %s and row %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(irow), str(r1), str(rgx), str(rgy), str(rsx), str(rsy), str(rcell))
                        sys.exit(1)
                    # cols
                    icol, c1 = get_col_from_grid_coordinates(gx, gy, sx, sy)
                    ccell = cols[icol][c1]
                    if cell != ccell:
                        print "ERROR: %s%s%s%s = %s and col %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(icol), str(c1), str(ccell))
                        sys.exit(1)
                    cgx, cgy, csx, csy = get_grid_coordinates_from_col(icol, c1)
                    ccell = grid[cgx][cgy][csx][csy]
                    if cell != ccell or gx != cgx or gy != cgy or sx != csx or sy != csy:
                        print "ERROR: %s%s%s%s = %s and col %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(icol), str(c1), str(cgx), str(cgy), str(csx), str(csy), str(ccell))
                        sys.exit(1)

def verify_grid_squares(grid):
    # print "verify_grid_squares"
    for sn in xrange(9):
        gx, gy, _, _ = get_grid_coordinates_from_square(sn, 0)
        square = grid[gx][gy]
        for sx in xrange(3):
            for sy in xrange(3):
                cell = square[sx][sy]
                # squares
                isquare, s1 = get_square_from_grid_coordinates(gx, gy, sx, sy)
                scell = squares[isquare][s1]
                if cell != scell:
                    print "ERROR: %s%s%s%s = %s and square %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(isquare), str(s1), str(scell))
                    sys.exit(1)
                sgx, sgy, ssx, ssy = get_grid_coordinates_from_square(isquare, s1)
                scell = grid[sgx][sgy][ssx][ssy]
                if cell != scell or gx != sgx or gy != sgy or sx != ssx or sy != ssy:
                    print "ERROR: %s%s%s%s = %s and square %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(isquare), str(s1), str(sgx), str(sgy), str(ssx), str(ssy), str(scell))
                    sys.exit(1)
                # rows
                irow, r1 = get_row_from_grid_coordinates(gx, gy, sx, sy)
                rcell = rows[irow][r1]
                if cell != rcell:
                    print "ERROR: %s%s%s%s = %s and row %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(irow), str(r1), str(rcell))
                    sys.exit(1)
                rgx, rgy, rsx, rsy = get_grid_coordinates_from_row(irow, r1)
                rcell = grid[rgx][rgy][rsx][rsy]
                if cell != rcell or gx != rgx or gy != rgy or sx != rsx or sy != rsy:
                    print "ERROR: %s%s%s%s = %s and row %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(irow), str(r1), str(rgx), str(rgy), str(rsx), str(rsy), str(rcell))
                    sys.exit(1)
                # cols
                icol, c1 = get_col_from_grid_coordinates(gx, gy, sx, sy)
                ccell = cols[icol][c1]
                if cell != ccell:
                    print "ERROR: %s%s%s%s = %s and col %s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(icol), str(c1), str(ccell))
                    sys.exit(1)
                cgx, cgy, csx, csy = get_grid_coordinates_from_col(icol, c1)
                ccell = grid[cgx][cgy][csx][csy]
                if cell != ccell or gx != cgx or gy != cgy or sx != csx or sy != csy:
                    print "ERROR: %s%s%s%s = %s and col %s%s %s%s%s%s = %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(icol), str(c1), str(cgx), str(cgy), str(csx), str(csy), str(ccell))
                    sys.exit(1)

def verify(grid):
    # print "verify"
    verify_grid(grid)
    verify_grid_squares(grid)
    verify_squares(grid)
    verify_rows(grid)
    verify_cols(grid)

def init(filename):
    grid = yaml.load(file(filename))
    get_squares(grid)
    get_rows(grid)
    get_cols(grid)
    get_grid(grid)
    verify(grid)
    return grid

def reinit(grid):
    get_squares(grid)
    get_rows(grid)
    get_cols(grid)
    get_grid(grid)
    verify(grid)

def show_squares(grid):
    global squares
    squares = []
    for sn in xrange(9):
        get_square(grid, sn)
    for sn in xrange(9):
        square = squares[sn]
        print "square %s %s" % (str(sn + 1), str(square))

def get_squares(grid):
    global squares
    squares = []
    for sn in xrange(9):
        get_square(grid, sn)
    # for sn in xrange(9):
        # square = squares[sn]
        # print "square %s %s" % (str(sn), str(square))

def get_square(grid, sn):
    squares.append([])
    gx, gy, _, _ = get_grid_coordinates_from_square(sn, 0)
    sa = grid[gx][gy]
    # squares[sn].append(sa)
    for sx in xrange(3):
        for sy in xrange(3):
            squares[sn].append(sa[sx][sy])

def show_rows(grid):
    global rows
    rows = []
    for rn in xrange(9):
        get_row(grid, rn)
    for rn in xrange(9):
        row = rows[rn]
        print "row %s %s" % (str(rn + 1), str(row))

def get_rows(grid):
    global rows
    rows = []
    for rn in xrange(9):
        get_row(grid, rn)
    # for rn in xrange(9):
        # row = rows[rn]
        # print "row %s %s" % (str(rn), str(row))

def get_row(grid, rn):
    sx = (rn) / 3
    sr = ((rn) - (sx * 3)) % 3
    row = []
    for sy in xrange(3):
        # sa = grid[sx][sy]
        ra = grid[sx][sy][sr]
        for x1 in xrange(3):
            row.append(ra[x1])
    rows.append(row)

def show_cols(grid):
    global cols
    cols = []
    for cn in xrange(9):
        get_col(grid, cn)
    for cn in xrange(9):
        print "column %s %s" % (str(cn + 1), str(cols[cn]))


def get_cols(grid):
    global cols
    cols = []
    for cn in xrange(9):
        get_col(grid, cn)
    # for cn in xrange(9):
        # print "column %s %s" % (str(cn), str(cols[cn]))

def get_col(grid, cn):
    sy = (cn) / 3
    sc = ((cn) - (sy * 3)) % 3
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
                    isquare, s1 = get_square_from_grid_coordinates(gx, gy, sx, sy)
                    if square != isquare:
                        print "ERROR"
                        sys.exit(1)
                    if not cell in squares[square]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: square = %s %s" % (str(square), str(squares[square]))
                        sys.exit(1)
                    row = gx * 3 + sx
                    irow, r1 = get_row_from_grid_coordinates(gx, gy, sx, sy)
                    if row != irow:
                        print "ERROR"
                        sys.exit(1)
                    if not cell in rows[row]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: row = %s %s" % (str(row), str(rows[row]))
                        sys.exit(1)
                    col = gy * 3 + sy
                    icol, c1 = get_col_from_grid_coordinates(gx, gy, sx, sy)
                    if col != icol:
                        print "ERROR"
                        sys.exit(1)
                    if not cell in cols[col]:
                        print "ERROR: %s %s %s %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                        print "ERROR: col = %s %s" % (str(col), str(cols[col]))
                        sys.exit(1)

def check_choices(grid):
    ret = False
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    print "%s%s%s%s is %s" % (str(gx), str(gy), str(sx), str(sy), str(cell))
                    if not cell or isinstance(cell, list):
                        square = gx * 3 + gy
                        row = gx * 3 + sx
                        col = gy * 3 + sy
                        choices = get_choices(cell, square, row, col)
                        print "choices for %s%s%s%s %s -> %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(choices))
                        if len(choices) == 1:
                            grid[gx][gy][sx][sy] = choices[0]
                            ret = True
                            reinit(grid)
                        else:
                            if not cell or (isinstance(cell, list) and len(choices) < len(cell)):
                                ret = True
                                grid[gx][gy][sx][sy] = choices
                                reinit(grid)
    return ret

def get_choices(cell, square, row, col):
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
            if isinstance(cell, list):
                if x1 in cell:
                    choices.append(x1)
            else:
                choices.append(x1)
    return choices

def common_choices(grid):
    ret = False
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    if isinstance(cell, list):
                        isquare = gx * 3 + gy
                        irow = gx * 3 + sx
                        icol = gy * 3 + sy
                        # columns
                        col = cols[icol]
                        cmatches = []
                        for c1 in xrange(9):
                            if cell == col[c1]:
                                # print "found %s%s%s%s %s in col %s at %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(icol), str(c1))
                                gc = get_grid_coordinates_from_col(icol, c1)
                                # print "gc for col %s%s is %s" % (str(icol), str(c1), str(gc))
                                ccell = grid[gc[0]][gc[1]][gc[2]][gc[3]]
                                if cell == ccell:
                                    cmatches.append(c1)
                                else:
                                    print "ERROR: did not find col %s%s cell %s%s%s%s at %s" % (str(icol), str(c1), str(gx), str(gy), str(sx), str(sy), str(gc))
                        if len(cmatches) == len(cell):
                            # print "%s%s%s%s has %s col matches %s in %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(cmatches), str(icol), str(col))
                            for c1 in xrange(9):
                                scol = col[c1]
                                if not isinstance(scol, list):
                                    continue
                                if cell == scol:
                                    continue
                                nlist = []
                                for s2 in scol:
                                    if not s2 in cell:
                                        nlist.append(s2)
                                if nlist != scol:
                                    ret = True
                                    print "need to update column %s to %s" % (str(scol), str(nlist))
                                    gc = get_grid_coordinates_from_col(icol, c1)
                                    if len(nlist) == 1:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist[0]
                                    else:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist
                                    # print "col was %s" % str(col)
                                    reinit(grid)
                                    # col = cols[icol]
                                    # print "col is %s" % str(col)
                        # rows
                        row = rows[irow]
                        rmatches = []
                        for r1 in xrange(9):
                            if cell == row[r1]:
                                # print "found %s%s%s%s %s in row %s at %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(irow), str(r1))
                                gc = get_grid_coordinates_from_row(irow, r1)
                                # print "gc for row %s%s is %s" % (str(irow), str(r1), str(gc))
                                rcell = grid[gc[0]][gc[1]][gc[2]][gc[3]]
                                if cell == rcell:
                                    rmatches.append(r1)
                                else:
                                    print "ERROR: did not find row %s%s cell %s%s%s%s at %s" % (str(irow), str(r1), str(gx), str(gy), str(sx), str(sy), str(gc))
                        if len(rmatches) == len(cell):
                            # print "%s%s%s%s has %s row matches %s in %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(rmatches), str(irow), str(row))
                            for r1 in xrange(9):
                                srow = row[r1]
                                if not isinstance(srow, list):
                                    continue
                                if cell == srow:
                                    continue
                                nlist = []
                                for s2 in srow:
                                    if not s2 in cell:
                                        nlist.append(s2)
                                if nlist != srow:
                                    ret = True
                                    print "need to update row %s to %s" % (str(srow), str(nlist))
                                    gc = get_grid_coordinates_from_row(irow, r1)
                                    if len(nlist) == 1:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist[0]
                                    else:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist
                                    # print "row was %s" % str(row)
                                    reinit(grid)
                                    # row = rows[irow]
                                    # print "row is %s" % str(row)
                        # squares
                        square = squares[isquare]
                        smatches = []
                        for s1 in xrange(9):
                            if cell == square[s1]:
                                # print "found %s%s%s%s %s in square %s at %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(isquare), str(s1))
                                gc = get_grid_coordinates_from_square(isquare, s1)
                                # print "gc for square %s%s is %s" % (str(isquare), str(s1), str(gc))
                                scell = grid[gc[0]][gc[1]][gc[2]][gc[3]]
                                if cell == scell:
                                    smatches.append(s1)
                                else:
                                    print "ERROR: did not find square %s%s cell %s%s%s%s at %s" % (str(isquare), str(s1), str(gx), str(gy), str(sx), str(sy), str(gc))
                        if len(smatches) == len(cell):
                            # print "%s%s%s%s has %s square matches %s in %s %s" % (str(gx), str(gy), str(sx), str(sy), str(cell), str(smatches), str(isquare), str(square))
                            for s1 in xrange(9):
                                ssquare = square[s1]
                                if not isinstance(ssquare, list):
                                    continue
                                if cell == ssquare:
                                    continue
                                nlist = []
                                for s2 in ssquare:
                                    if not s2 in cell:
                                        nlist.append(s2)
                                if nlist != ssquare:
                                    ret = True
                                    print "need to update square %s to %s" % (str(ssquare), str(nlist))
                                    gc = get_grid_coordinates_from_square(isquare, s1)
                                    if len(nlist) == 1:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist[0]
                                    else:
                                        grid[gc[0]][gc[1]][gc[2]][gc[3]] = nlist
                                    # print "square was %s" % str(square)
                                    reinit(grid)
                                    # square = squares[isquare]
                                    # print "square is %s" % str(square)
    return ret

def check_numbers(grid):
    ret = False
    for gx in xrange(3):
        for gy in xrange(3):
            for sx in xrange(3):
                for sy in xrange(3):
                    cell = grid[gx][gy][sx][sy]
                    if not isinstance(cell, list):
                        continue
                    for cnum in cell:
                        # print "looking for %s" % str(cnum)
                        # square
                        ncount = 0
                        isquare, _ = get_square_from_grid_coordinates(gx, gy, sx, sy)
                        square = squares[isquare]
                        for s1 in xrange(9):
                            scell = square[s1]
                            if isinstance(scell, list):
                                if cnum in scell:
                                    ncount += 1
                            else:
                                if scell == cnum:
                                    ncount += 1
                        if ncount == 1:
                            ret = True
                            print "square %s%s%s%s must be %s" % (str(gx), str(gy), str(sx), str(sy), str(cnum))
                            grid[gx][gy][sx][sy] = cnum
                            reinit(grid)
                            break
                        # row
                        ncount = 0
                        irow, _ = get_row_from_grid_coordinates(gx, gy, sx, sy)
                        row = rows[irow]
                        for s1 in xrange(9):
                            rcell = row[s1]
                            if isinstance(rcell, list):
                                if cnum in rcell:
                                    ncount += 1
                            else:
                                if rcell == cnum:
                                    ncount += 1
                        if ncount == 1:
                            ret = True
                            print "row %s%s%s%s must be %s" % (str(gx), str(gy), str(sx), str(sy), str(cnum))
                            grid[gx][gy][sx][sy] = cnum
                            reinit(grid)
                            break
                        # col
                        ncount = 0
                        icol, _ = get_col_from_grid_coordinates(gx, gy, sx, sy)
                        col = cols[icol]
                        for s1 in xrange(9):
                            ccell = col[s1]
                            if isinstance(ccell, list):
                                if cnum in ccell:
                                    ncount += 1
                            else:
                                if ccell == cnum:
                                    ncount += 1
                        if ncount == 1:
                            ret = True
                            print "column %s%s%s%s must be %s" % (str(gx), str(gy), str(sx), str(sy), str(cnum))
                            grid[gx][gy][sx][sy] = cnum
                            reinit(grid)
                            break
    return ret

def solve(grid):
    changed = True
    loop = 0
    while changed and loop < 10:
        loop += 1
        print "\nstart solve loop %s" % str(loop)
        changed = False
        # show_squares(grid)
        count = 0
        while (check_choices(grid)):
            count += 1
            print "\nresult of check_choices %s" % str(count)
            # show_squares(grid)
            show_rows(grid)
            changed = True
        # show_cols(grid)
        count = 0
        while (common_choices(grid)):
            count += 1
            print "\nresult of common_choices %s" % str(count)
            # show_cols(grid)
            show_rows(grid)
            changed = True
        # show_rows(grid)
        count = 0
        while (check_numbers(grid)):
            count += 1
            print "\nresult of check_numbers %s" % str(count)
            # show_rows(grid)
            show_rows(grid)
            changed = True
        # show_rows(grid)

def main():
    # grid = init('../../../test/john/env/yml/s178.yml')
    # grid = init('../../../test/john/env/yml/s105.yml')
    # grid = init('../../../test/john/env/yml/s053.yml')
    # grid = init('../../../test/john/env/yml/s001.yml')
    # grid = init('../../../test/john/env/yml/s165.yml')
    grid = init('../../../test/john/env/yml/s165a.yml')
    # grid = init('../../../test/john/env/yml/s165a1.yml')
    solve(grid)
    show_rows(grid)

main()

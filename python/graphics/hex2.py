#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

from graphics import *

XSCALE = 2550
YSCALE = 1310
XCENTER = XSCALE / 2
YCENTER = YSCALE / 2

def hex1(win, xoffset, yoffset, scale = 1.0):
    sxoffset = xoffset * scale + XCENTER
    syoffset = yoffset * scale + YCENTER
    p = Polygon(
        Point(-4 * scale + sxoffset, -7 * scale + syoffset),
        Point( 4 * scale + sxoffset, -7 * scale + syoffset),
        Point( 8 * scale + sxoffset,  0 * scale + syoffset),
        Point( 4 * scale + sxoffset,  7 * scale + syoffset),
        Point(-4 * scale + sxoffset,  7 * scale + syoffset),
        Point(-8 * scale + sxoffset,  0 * scale + syoffset))
    p.draw(win)

def main():
    scale = 7.7
    win = GraphWin("hex2", XSCALE, YSCALE)
    win.setCoords(0,0, XSCALE , YSCALE)
    # one side is 8 units long
    # height of vertical rectangle is 14
    # bulge to either side is 4

    # 1 -> 1
    # layer 0
    # center
    hex1(win, 0, 0, scale)

    # 6 -> 7
    # layer 1
    # 1.1 upper right        -> lastx + 12, lasty + 7
    hex1(win,  12,   7, scale)
    # 1.2 lower right        -> lastx + 12, lasty - 7
    hex1(win,  12,  -7, scale)
    # 1.3 bottom             -> lastx     , lasty - 14
    hex1(win,   0, -14, scale)
    # 1.4 lower left        ->  lastx - 12, lasty - 7
    hex1(win, -12,  -7, scale)
    # 1.5 upper left        ->  lastx - 12, lasty + 7
    hex1(win, -12,   7, scale)
    # 1.6 top               -> lastx      , lasty + 14
    hex1(win,   0,  14, scale)

    # 12 -> 19
    # layer 2
    # 2.1 one o'clock
    hex1(win, 12, 21, scale)
    # 2.2 two o'clock
    hex1(win, 24, 14, scale)
    # 2.3 three o'clock
    hex1(win, 24, 0, scale)
    # 2.4 four o'clock
    hex1(win, 24, -14, scale)
    # 2.5 five o'clock
    hex1(win, 12, -21, scale)
    # 2.6 six o'clock
    hex1(win, 0, -28, scale)
    # 2.7 seven o'clock
    hex1(win, -12, -21, scale)
    # 2.8 eight o'clock
    hex1(win, -24, -14, scale)
    # 2.9 nine o'clock
    hex1(win, -24, 0, scale)
    # 2.10 ten o'clock
    hex1(win, -24, 14, scale)
    # 2.11 eleven o'clock
    hex1(win, -12, 21, scale)
    # 2.12 twelve o'clock
    hex1(win, 0, 28, scale)

    # 18 -> 37
    # layer 3
    # 3.1 above one o'clock
    hex1(win, 12, 35, scale)
    # 3.2 above two o'clock
    hex1(win, 24, 28, scale)
    # 3.3 shift one o'clock
    hex1(win, 36, 21, scale)
    # 3.4 down from 3
    hex1(win, 36, 7, scale)
    # 3.5 down from 4
    hex1(win, 36, -7, scale)
    # 3.6 down from 5
    hex1(win, 36, -21, scale)
    # 3.7 down from four o'clock
    hex1(win, 24, -28, scale)
    # 3.8 down from five o'clock
    hex1(win, 12, -35, scale)
    # 3.9 bottom
    hex1(win, 0, -42, scale)
    # 3.10 down from  seven o'clock
    hex1(win, -12, -35, scale)
    # 3.11 down from eight o'clock
    hex1(win, -24, -28, scale)
    # 3.12
    hex1(win, -36, -21, scale)
    # 3.13 up from 12
    hex1(win, -36, -7, scale)
    # 3.14 up from 13
    hex1(win, -36, 7, scale)
    # 3.15 up from 14
    hex1(win, -36, 21, scale)
    # 3.16 up from ten o'clock
    hex1(win, -24, 28, scale)
    # 3.17 up from eleven o'clock
    hex1(win, -12, 35, scale)
    # 3.18 top
    hex1(win, 0, 42, scale)

    # 24 -> 61
    # layer 4
    # 4.1 above 3.1             must be 40 to 63
    hex1(win, 12, 49, scale)
    # 4.2 above 3.2             must be 40 to 63
    hex1(win, 24, 42, scale)
    # 4.3 above 3.3             must be 40 to 63
    hex1(win, 36, 35, scale)
    # 4.4                       must be 44, 45, 46, 47, 60, 61, 62, 63
    hex1(win, 48, 28, scale)
    # 4.5 down from 4.4
    hex1(win, 48, 14, scale)
    # 4.6 down from 5
    hex1(win, 48, 0, scale)
    # 4.7 down from 6
    hex1(win, 48, -14, scale)
    # 4.8 down from 7           must be 9, 11, 25, 27, 41, 43, 57 or 59
    hex1(win, 48, -28, scale)
    # 4.9
    hex1(win, 36, -35, scale)
    # 4.10
    hex1(win, 24, -42, scale)
    # 4.11
    hex1(win, 12, -49, scale)
    # 4.12 bottom
    hex1(win, 0, -56, scale)
    # 4.13
    hex1(win, -12, -49, scale)
    # 4.14
    hex1(win, -24, -42, scale)
    # 4.15                      must be 17, 21, 25, 29, 49, 53, 57 or 61
    hex1(win, -36, -35, scale)
    # 4.16
    hex1(win, -48, -28, scale)
    # 4.17
    hex1(win, -48, -14, scale)
    # 4.18
    hex1(win, -48, 0, scale)
    # 4.19
    hex1(win, -48, 14, scale)
    # 4.20
    hex1(win, -48, 28, scale)
    # 4.21
    hex1(win, -36, 35, scale)
    # 4.22
    hex1(win, -24, 42, scale)
    # 4.23
    hex1(win, -12, 49, scale)
    # 4.24 top                  must be 24 to 31
    hex1(win, 0, 56, scale)


    # 5.10 top                  must be 63 - 1 = 62
    hex1(win, 0, 70, scale)
    t = Text(Point(XCENTER,YCENTER + 70 * scale), "62")
    t.draw(win)
    # 5.20 lower right axis     must be 63 - 16 = 47
    hex1(win, 60, -35, scale)
    t = Text(Point(XCENTER + 60 * scale,YCENTER - 35 * scale), "47")
    t.draw(win)
    # 5.30 lower left axis      must be 63 - 8 = 55
    hex1(win, -60, -35, scale)
    t = Text(Point(XCENTER - 60 * scale,YCENTER - 35 * scale), "55")
    t.draw(win)


    # 30 -> 91
    # layer 5

    # 36 -> 127
    # layer 6

    # 42 -> 169 64, 128, 192, 256, 320
    # layer 6

    # 7 48 -> 217
    # 8 54 -> 261

    p0 = Point(XCENTER, YCENTER)
    p0.setFill("red")
    p0.setOutline("red")
    p0.draw(win)
    p1 = Point(XCENTER + 12 * scale, YCENTER + 7 * scale)
    l1 = Line(p0, p1)
    l1.setFill("red")
    l1.draw(win)

    t = Text(Point(XCENTER,YCENTER), "0")
    t.draw(win)

    win.getMouse()
    win.close()

main()

#
#
# __
#/  \
#\__/
#
#  ____
# /    \
#/      \
#\      /
# \____/
#
#       5
#     __  __
#    /      \
# 4            3
#  /     0    \     000000
#  \          /
# 1            2
#    \__  __/
#       0
#
#       5
#     __  __
#    /      \
# 4            3
#  /     1    \     000001
#  \          /
# 1            2
#    \______/
#       0
#
#       5
#     __  __
#    /      \
# 4            3
#  /     2    \     000010
#  \          /
# 1 \          2
#    \__  __/
#       0
#
#       5
#     __  __
#    /      \
# 4            3
#  /     3    \     000011
#  \          /
# 1 \          2
#    \______/
#       0
#
#       5
#     __  __
#    /      \
# 4            3
#  /     4    \     000100
#  \          /
# 1          / 2
#    \__  __/
#       0
#
#
#       5
#     ______
#    /      \
# 4 /        \ 3
#  /    61    \    111101
#  \          /
# 1          / 2
#    \______/
#       0
#
#       5
#     ______
#    /      \
# 4 /        \ 3
#  /    62    \    111110
#  \          /
# 1 \        / 2
#    \__  __/
#       0
#
#       5
#     ______
#    /      \
# 4 /        \ 3
#  /    63    \    111111
#  \          /
# 1 \        / 2
#    \______/
#       0

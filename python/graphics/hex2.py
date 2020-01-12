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
    scale = 3.7
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
    # 1 upper right
    hex1(win,  12,   7, scale)
    # 2 lower right
    hex1(win,  12,  -7, scale)
    # 3 bottom
    hex1(win,   0, -14, scale)
    # 4 lower left
    hex1(win, -12,  -7, scale)
    # 5 upper left
    hex1(win, -12,   7, scale)
    # 6 top
    hex1(win,   0,  14, scale)
    # 12 -> 19
    # layer 2
    # 1 one o'clock
    hex1(win, 12, 21, scale)
    # 2 two o'clock
    hex1(win, 24, 14, scale)
    # 3 three o'clock
    hex1(win, 24, 0, scale)
    # 4 four o'clock
    hex1(win, 24, -14, scale)
    # 5 five o'clock
    hex1(win, 12, -21, scale)
    # 6 six o'clock
    hex1(win, 0, -28, scale)
    # 7 seven o'clock
    hex1(win, -12, -21, scale)
    # 8 eight o'clock
    hex1(win, -24, -14, scale)
    # 9 nine o'clock
    hex1(win, -24, 0, scale)
    # 10 ten o'clock
    hex1(win, -24, 14, scale)
    # 11 eleven o'clock
    hex1(win, -12, 21, scale)
    # 12 twelve o'clock
    hex1(win, 0, 28, scale)

    # 18 -> 37
    # layer 3
    # 1 above one o'clock
    hex1(win, 12, 35, scale)
    # 2 above two o'clock
    hex1(win, 24, 28, scale)
    # 3 shift one o'clock
    hex1(win, 36, 21, scale)
    # 4 down from 3
    hex1(win, 36, 7, scale)
    # 5 down from 4
    hex1(win, 36, -7, scale)
    # 6 down from 5
    hex1(win, 36, -21, scale)
    # 7 down from four o'clock
    hex1(win, 24, -28, scale)
    # 8 down from five o'clock
    hex1(win, 12, -35, scale)
    # 9 bottom
    hex1(win, 0, -42, scale)
    # 10 down from  seven o'clock
    hex1(win, -12, -35, scale)
    # 11 down from eight o'clock
    hex1(win, -24, -28, scale)
    # 12
    hex1(win, -36, -21, scale)
    # 13 up from 12
    hex1(win, -36, -7, scale)
    # 14 up from 13
    hex1(win, -36, 7, scale)
    # 15 up from 14
    hex1(win, -36, 21, scale)
    # 16 up from ten o'clock
    hex1(win, -24, 28, scale)
    # 17 up from eleven o'clock
    hex1(win, -12, 35, scale)
    # 18 top
    hex1(win, 0, 42, scale)

    p0 = Point(XCENTER, YCENTER)
    p0.setFill("red")
    p0.setOutline("red")
    p0.draw(win)
    p1 = Point(XCENTER + 12 * scale, YCENTER + 7 * scale)
    l1 = Line(p0, p1)
    l1.setFill("red")
    l1.draw(win)
    win.getMouse()
    win.close()

main()

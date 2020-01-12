#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

from graphics import *

XSCALE = 2550
YSCALE = 1310
XCENTER = XSCALE / 2
YCENTER = YSCALE / 2

def hex1(win, xoffset, yoffset):
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset))
    p.draw(win)

def main():
    # win = GraphWin("test_%s_%s" % (str(xscale), str(yscale)), XSCALE, YSCALE)
    win = GraphWin("hex1", XSCALE, YSCALE)
    win.setCoords(0,0, XSCALE , YSCALE)

    # one side is 16 units long
    # height of vertical rectangle is 28
    # bulge to either side is 8

    # layer 0
    # center
    hex1(win, XCENTER, YCENTER)

    # layer 1
    # upper right
    hex1(win, XCENTER + 24, YCENTER + 14)
    # lower right
    hex1(win, XCENTER + 24, YCENTER - 14)
    # top
    hex1(win, XCENTER, YCENTER + 28)
    # bottom
    hex1(win, XCENTER, YCENTER - 28)
    # upper left
    hex1(win, XCENTER - 24, YCENTER + 14)
    # lower left
    hex1(win, XCENTER - 24, YCENTER - 14)

    # layer 2
    # one o'clock
    hex1(win, XCENTER + 24, YCENTER + 42)
    # two o'clock
    hex1(win, XCENTER + 48, YCENTER + 28)
    # three o'clock
    hex1(win, XCENTER + 48, YCENTER)
    # four o'clock
    hex1(win, XCENTER + 48, YCENTER - 28)
    # five o'clock
    hex1(win, XCENTER + 24, YCENTER - 42)
    # six o'clock
    hex1(win, XCENTER, YCENTER - 56)
    # seven o'clock
    hex1(win, XCENTER - 24, YCENTER - 42)
    # eight o'clock
    hex1(win, XCENTER - 48, YCENTER - 28)
    # nine o'clock
    hex1(win, XCENTER - 48, YCENTER)
    # ten o'clock
    hex1(win, XCENTER - 48, YCENTER + 28)
    # eleven o'clock
    hex1(win, XCENTER - 24, YCENTER + 42)
    # twelve o'clock
    hex1(win, XCENTER, YCENTER + 56)

    win.getMouse()
    win.close()

main()

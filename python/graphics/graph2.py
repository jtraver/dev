#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py

from graphics import *

SCALE = 10

def main():
    win = GraphWin("My Circle", 100 * SCALE, 100 * SCALE)
    c = Circle(Point(50 * SCALE,50 * SCALE), 10 * SCALE)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()

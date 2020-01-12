#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html

from graphics import *

SCALE = 20
SCALE2 = 200

def hex1(xscale, yscale):
    win = GraphWin("test_%s_%s" % (str(xscale), str(yscale)), 2550, 1310)
    # win = GraphWin("test_%s_%s" % (str(xscale), str(yscale)))
    win.setCoords(0,0, 2550 , 1310)
    # win.setCoords(0,0, 10,10)
    # t = Text(Point(5,5), "Centered Text")
    # t.draw(win)

    # center
    xoffset = 100
    yoffset = 100
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # upper right
    xoffset = 124
    yoffset = 114
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # lower right
    xoffset = 124
    yoffset = 86
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # top
    xoffset = 100
    yoffset = 128
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # bottom
    xoffset = 100
    yoffset = 72
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # upper left
    xoffset = 76
    yoffset = 114
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    # lower right
    xoffset = 76
    yoffset = 86
    p = Polygon(Point(8 + xoffset,0 + yoffset), Point(24 + xoffset,0 + yoffset), Point(32 + xoffset,14 + yoffset), Point(24 + xoffset, 28 + yoffset), Point(8 + xoffset, 28 + yoffset), Point(0 + xoffset, 14 + yoffset), Point(8 + xoffset, 0 + yoffset))
    p.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("My Circle", 100 * SCALE, 100 * SCALE)
    c = Circle(Point(50 * SCALE,50 * SCALE), 10 * SCALE)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def main():
    hex1(10, 10)
    # circle()

main()

def test():
    win = GraphWin()
    win.setCoords(0,0,10,10)
    t = Text(Point(5,5), "Centered Text")
    t.draw(win)
    p = Polygon(Point(1,1), Point(5,3), Point(2,7))
    p.draw(win)
    e = Entry(Point(5,6), 10)
    e.draw(win)
    win.getMouse()
    p.setFill("red")
    p.setOutline("blue")
    p.setWidth(2)
    s = ""
    for pt in p.getPoints():
        s = s + "(%0.1f,%0.1f) " % (pt.getX(), pt.getY())
    t.setText(e.getText())
    e.setFill("green")
    e.setText("Spam!")
    e.move(2,0)
    win.getMouse()
    p.move(2,3)
    s = ""
    for pt in p.getPoints():
        s = s + "(%0.1f,%0.1f) " % (pt.getX(), pt.getY())
    t.setText(s)
    win.getMouse()
    p.undraw()
    e.undraw()
    t.setStyle("bold")
    win.getMouse()
    t.setStyle("normal")
    win.getMouse()
    t.setStyle("italic")
    win.getMouse()
    t.setStyle("bold italic")
    win.getMouse()
    t.setSize(14)
    win.getMouse()
    t.setFace("arial")
    t.setSize(20)
    win.getMouse()
    win.close()

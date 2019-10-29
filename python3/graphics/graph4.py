#!/usr/bin/env python3
#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py

from graphics import *

SCALE = 10
SCALE2 = 100

def test():
    win = GraphWin("test", SCALE * SCALE2, SCALE * SCALE2)
    # win.setCoords(0,0, 10 * SCALE,10 * SCALE)
    win.setCoords(0,0, 10,10)
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


def circle():
    win = GraphWin("My Circle", 100 * SCALE, 100 * SCALE)
    c = Circle(Point(50 * SCALE,50 * SCALE), 10 * SCALE)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

def main():
    test()
    circle()

main()

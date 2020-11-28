#!/usr/bin/python

# http://mcsp.wartburg.edu/zelle/python/graphics.py
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics/index.html


import math

from graphics import *

XSCALE = 2550
YSCALE = 1310
XCENTER = XSCALE / 2
YCENTER = YSCALE / 2

# https://en.wikipedia.org/wiki/Incircle_and_excircles_of_a_triangle#Trilinear_coordinates
# {\displaystyle \left({\frac {ax_{a}+bx_{b}+cx_{c}}{a+b+c}},{\frac {ay_{a}+by_{b}+cy_{c}}{a+b+c}}\right)={\frac {a\left(x_{a},y_{a}\right)+b\left(x_{b},y_{b}\right)+c\left(x_{c},y_{c}\right)}{a+b+c}}.}
# {ax_{a}+bx_{b}+cx_{c}}{a+b+c}},{{ay_{a}+by_{b}+cy_{c}}{a+b+c}}

def circles5(win, scale):

    red1 = color_rgb(255, 0, 0)
    green1 = color_rgb(0, 255, 0)
    blue1 = color_rgb(0, 0, 255)
    print "red1 = %s" % str(red1)
    print "green1 = %s" % str(green1)
    print "blue1 = %s" % str(blue1)
    rb_magenta1 = color_rgb(255, 0, 255)
    gb_cyan1 = color_rgb(0, 255, 255)
    rg_yellow1 = color_rgb(255, 255, 0)

    rm_rose1 = color_rgb(255, 0, 127)
    bm_violet1 = color_rgb(127, 0, 255)
    bc_azure1 = color_rgb(0, 127, 255)
    gc_green1 = color_rgb(0, 255, 127)
    gy_chart1 = color_rgb(127, 255, 0)
    ry_orange1 = color_rgb(255, 127, 0)
    # red magenta blue cyan green yellow
    # rose violet azure spring-green chartreuse orange

    c0 = Circle(Point(XCENTER,YCENTER), 10 * scale)
    c0.setWidth(4)
    # c0.setWidth(10)
    # c0.setOutline(rm_rose1)
    # c0.setOutline(bm_violet1)
    # c0.setOutline(bc_azure1)
    # c0.setOutline(gc_green1)
    # c0.setOutline(gy_chart1)
    # c0.setOutline(ry_orange1)
    c0.draw(win)
    # https://en.wikipedia.org/wiki/Color_wheel
    # https://en.wikipedia.org/wiki/File:Color_star-en_(tertiary_names).svg

    # red purple blue green yellow orange
    # magenta, violet, teal, chartreuse, amber, vermilion
    # c0.setOutline("red")                  #FF0000
    # c0.setOutline("purple")               #A020F0
    # c0.setOutline("blue")                 #0000FF
    # c0.setOutline("green")                #00FF00
    # c0.setOutline("yellow")               #FFFF00
    # c0.setOutline("orange")               #FFA500
    # c0.setOutline("magenta")              #FF00FF
    # c0.setOutline("violet")
    # # c0.setOutline("teal")     # unknown     #008080  https://en.wikipedia.org/wiki/X11_color_names
    # c0.setOutline("chartreuse")
    # # c0.setOutline("amber")    # unknown
    # # c0.setOutline("vermilion")        # unknown

    # https://en.wikipedia.org/wiki/File:RBG_color_wheel.svg
    # red magenta blue cyan green yellow
    # rose violet azure spring-green chartreuse orange
    # c0.setOutline("red")                  #FF0000
    # c0.setOutline("magenta")              #FF00FF
    # c0.setOutline("blue")                 #0000FF
    # c0.setOutline("cyan")                 #00FFFF
    # c0.setOutline("green")                #00FF00
    # c0.setOutline("yellow")               #FFFF00
    # # c0.setOutline("rose")     # unknown
    # c0.setOutline("pink")                 #FFC0CB
    # c0.setOutline("violet")               #EE82EE
    # c0.setOutline("azure")                #F0FFFF
    # c0.setOutline("spring green")         #00FF7F
    # c0.setOutline("chartreuse")           #7FFF00
    # c0.setOutline("orange")               #FFA500

    radius1 = 10 * scale
    diameter1 = radius1 * 2
    npoints = 6
    inc1 = (math.pi * 2) / npoints
    theta1 = 0
    xs = []
    ys = []
    # color1 = ["red", "magenta", "blue", "cyan", "green", "yellow"]
    color1 = [red1, rb_magenta1, blue1, gb_cyan1, green1, rg_yellow1]
    for i1 in range(npoints):
        x1 = (math.sin(theta1) * diameter1) + XCENTER
        xs.append(x1)
        y1 = (math.cos(theta1) * diameter1) + YCENTER
        ys.append(y1)
        c1 = Circle(Point(x1, y1), 10 * scale)
        c1.setOutline(color1[i1])
        c1.setWidth(4)
        c1.draw(win)
        theta1 += inc1
    xa = XCENTER * diameter1
    ya = YCENTER * diameter1
    xb1 = xs[0] * diameter1
    yb1 = ys[0] * diameter1
    xc1 = xs[1] * diameter1
    yc1 = ys[1] * diameter1
    x1 = (xa + xb1 + xc1) / (3 * diameter1)
    y1 = (ya + yb1 + yc1) / (3 * diameter1)
    c1 = Circle(Point(x1, y1), 10 * scale)
    # c1.setOutline("pink")
    c1.setOutline(rm_rose1)
    c1.setWidth(4)
    c1.draw(win)

    xb2 = xs[2] * diameter1
    yb2 = ys[2] * diameter1
    xc2 = xs[3] * diameter1
    yc2 = ys[3] * diameter1
    x2 = (xa + xb2 + xc2) / (3 * diameter1)
    y2 = (ya + yb2 + yc2) / (3 * diameter1)
    c2 = Circle(Point(x2, y2), 10 * scale)
    # c2.setOutline("azure")
    c2.setOutline(bc_azure1)
    # c2.setWidth(10)
    c2.setWidth(4)
    c2.draw(win)

    # red magenta blue cyan green yellow
    # rose violet azure spring-green chartreuse orange
    xb3 = xs[4] * diameter1
    yb3 = ys[4] * diameter1
    xc3 = xs[5] * diameter1
    yc3 = ys[5] * diameter1
    x3 = (xa + xb3 + xc3) / (3 * diameter1)
    y3 = (ya + yb3 + yc3) / (3 * diameter1)
    c3 = Circle(Point(x3, y3), 10 * scale)
    # c3.setOutline(gc_green1)
    c3.setOutline(gy_chart1)
    c3.setWidth(4)
    c3.draw(win)

    ## rm_rose1 = color_rgb(255, 0, 127)
    # bm_violet1 = color_rgb(127, 0, 255)
    ## bc_azure1 = color_rgb(0, 127, 255)
    # gc_green1 = color_rgb(0, 255, 127)
    ## gy_chart1 = color_rgb(127, 255, 0)
    # ry_orange1 = color_rgb(255, 127, 0)
    # # red magenta blue cyan green yellow
    # # rose violet azure spring-green chartreuse orange

    xb4 = xs[5] * diameter1
    yb4 = ys[5] * diameter1
    xc4 = xs[0] * diameter1
    yc4 = ys[0] * diameter1
    x4 = (xa + xb4 + xc4) / (3 * diameter1)
    y4 = (ya + yb4 + yc4) / (3 * diameter1)
    c4 = Circle(Point(x4, y4), 10 * scale)
    # c4.setOutline(bm_violet1)
    # c4.setOutline(gc_green1)
    c4.setOutline(ry_orange1)
    c4.setWidth(4)
    c4.draw(win)

    xb5 = xs[1] * diameter1
    yb5 = ys[1] * diameter1
    xc5 = xs[2] * diameter1
    yc5 = ys[2] * diameter1
    x5 = (xa + xb5 + xc5) / (3 * diameter1)
    y5 = (ya + yb5 + yc5) / (3 * diameter1)
    c5 = Circle(Point(x5, y5), 10 * scale)
    c5.setOutline(bm_violet1)
    c5.setWidth(4)
    c5.draw(win)

    xb6 = xs[3] * diameter1
    yb6 = ys[3] * diameter1
    xc6 = xs[4] * diameter1
    yc6 = ys[4] * diameter1
    x6 = (xa + xb6 + xc6) / (3 * diameter1)
    y6 = (ya + yb6 + yc6) / (3 * diameter1)
    c6 = Circle(Point(x6, y6), 10 * scale)
    c6.setOutline(gc_green1)
    c6.setWidth(4)
    c6.draw(win)

def circles4(win, scale):
    c0 = Circle(Point(XCENTER,YCENTER), 10 * scale)
    c0.draw(win)
    radius1 = 10 * scale
    diameter1 = radius1 * 2
    npoints = 6
    inc1 = (math.pi * 2) / npoints
    theta1 = 0
    xs = []
    ys = []
    for i1 in range(npoints):
        x1 = (math.sin(theta1) * diameter1) + XCENTER
        xs.append(x1)
        y1 = (math.cos(theta1) * diameter1) + YCENTER
        ys.append(y1)
        c1 = Circle(Point(x1, y1), 10 * scale)
        c1.draw(win)
        theta1 += inc1
    xa = XCENTER * diameter1
    ya = YCENTER * diameter1
    xb1 = xs[0] * diameter1
    yb1 = ys[0] * diameter1
    xc1 = xs[1] * diameter1
    yc1 = ys[1] * diameter1
    x1 = (xa + xb1 + xc1) / (3 * diameter1)
    y1 = (ya + yb1 + yc1) / (3 * diameter1)
    c1 = Circle(Point(x1, y1), 10 * scale)
    c1.draw(win)
    xb2 = xs[2] * diameter1
    yb2 = ys[2] * diameter1
    xc2 = xs[3] * diameter1
    yc2 = ys[3] * diameter1
    x2 = (xa + xb2 + xc2) / (3 * diameter1)
    y2 = (ya + yb2 + yc2) / (3 * diameter1)
    c2 = Circle(Point(x2, y2), 10 * scale)
    c2.draw(win)
    xb3 = xs[4] * diameter1
    yb3 = ys[4] * diameter1
    xc3 = xs[5] * diameter1
    yc3 = ys[5] * diameter1
    x3 = (xa + xb3 + xc3) / (3 * diameter1)
    y3 = (ya + yb3 + yc3) / (3 * diameter1)
    c3 = Circle(Point(x3, y3), 10 * scale)
    c3.draw(win)
    xb4 = xs[5] * diameter1
    yb4 = ys[5] * diameter1
    xc4 = xs[0] * diameter1
    yc4 = ys[0] * diameter1
    x4 = (xa + xb4 + xc4) / (3 * diameter1)
    y4 = (ya + yb4 + yc4) / (3 * diameter1)
    c4 = Circle(Point(x4, y4), 10 * scale)
    c4.draw(win)
    xb5 = xs[1] * diameter1
    yb5 = ys[1] * diameter1
    xc5 = xs[2] * diameter1
    yc5 = ys[2] * diameter1
    x5 = (xa + xb5 + xc5) / (3 * diameter1)
    y5 = (ya + yb5 + yc5) / (3 * diameter1)
    c5 = Circle(Point(x5, y5), 10 * scale)
    c5.draw(win)
    xb6 = xs[3] * diameter1
    yb6 = ys[3] * diameter1
    xc6 = xs[4] * diameter1
    yc6 = ys[4] * diameter1
    x6 = (xa + xb6 + xc6) / (3 * diameter1)
    y6 = (ya + yb6 + yc6) / (3 * diameter1)
    c6 = Circle(Point(x6, y6), 10 * scale)
    c6.draw(win)

def circles3(win, scale):
    c0 = Circle(Point(XCENTER,YCENTER), 10 * scale)
    c0.draw(win)
    radius1 = 10 * scale
    diameter1 = radius1 * 2
    npoints = 6
    inc1 = (math.pi * 2) / npoints
    theta1 = 0
    xs = []
    ys = []
    for i1 in range(npoints):
        x1 = (math.sin(theta1) * diameter1) + XCENTER
        xs.append(x1)
        y1 = (math.cos(theta1) * diameter1) + YCENTER
        ys.append(y1)
        c1 = Circle(Point(x1, y1), 10 * scale)
        c1.draw(win)
        theta1 += inc1
    xa = XCENTER * diameter1
    ya = YCENTER * diameter1
    xb1 = xs[0] * diameter1
    yb1 = ys[0] * diameter1
    xc1 = xs[1] * diameter1
    yc1 = ys[1] * diameter1
    x1 = (xa + xb1 + xc1) / (3 * diameter1)
    y1 = (ya + yb1 + yc1) / (3 * diameter1)
    c1 = Circle(Point(x1, y1), 10 * scale)
    c1.draw(win)
    xb2 = xs[2] * diameter1
    yb2 = ys[2] * diameter1
    xc2 = xs[3] * diameter1
    yc2 = ys[3] * diameter1
    x2 = (xa + xb2 + xc2) / (3 * diameter1)
    y2 = (ya + yb2 + yc2) / (3 * diameter1)
    c2 = Circle(Point(x2, y2), 10 * scale)
    c2.draw(win)
    xb3 = xs[4] * diameter1
    yb3 = ys[4] * diameter1
    xc3 = xs[5] * diameter1
    yc3 = ys[5] * diameter1
    x3 = (xa + xb3 + xc3) / (3 * diameter1)
    y3 = (ya + yb3 + yc3) / (3 * diameter1)
    c3 = Circle(Point(x3, y3), 10 * scale)
    c3.draw(win)

def circles2(win, scale):
    c0 = Circle(Point(XCENTER,YCENTER), 10 * scale)
    c0.draw(win)
    radius1 = 10 * scale
    diameter1 = radius1 * 2
    # c1 = Circle(Point(XCENTER + diameter1,YCENTER), 10 * scale)
    # c1.draw(win)
    # c2 is at 60 degrees, same diameter
    npoints = 6
    inc1 = (math.pi * 2) / npoints
    # inc1 = (math.pi) / npoints
    theta1 = 0
    # x2 = (math.sin(theta1) * diameter1) + XCENTER
    # y2 = (math.cos(theta1) * diameter1) + YCENTER
    # c2 = Circle(Point(x2, y2), 10 * scale)
    # c2.draw(win)
    # theta1 += inc1
    # x3 = (math.sin(theta1) * diameter1) + XCENTER
    # y3 = (math.cos(theta1) * diameter1) + YCENTER
    # c3 = Circle(Point(x3, y3), 10 * scale)
    # c3.draw(win)
    for i1 in range(npoints):
        x1 = (math.sin(theta1) * diameter1) + XCENTER
        y1 = (math.cos(theta1) * diameter1) + YCENTER
        c1 = Circle(Point(x1, y1), 10 * scale)
        c1.draw(win)
        theta1 += inc1
    #for i1 in range(npoints):
    #    x1 = (math.sin(theta1) * radius) + xoffset
    #    y1 = (math.cos(theta1) * radius) + yoffset
    #    hex1(win, x1, y1, scale)
    #    theta1 += inc1

def circles1(win, xoffset, yoffset, scale = 1.0):
    sxoffset = xoffset * scale + XCENTER
    syoffset = yoffset * scale + YCENTER
    #p = Polygon(
    #    Point(-4 * scale + sxoffset, -7 * scale + syoffset),
    #    Point( 4 * scale + sxoffset, -7 * scale + syoffset),
    #    Point( 8 * scale + sxoffset,  0 * scale + syoffset),
    #    Point( 4 * scale + sxoffset,  7 * scale + syoffset),
    #    Point(-4 * scale + sxoffset,  7 * scale + syoffset),
    #    Point(-8 * scale + sxoffset,  0 * scale + syoffset))
    #p.draw(win)
    # c = Circle(Point(50 * SCALE,50 * SCALE), 10 * SCALE)
    c = Circle(Point(XCENTER,YCENTER), 10 * scale)
    c.draw(win)
    c1 = Circle(Point(-4 * scale + sxoffset, -7 * scale + syoffset), 10 * scale)
    c1.draw(win)
    c2 = Circle(Point( 4 * scale + sxoffset, -7 * scale + syoffset), 10 * scale)
    c2.draw(win)
    c3 = Circle(Point( 8 * scale + sxoffset,  0 * scale + syoffset), 10 * scale)
    c3.draw(win)
    c4 = Circle(Point( 4 * scale + sxoffset,  7 * scale + syoffset), 10 * scale)
    c4.draw(win)
    c5 = Circle(Point(-4 * scale + sxoffset,  7 * scale + syoffset), 10 * scale)
    c5.draw(win)
    c6 = Circle(Point(-8 * scale + sxoffset,  0 * scale + syoffset), 10 * scale)
    c6.draw(win)


def main():
    radius = 500.0
    # scale = 0.5
    scale = 10.0
    win = GraphWin("circle1", XSCALE, YSCALE)
    win.setCoords(0,0, XSCALE , YSCALE)
    # one side is 8 units long
    # height of vertical rectangle is 14
    # bulge to either side is 4

    # 1 -> 1
    # layer 0
    # center
    # circle1(win, 0, 0, scale, radius)
    # circles1(win, 0, 0, scale)
    # circles2(win, scale)
    # circles3(win, scale)
    # circles4(win, scale)
    circles5(win, scale)

    # p0 = Point(XCENTER, YCENTER)
    # p0.setFill("red")
    # p0.setOutline("red")
    # p0.draw(win)
    # p1 = Point(XCENTER + 12 * scale, YCENTER + 7 * scale)
    # l1 = Line(p0, p1)
    # l1.setFill("red")
    # l1.draw(win)

    # t = Text(Point(XCENTER,YCENTER), "0")
    # t.draw(win)

    win.getMouse()
    win.close()


# https://math.stackexchange.com/questions/260096/find-the-coordinates-of-a-point-on-a-circle
# x = rsin(theta), y = rcos(theta)
def circle1(win, xoffset, yoffset, scale = 1.0, radius = 10.0):
    hex1(win, xoffset, yoffset, scale)
    # theta is degrees or radians?
    npoints = 10
    npoints = 1
    npoints = 100
    inc1 = (math.pi * 2) / npoints
    theta1 = 0.0
    for i1 in range(npoints):
        x1 = (math.sin(theta1) * radius) + xoffset
        y1 = (math.cos(theta1) * radius) + yoffset
        hex1(win, x1, y1, scale)
        theta1 += inc1


# math = <module 'math' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'>
# acos       acos(x) Return the arc cosine (measured in radians) of x.
# acosh      acosh(x) Return the inverse hyperbolic cosine of x.
# asin       asin(x) Return the arc sine (measured in radians) of x.
# asinh      asinh(x) Return the inverse hyperbolic sine of x.
# atan       atan(x) Return the arc tangent (measured in radians) of x.
# atan2      atan2(y, x) Return the arc tangent (measured in radians) of y/x. Unlike atan(y/x), the signs of both x and y are considered.
# atanh      atanh(x) Return the inverse hyperbolic tangent of x.
# ceil       ceil(x) Return the ceiling of x as a float. This is the smallest integral value >= x.
# copysign   copysign(x, y) Return x with the sign of y.
# cos        cos(x) Return the cosine of x (measured in radians).
# cosh       cosh(x) Return the hyperbolic cosine of x.
# degrees    degrees(x) Convert angle x from radians to degrees.
# erf        erf(x) Error function at x.
# erfc       erfc(x) Complementary error function at x.
# exp        exp(x) Return e raised to the power of x.
# expm1      expm1(x) Return exp(x)-1. This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
# fabs       fabs(x) Return the absolute value of the float x.
# factorial  factorial(x) -> Integral Find x!. Raise a ValueError if x is negative or non-integral.
# floor      floor(x) Return the floor of x as a float. This is the largest integral value <= x.
# fmod       fmod(x, y) Return fmod(x, y), according to platform C. x % y may differ.
# frexp      frexp(x) Return the mantissa and exponent of x, as pair (m, e). m is a float and e is an int, such that x = m * 2.**e. If x is 0, m and e are both 0. Else 0.5 <= abs(m) < 1.0.
# fsum       fsum(iterable) Return an accurate floating point sum of values in the iterable. Assumes IEEE-754 floating point arithmetic.
# gamma      gamma(x) Gamma function at x.
# hypot      hypot(x, y) Return the Euclidean distance, sqrt(x*x + y*y).
# isinf      isinf(x) -> bool Check if float x is infinite (positive or negative).
# isnan      isnan(x) -> bool Check if float x is not a number (NaN).
# ldexp      ldexp(x, i) Return x * (2**i).
# lgamma     lgamma(x) Natural logarithm of absolute value of Gamma function at x.
# log        log(x[, base]) Return the logarithm of x to the given base. If the base not specified, returns the natural logarithm (base e) of x.
# log10      log10(x) Return the base 10 logarithm of x.
# log1p      log1p(x) Return the natural logarithm of 1+x (base e). The result is computed in a way which is accurate for x near zero.
# modf       modf(x) Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
# pow        pow(x, y) Return x**y (x to the power of y).
# radians    radians(x) Convert angle x from degrees to radians.
# sin        sin(x) Return the sine of x (measured in radians).
# sinh       sinh(x) Return the hyperbolic sine of x.
# sqrt       sqrt(x) Return the square root of x.
# tan        tan(x) Return the tangent of x (measured in radians).
# tanh       tanh(x) Return the hyperbolic tangent of x.
# trunc      trunc(x:Real) -> Integral Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.
# math.pi = 3.14159265359
# math.e = 2.71828182846
# phi = 1.61803398875


        

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

def old_main():
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

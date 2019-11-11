#!/usr/bin/python

def main():
    iching1()

def iching1():
    itob = []
    itob.append(None)
    itob.append(63)
    itob.append(0)
    itob.append(17)
    itob.append(34)
    itob.append(23)
    itob.append(58)
    itob.append(2)
    itob.append(16)
    itob.append(55)
    itob.append(59)
    itob.append(7)
    itob.append(56)
    itob.append(61)
    itob.append(47)
    itob.append(4)
    itob.append(8)
    itob.append(25)
    itob.append(38)
    itob.append(3)
    itob.append(48)
    itob.append(41)
    itob.append(37)
    itob.append(32)
    itob.append(1)
    itob.append(57)
    itob.append(39)
    itob.append(33)
    itob.append(30)
    itob.append(18)
    itob.append(45)
    itob.append(28)
    itob.append(14)
    itob.append(60)
    itob.append(15)
    itob.append(40)
    itob.append(5)
    itob.append(53)
    itob.append(43)
    itob.append(20)
    itob.append(10)
    itob.append(35)
    itob.append(49)
    itob.append(31)
    itob.append(62)
    itob.append(24)
    itob.append(6)
    itob.append(26)
    itob.append(22)
    itob.append(29)
    itob.append(46)
    itob.append(9)
    itob.append(36)
    itob.append(52)
    itob.append(11)
    itob.append(13)
    itob.append(44)
    itob.append(54)
    itob.append(27)
    itob.append(50)
    itob.append(19)
    itob.append(51)
    itob.append(12)
    itob.append(21)
    itob.append(42)
    btoi = []
    for h1 in xrange(65):
        icount = 0
        for itob1 in itob:
            if itob1 == h1:
                btoi.append(icount)
                break
            icount += 1
    for hexagram in xrange(64):
        btoi1 = btoi[hexagram]
        print "\n%s %s" % (str(hexagram), str(btoi1))
        print_hexagram(hexagram)

def print_hexagram(hexagram):
    h1 = hexagram
    l6 = h1 / 32
    h1 %= 32
    l5 = h1 / 16
    h1 %= 16
    l4 = h1 / 8
    h1 %= 8
    l3 = h1 / 4
    h1 %= 4
    l2 = h1 / 2
    h1 %= 2
    l1 = h1
    if l6:
        print "---"
    else:
        print "- -"
    if l5:
        print "---"
    else:
        print "- -"
    if l4:
        print "---"
    else:
        print "- -"
    if l3:
        print "---"
    else:
        print "- -"
    if l2:
        print "---"
    else:
        print "- -"
    if l1:
        print "---"
    else:
        print "- -"


main()

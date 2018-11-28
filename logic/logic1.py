#!/usr/bin/python

# bools = [False, True]
bools = [0, 1]

def main():
    s1_6e2p35()

def s1_6e2p35():
    fail = 0
    for P in bools:
        for Q in bools:
            for R in bools:
                result = get_circuit(P, Q, R)
                print "P %s  Q %s  R %s  result %s" % (str(P), str(Q), str(R), str(result))
                check = get_check(P, Q, R)
                if result == check:
                    pass
                else:
                    fail += 1
                    print "FAIL P %s  Q %s  R %s  result %s   check %s" % (str(P), str(Q), str(R), str(result), str(check))
    if fail == 0:
        print "PASS"
    else:
        print "FAIL"
    print "DONE"

def get_circuit(P, Q, R):
    print "P %s  Q %s  R %s" % (str(P), str(Q), str(R))
    notP = 1
    if P:
        notP = 0
    notQ = 1
    if Q:
        notQ = 0
    print "P %s  Q %s  R %s  notP %s  notQ %s" % (str(P), str(Q), str(R), str(notP), str(notQ))
    notPornotQ = 0
    if notP or notQ:
        notPornotQ = 1
    print "P %s  Q %s  R %s  notP %s  notQ %s  notPornotQ %s" % (str(P), str(Q), str(R), str(notP), str(notQ), str(notPornotQ))
    notPornotQandnotP = 0
    if notPornotQ and notP:
        notPornotQandnotP = 1
    print "P %s  Q %s  R %s  notP %s  notQ %s  notPornotQ %s  notPornotQandnotP %s" % (str(P), str(Q), str(R), str(notP), str(notQ), str(notPornotQ), str(notPornotQandnotP))
    notPornotQandR = 0
    if notPornotQ and R:
        notPornotQandR = 1
    print "P %s  Q %s  R %s  notP %s  notQ %s  notPornotQ %s  notPornotQandnotP %s  notPornotQandR %s" % (str(P), str(Q), str(R), str(notP), str(notQ), str(notPornotQ), str(notPornotQandnotP), str(notPornotQandR))
    notPornotQandnotPornotPornotQandR = 0
    if notPornotQandnotP or notPornotQandR:
        notPornotQandnotPornotPornotQandR = 1
    print "P %s  Q %s  R %s  notP %s  notQ %s  notPornotQ %s  notPornotQandnotP %s  notPornotQandR %s  notPornotQandnotPornotPornotQandR %s" % (str(P), str(Q), str(R), str(notP), str(notQ), str(notPornotQ), str(notPornotQandnotP), str(notPornotQandR), str(notPornotQandnotPornotPornotQandR))
    return notPornotQandnotPornotPornotQandR

def get_check(P, Q, R):
    notP = 1
    if P:
        notP = 0
    notQ = 1
    if Q:
        notQ = 0
    if notP or (R and notQ):
        return 1
    return 0

main()

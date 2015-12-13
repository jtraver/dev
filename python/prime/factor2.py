#!/usr/bin/python

limit = 1002
primes = []
dprimes = {}

def is_prime(pc):
    if pc in dprimes:
        return True
    if pc < 0:
        return False
    prime = True
    if pc < 1:
        return prime
    for idiv in xrange(1, len(primes)):
        div = primes[idiv]
        if div * div > pc:
            break
        if pc % div == 0:
            return False
    if prime and not pc in dprimes:
        primes.append(pc)
        dprimes[pc] = 1
    return prime

def main():
    p = 100.00
    l = 10
    is_prime(1)
    # for pc in xrange(2, limit):
    pc = 2
    while 1:
        if is_prime(pc):
            r = p / pc
            p -= r
            # print "%s %s %s" % (str(pc), str(r), str(p))
        if pc > l:
            l *= 10
            print "%s %s %s" % (str(pc), str(r), str(p))
        pc += 1

main()

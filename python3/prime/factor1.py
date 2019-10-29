#!/usr/bin/env python3
#!/usr/bin/python

limit = 100000001
primes = []
dprimes = {}
factors = {}

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
            # print "found %s in %s" % (str(div), str(pc))
            if div in factors:
                factors[div] += 1
            else:
                factors[div] = 1
            return False
    if prime and not pc in dprimes:
        primes.append(pc)
        dprimes[pc] = 1
    return prime

def main():
    for pc in xrange(1, limit):
        if is_prime(pc):
            # print "%s is prime" % str(pc)
            pass
        else:
            continue
    total = 0
    print
    for pc in primes:
        if pc in factors:
            count = factors[pc]
            total += count
            print "%s %s" % (str(pc), str(count))
    print "%s total" % str(total)

main()

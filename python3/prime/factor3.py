#!/usr/bin/env python3
#!/usr/bin/python

limit = 1000001
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
    for idiv in range(1, len(primes)):
        div = primes[idiv]
        if div * div > pc:
            break
        if pc % div == 0:
            # print "found %s in %s" % (str(div), str(pc))
            if div in factors:
                factors[div].append(pc)
            else:
                factors[div] = [pc]
            return False
    if prime and not pc in dprimes:
        primes.append(pc)
        dprimes[pc] = 1
    return prime

def main():
    for pc in range(1, limit):
        if is_prime(pc):
            # print "%s is prime" % str(pc)
            pass
        else:
            continue
    total = 0
    print()
    index = 0
    for pc in primes:
        index += 1
        if pc in factors:
            count = len(factors[pc])
            total += count
            if count < 20:
                print("%s %s %s" % (str(pc), str(count), factors[pc]))
            elif index < len(primes):
                slice1 = factors[pc][0:10]
                print("%s %s %s..." % (str(pc), str(count), slice1))
            else:
                print("%s %s [%s, ...]" % (str(pc), str(count), pc * pc))
    print("%s total" % str(total))

main()

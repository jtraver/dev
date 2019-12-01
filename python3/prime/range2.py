#!/usr/bin/env python3
#!/usr/bin/python

limit = 100000
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
    for idiv in range(1, len(primes)):
        div = primes[idiv]
        if div * div > pc:
            break
        if pc % div == 0:
            prime = False
    if prime and not pc in dprimes:
        primes.append(pc)
        dprimes[pc] = 1
    return prime

def main():
    maxpair = 0
    maxlower = -2
    intlower = 0
    for pc in range(1, limit, 2):
        if is_prime(pc):
            print("%s is prime" % str(pc))
        else:
            continue
        lower = pc - 2
        upper = pc + 2
        paircount = 0
        lastlower = -2
        while lower >= 0:
            if is_prime(lower) and is_prime(upper):
                print("  %s + %s" % (str(lower), str(upper)))
                paircount += 1
                lastlower = lower
            lower -= 2
            upper += 2
        print("    %s pairs for %s" % (str(paircount), str(pc)))
        if paircount < intlower:
            intlower = paircount
            print("      new interim lower %s for %s (last max %s)" % (intlower, str(pc), str(maxpair)))
        if paircount > maxpair:
            maxpair = paircount
            print("      new max pairs %s for %s" % (maxpair, str(pc)))
            intlower = maxpair
        if lastlower > maxlower:
            maxlower = lastlower
            print("      new max lower %s for %s" % (maxlower, str(pc)))

main()

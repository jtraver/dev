#!/usr/bin/env python3
#!/usr/bin/python

limit = 10000

primes = [ 2 ]

def is_prime(candi):
    for i1 in range(0, len(primes)):
        p1 = primes[i1]
        if p1 * p1 > candi:
            break
        if candi % p1 == 0:
            return False
    return True

for c1 in range(3, limit, 2):
    if is_prime(c1):
        primes.append(c1)
        print("primes.append((%d, %d))" % (c1, c1))

print("%s" % str(primes))

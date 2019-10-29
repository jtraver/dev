#!/usr/bin/env python3
#!/usr/bin/python

limit = 1000000

primes = [ 2 ]
lens = []

def is_prime(candi):
    for i1 in range(0, len(primes)):
        p1 = primes[i1]
        if p1 * p1 > candi:
            break
        if candi % p1 == 0:
            return False
    return True

for i1 in range(0, 10):
    lens.append(0)

lens[1] = 1

for c1 in range(3, limit, 2):
    if is_prime(c1):
        primes.append(c1)
        # print "%d" % c1
        lens[len(str(c1))] += 1

# print "%s" % str(primes)
print "%s" % str(lens)

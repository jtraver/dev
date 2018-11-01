#!/usr/bin/python

# 1.61803398875 * 0.61803398875

def main():
    phi1 = phi()
    print "phi1 = %s" % str(phi1)
    print "1.61803398875 * 0.61803398875"

def phi():
    print "phi"
    expected = 1.0
    guess = 1.0
    result = guess1(guess)
    count = 0
    step = 0.1
    limit = 10000
    last = 0.0
    # while count < limit and result != expected:
    while count < limit and last != guess:
        last = guess
        count += 1
        if result > expected:
            guess -= step
        else:
            guess += step
        result = guess1(guess)
        if count % 10 == 0:
            print "%s result = %s, guess = %s" % (str(count), str(result), str(guess))
            step /= 10.0
    print "%s result = %s, guess = %s" % (str(count), str(result), str(guess))
    return guess

def guess1(guess):
    return guess * (guess + 1.0)

main()

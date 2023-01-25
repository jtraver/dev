#!/usr/bin/env python3

def main():
    total = 0
    for loop in range(10000):
        total += loop
        print("%s %s" % (str(loop), str(total)))
        if total > 86400:
            break
        
        

main()

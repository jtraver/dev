#!/usr/bin/env python3

# https://www.youtube.com/watch?v=sVKuaZjG56A

def main():
    for a in range(20):
        b = 20 - a
        max = a * a * b
        print("a = %s, b = %s, max = %s" % (str(a), str(b), str(max)))

main()

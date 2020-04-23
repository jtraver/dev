#!/usr/bin/env python3
#!/usr/bin/python

def main():
    int1()

def int1():
    s = 9223372036854775807
    print("%s" % str(s))
    for _ in range(30):
        s *= 2
        print("%s" % str(s))
    s *= 2
    print("%s" % str(s))
        
main()

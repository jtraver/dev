#!/usr/bin/env python3
#!/usr/bin/python

import psutil

def main():
    count = 0
    for proc in psutil.process_iter():
        count += 1
        print("%s proc = %s" % (str(count), str(proc)))

main()

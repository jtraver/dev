#!/usr/bin/env python3

# import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


## We can use a with statement to ensure threads are cleaned up promptly
#with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#    # Start the load operations and mark each future with its URL
#    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
#    for future in concurrent.futures.as_completed(future_to_url):
#        url = future_to_url[future]
#        try:
#            data = future.result()
#        except Exception as exc:
#            print('%r generated an exception: %s' % (url, exc))
#        else:
#            print('%r page is %d bytes' % (url, len(data)))

def test1():
    pass

def test2():
    return "test2"

def test3():
    raise Exception("test3 exception");

def test4():
    return True

def test5():
    return False

def test6():
    return None

def main():
    with ThreadPoolExecutor(max_workers=15) as executor:
        ex1 = executor.submit(test1)
        ex2 = executor.submit(test2)
        # ex3 = executor.submit(test3)
        ex4 = executor.submit(test4)
        ex5 = executor.submit(test5)
        ex6 = executor.submit(test6)
        print("ex1.result = %s" % str(ex1.result()))
        print("ex2.result = %s" % str(ex2.result()))
        # print("ex3.result = %s" % str(ex3.result()))
        print("ex4.result = %s" % str(ex4.result()))
        print("ex5.result = %s" % str(ex5.result()))
        print("ex6.result = %s" % str(ex6.result()))

main()

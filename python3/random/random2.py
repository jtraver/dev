#!/usr/bin/env python3

import random
import sys

def main():
    min = 0
    max = 2
    bl = 8
    while True:
        i1 = next(integer(min, max))
        l1 = int.bit_length(i1)
        if bl == l1:
            lb = int(bl / 8)
            print("byte %s, len = %s, min = %s, max = %s, i1 = %s" % (str(lb), str(l1), str(min), str(max), str(i1)))
            bl += 8
        else:
            # print("len = %s, min = %s, max = %s, i1 = %s" % (str(l1), str(min), str(max), str(i1)))
            pass
        min = max
        max *= 2
        if max > sys.maxsize * 1024:
            break

#byte 1, len = 8, min = 128, max = 256, i1 = 128
#byte 2, len = 16, min = 32768, max = 65536, i1 = 40382
#byte 3, len = 24, min = 8388608, max = 16777216, i1 = 15109634
#byte 4, len = 32, min = 2147483648, max = 4294967296, i1 = 3360559552
#byte 5, len = 40, min = 549755813888, max = 1099511627776, i1 = 844347915395
#byte 6, len = 48, min = 140737488355328, max = 281474976710656, i1 = 147538344814960
#byte 7, len = 56, min = 36028797018963968, max = 72057594037927936, i1 = 53206000906397931
#byte 8, len = 64, min = 9223372036854775808, max = 18446744073709551616, i1 = 10130302800993389589
#byte 9, len = 72, min = 2361183241434822606848, max = 4722366482869645213696, i1 = 4607965403856788518529

# # len1 = random.randint(0, max_byte_array)
# # byte = random.randint(0, 255)
# # nbins = random.randint(0, max_list)
# # dtype = random.randint(0, 2)
# # htype = random.randint(0, len(basic) - 1)
# # dtype = random.randint(0, len(hashable) - 1)
# # dtype = random.randint(0, 1)
# # val = random.random() * random.randint(1, 100000)
# # val = random.randint(1, 100000)
# # nbins = random.randint(0, max_list)
# # dtype = random.randint(0, len(types) - 1)
# # nbins = random.randint(0, max_dict)
# # dtype = random.randint(0, len(basic) - 1)
# # nbins = random.randint(0, max_string)
# # random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # ))
# # nbins = random.randint(0, max_unicode)
# # u = unichr(random.randint(0, max_unicode_char))
# # c = random.randint(0, 1)
# # u = u + unichr(random.randint(0, max_unicode_char))
# # u = u + unichr(random.randint(0xd800, 0xdbff))
# # u = u + unichr(random.randint(0xdc00, 0xdfff))
# # dtype = random.randint(0, 1)
# # val = random.random() * random.randint(1, 100000)
# # val = random.randint(1, 100000)
# # btype = random.randint(0, 32)
# # nbins = random.randint(0, tot_bins)
# # dtype = random.randint(0, 2)
# # htype = random.randint(0, len(basic) - 1)
# 

def check_len():
    while True:
        a = random.randint(1000000000, 4000000000)
        b = random.randint(0, 4000000000)
        print("a = %s 0x%lx" % (str(a), a))
        print("b = %s 0x%lx" % (str(b), b))
        c = a << 32 | b
        print("c = %s 0x%lx" % (str(c), c))
        len1 = len(str("%lx" % c))
        print("len1 = %s" % str(len1))
        if len1 != 16:
            break


def integer(min=0, max=sys.maxsize, step=1, rand=True):
    """Generates an integer within specified range.

    :param min:     The minimum integer value to be generated.
    :param max:     The maximum integer value to be generated.
    :param rand:    If true, generate random values in the given range.
    """
    if rand:
        while True:
            i = random.randrange(min, max)
            yield i
    else:
        for i in range(min, max, step):
            yield i


main()

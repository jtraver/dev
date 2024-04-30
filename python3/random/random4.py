#!/usr/bin/env python3

import random
import sys

def main():

    n_bytes = 1
    min_bits = 0
    n_bits = n_bytes * 8
    in1 = n_byte_integer(n_bytes)
    l1 = int.bit_length(in1)
    if l1 > n_bits or l1 < min_bits:
        print("n_bytes = %s, n_bits = %s, l1 = %s, in1 = %s" % (str(n_bytes), str(n_bits), str(l1), str(in1)))

    n_bytes = 2
    min_bits = n_bits + 1
    n_bits = n_bytes * 8
    in1 = n_byte_integer(n_bytes)
    l1 = int.bit_length(in1)
    if l1 > n_bits or l1 < min_bits:
        print("n_bytes = %s, n_bits = %s, l1 = %s, in1 = %s" % (str(n_bytes), str(n_bits), str(l1), str(in1)))

    for ix1 in range(100):
        min_bits = 0
        for n_bytes in range(1, 10):
            n_bits = n_bytes * 8
            in1 = n_byte_integer(n_bytes)
            l1 = int.bit_length(in1)
            if l1 > n_bits or l1 < min_bits:
                print("n_bytes = %s, n_bits = %s, l1 = %s, in1 = %s" % (str(n_bytes), str(n_bits), str(l1), str(in1)))
            min_bits = n_bits + 1

    for ix1 in range(100):
        i1 = one_byte()
        l1 = int.bit_length(i1)
        if l1 > 8 or l1 < 0:
            print("l1 = %s, i1 = %s" % (str(l1), str(i1)))

        i2 = two_bytes()
        l2 = int.bit_length(i2)
        if l2 > 16 or i2 < 9:
            print("l2 = %s, i2 = %s" % (str(l2), str(i2)))

        i3 = three_bytes()
        l3 = int.bit_length(i3)
        if l3 > 24 or i3 < 17:
            print("l3 = %s, i3 = %s" % (str(l3), str(i3)))

        i4 = four_bytes()
        l4 = int.bit_length(i4)
        if l4 > 32 or i4 < 25:
            print("l4 = %s, i4 = %s" % (str(l4), str(i4)))

        i5 = five_bytes()
        l5 = int.bit_length(i5)
        if l5 > 40 or l5 < 33:
            print("l5 = %s, i5 = %s" % (str(l5), str(i5)))

        i6 = six_bytes()
        l6 = int.bit_length(i6)
        if l6 > 48 or l6 < 41:
            print("l6 = %s, i6 = %s" % (str(l6), str(i6)))

        i7 = seven_bytes()
        l7 = int.bit_length(i7)
        if l7 > 56 or l7 < 49:
            print("l7 = %s, i7 = %s" % (str(l7), str(i7)))

        i8 = eight_bytes()
        l8 = int.bit_length(i8)
        if l8 > 64 or l8 < 57:
            print("l8 = %s, i8 = %s" % (str(l8), str(i8)))

        i9 = nine_bytes()
        l9 = int.bit_length(i9)
        if l9 > 72 or l9 < 65:
            print("l9 = %s, i9 = %s" % (str(l9), str(i9)))

        i10 = ten_bytes()
        l10 = int.bit_length(i10)
        if l10 > 80 or l10 < 73:
            print("l10 = %s, i10 = %s" % (str(l10), str(i10)))

    byte = 256
    for x1 in range(1, 10):
        print("x1 = %s, byte = %s" % (str(x1), str(byte)))
        byte *= 256

# x1 = 1, byte = 256
# x1 = 2, byte = 65536
# x1 = 3, byte = 16777216
# x1 = 4, byte = 4294967296
# x1 = 5, byte = 1099511627776
# x1 = 6, byte = 281474976710656
# x1 = 7, byte = 72057594037927936
# x1 = 8, byte = 18446744073709551616
# x1 = 9, byte = 4722366482869645213696

def n_byte_integer(n_bytes):
    min = 0
    max = 256
    for _ in range(1, n_bytes):
        min = max
        max *= 256
    return next(integer(min, max))

def one_byte():
    return next(integer(0, 256))

def two_bytes():
    return next(integer(256, 256 * 256))

def three_bytes():
    min = 256 * 256
    max = min * 256
    return next(integer(min, max))

def four_bytes():
    min = 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def five_bytes():
    min = 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def six_bytes():
    min = 256 * 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def seven_bytes():
    min = 256 * 256 * 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def eight_bytes():
    min = 256 * 256 * 256 * 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def nine_bytes():
    min = 256 * 256 * 256 * 256 * 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def ten_bytes():
    min = 256 * 256 * 256 * 256 * 256 * 256 * 256 * 256 * 256
    max = min * 256
    return next(integer(min, max))

def old_main():
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

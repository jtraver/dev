#!/usr/bin/env python3
#!/usr/bin/python


def get_value(s):
    if s == "true":
        return True
    if s == "false":
        return False
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def main():
    str1 = '1'
    val1 = get_value(str1)
    print("val1 = %s" % str(val1))
    print("val1 = %s" % str(type(val1)))
    str1 = '1.2'
    val1 = get_value(str1)
    print("val1 = %s" % str(val1))
    print("val1 = %s" % str(type(val1)))
    float1 = 1.211111111111111111111111111111111111111111111111111111111111111111111111111111111
    print("float1 = %s" % str(float1))
    print("float1 = %s" % str(type(float1)))
    str1 = '1.211111111111111111111111111111111111111111111111111111111111111111111111111111111'
    val1 = get_value(str1)
    print("val1 = %s" % str(val1))
    print("val1 = %s" % str(type(val1)))
    str1 = 'a string'
    val1 = get_value(str1)
    print("val1 = %s" % str(val1))
    print("val1 = %s" % str(type(val1)))


main()

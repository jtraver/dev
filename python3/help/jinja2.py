#!/usr/bin/env python3
#!/usr/bin/python

import jinja2

elements = {
}


def do_dir(object):
    attrs = []
    for e in dir(object):
        if '__' in e:
            continue
        attr = getattr(object, e)
        if type(attr) == int or type(attr) == str or 'NoneType' in str(type(attr)):
            continue
        attrs.append(e)
    return attrs


def check(object, name, dict1, status):
    attrs1 = do_dir(object)
    for e1 in attrs1:
        attr1 = getattr(object, e1)
        if e1 in dict1:
            if 'method' in str(type(attr1)):
                # print "need a test for %s.%s" % (name, e1)
                pass
            else:
                status = check(attr1, name + "." + e1, dict1[e1], status)
        else:
            print "need tests for %s.%s" % (name, e1)
            status = False
    return status


def main():
    status = check(jinja2, 'jinja2', elements, True)
    if status:
        print "tests are good"
    else:
        print "need some tests"

main()

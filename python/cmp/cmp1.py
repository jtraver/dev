#!/usr/bin/python

dict1 = {
    'a': 1,
    'b': 2,
}

dict2 = {
    'a': 0,
    'b': 2,
}

if dict1 == dict2:
    print "FAIL"
else:
    print "PASS"

dict1 = {
    'a': {
        'c': 'bake'
    },
    'b': 2,
}

dict2 = {
    'a': {
        'c': 'shake'
    },
    'b': 2,
}

if dict1 == dict2:
    print "FAIL"
else:
    print "PASS"

dict1 = {
    'a': {
        'c': [0, 1]
    },
    'b': 2,
}

dict2 = {
    'a': {
        'c': [0, 2]
    },
    'b': 2,
}

if dict1 == dict2:
    print "FAIL"
else:
    print "PASS"

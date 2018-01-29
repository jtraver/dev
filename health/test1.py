#!/usr/bin/python

import yaml


test1 = {}
test1['dict2'] = { 'a2': 1, 'b2': 2, 'c2': 3}

list2 = []
list2.append('2 first')
list2.append(['a', 'b', 'c'])
list2.append([1, 2, 3])
list2.append('2 last')

dict1 = {}
dict1['dict1'] = { 'a1': 1, 'b1': 2, 'c1': 3}
dict1['dict2'] = { 'a2': 1, 'b2': 2, 'c2': 3}
dict1['list2'] = list2

test1['dict1'] = dict1
test1['dict3'] = None
test1['dict4'] = {}
test1['dict5'] = []


list1 = []
list1.append('1 first')
list1.append(['a', 'b', 'c'])
list1.append([1, 2, 3])
list1.append([None, {}, []])
list1.append('1 last')
test1['list1'] = list1

with open('test1.yml', 'w') as outfile:
    outfile.write(yaml.dump(test1, default_flow_style=False))

test2 = yaml.load(file('test1.yml'))
print "test2 = %s" % str(test2)

if test1 == test2:
    print "load and dump worked"
else:
    print "load and dump did not work"

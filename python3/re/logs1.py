#!/usr/bin/env python3
#!/usr/bin/python

import re

def grep_file_match(filename):
    # accept = ['INFO']
    # accept = ['config']
    accept = ['config', '\(partition\)']
    apat = '.*' + accept[0] + '.*'
    for pat in accept[1:]:
        apat += '|' + '.*' + pat + '.*'
    print("apat = %s" % str(apat))
    accept_regex = re.compile(r'%s' % apat)
    print("accept_regex = %s" % str(accept_regex))
    file1 = open(filename, 'r')
    for line in file1:
        line = line.strip()
        accept_res = accept_regex.match(line)
        # if accept_res != None:
            # print "accept_res = %s" % str(accept_res)
        if accept_res:
            print("%s" % str(line))


def grep_file_search(filename):
    # accept = ['INFO']
    # accept = ['config']
    accept = ['config', '\(partition\)']
    apat = accept[0]
    for pat in accept[1:]:
        apat += '|' + pat
    print("apat = %s" % str(apat))
    accept_regex = re.compile(r'%s' % apat)
    print("accept_regex = %s" % str(accept_regex))
    file1 = open(filename, 'r')
    for line in file1:
        line = line.strip()
        accept_res = accept_regex.search(line)
        # if accept_res != None:
            # print "accept_res = %s" % str(accept_res)
        if accept_res:
            print("%s" % str(line))

def main():
    # grep_file_match('data.txt')
    grep_file_search('data.txt')

main()

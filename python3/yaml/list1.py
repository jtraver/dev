#!/usr/bin/env python3
#!/usr/bin/python

import yaml

#with open('tags1.yml', 'w') as outfile:
#    outfile.write(yaml.dump(tags1, default_flow_style=False))
#
#tags2 = yaml.load(file('tags1.yml'), Loader=yaml.FullLoader)
#print "tags2 = %s" % str(tags2)
#
#if tags1 == tags2:
#    print "load and dump worked"
#else:
#    print "load and dump did not work"

def main():
    list1()

def list1():
    l1 = []
    l1.append("sunrider")
    l1.append("bulletproof")
    l1.append("metagenics")
    l1.append("nutrigold")
    l1.append("standard process")
    l1.append("irwin naturals")
    fn1 = "list1.yaml"
    s1 = yaml.dump(l1, default_flow_style=False)
    print("s1 =\n%s" % str(s1))
    with open(fn1, 'w') as outfile:
        outfile.write(s1)
    l2 = yaml.load(file(fn1), Loader=yaml.FullLoader)
    if l1 == l2:
        print("load and dump worked")
    else:
        print("load and dump did not work")

main()

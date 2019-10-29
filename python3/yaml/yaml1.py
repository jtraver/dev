#!/usr/bin/env python3
#!/usr/bin/python

import yaml

print "yaml = %s" % str(yaml)
print "yaml = %s" % dir(yaml)

# http://stackoverflow.com/questions/12470665/yaml-writing-data-into-yaml-through-python

tags1 = {
    'aerospike-client-c': '3.0.74',
    'aerospike-server': '3.3.10',
    'aerospike-server-enterprise': '3.3.10',
    'aerospike-tools': '3.3.10',
    'client': '2.1.40',
    'devtools': '1.0.0',
    'release': '1.0.11',
    'dev': '0.0.1'  # for development testing only
}

with open('tags1.yml', 'w') as outfile:
    outfile.write(yaml.dump(tags1, default_flow_style=False))

tags2 = yaml.load(file('tags1.yml'), Loader=yaml.FullLoader)
print "tags2 = %s" % str(tags2)

if tags1 == tags2:
    print "load and dump worked"
else:
    print "load and dump did not work"

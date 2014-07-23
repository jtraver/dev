#!/usr/bin/python

import yaml

print "yaml = %s" % str(yaml)
print "yaml = %s" % dir(yaml)

# http://stackoverflow.com/questions/12470665/yaml-writing-data-into-yaml-through-python

config1 = {
    'repos4': [
        {
            'name': 'aerospike-client-c',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'prod3.0'
                }
            }
        },
        {
            'name': 'aerospike-server',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'prod3.0'
                }
            }
        },
        {
            'name': 'aerospike-server-enterprise',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'prod3.0'
                }
            }
        },
        {
            'name': 'aerospike-tools',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'prod3.0'
                }
            }
        },
        {
            'name': 'client',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'prod2.0'
                }
            }
        },
        {
            'name': 'devtools',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'master'
                }
            }
        },
        {
            'name': 'release',
            'owner': 'citrusleaf',
            'branches': {
                'dev_branch': {
                    'branch': 'master'
                },
                'rel_branch': {
                    'branch': 'master'
                }
            }
        }
    ]
}

with open('config1.yml', 'w') as outfile:
    outfile.write( yaml.dump(config1, default_flow_style=False) )

config2 = yaml.load(file('config1.yml'))
print "config2 = %s" % str(config2)

if config1 == config2:
    print "load and dump worked"
else:
    print "load and dump did not work"

#!/usr/bin/env python

import os
import yaml

def file(filename):
    f = open(filename, "r")
    contents = ""
    for line in f:
        contents += line
    return contents

def find_yaml_files(directory):
    yaml_files = []
    for root, dirs, files in os.walk(directory):
        print("find_yaml_files: root = %s" % str(root))
        print("  dirs = %s" % str(dirs))
        print("  files = %s" % str(files))
        for file in files:
            print("    file = %s" % str(file))
            if file.endswith('.yaml') or file.endswith('.yml'):
                print("      yaml file = %s" % str(file))
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def main():
    print("main")
    # yaml_files = find_yaml_files('/path/to/your/directory')
    yaml_files = find_yaml_files('../../')
    print(yaml_files)
    for yaml_file in yaml_files:
        yaml1 = yaml.load(file(yaml_file), Loader=yaml.FullLoader)
        print("---------------------------------------------------------------------------------")
        print("%s =\n%s" % (str(yaml_file), yaml.dump(yaml1, default_flow_style=False)))

main()

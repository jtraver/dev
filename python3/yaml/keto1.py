#!/usr/bin/env python3

import glob
import os
import yaml

if False:
    filename = 'yaml3.config'

    dc1 = []
    dc1.append({"ip": "111.111.111.111", "name": "a1"})
    dc1.append({"ip": "222.222.222.222", "name": "b1"})
    clusters = []
    clusters.append({"name": "dc1", "nodes": dc1})
    config1 = {
        "user": "citrusleaf",
        "clusters": clusters
    }

    with open(filename, 'w') as outfile:
        outfile.write(yaml.dump(config1, default_flow_style=False))

    config2 = yaml.load(file(filename), Loader=yaml.FullLoader)
    print("config2 = %s" % str(config2))

    if config1 == config2:
        print("load and dump worked")
    else:
        print("load and dump did not work")

    os.system("cat " + filename)


if False:
    d210321 = []
    d210321.append({"name":  "cream cheese", "total": 212, "carb": 14, "protein": 21})
    d210321.append({"name":  "mac nutes", "total": 184, "carb": 28, "protein": 14})

    print("yaml1 = \n%s" % yaml.dump(d210321, default_flow_style=False))


if False:
    #!/usr/bin/env python3

    import glob

    def main():
        pyfiles = glob.glob("../*/*.py")
        for pyfile in pyfiles:
            print(("pyfile %s" % pyfile))

    main()


def file(filename):
    f = open(filename, "r")
    contents = ""
    for line in f:
        contents += line
    return contents

def main():
    ketofiles = glob.glob("keto.*")
    for ketofile in ketofiles:
        print(("ketofile %s" % ketofile))
        keto1 = yaml.load(file(ketofile), Loader=yaml.FullLoader)
        # print("keto1 = \n%s" % yaml.dump(keto1, default_flow_style=False))
        carbs = 0
        protein = 0
        for k1 in keto1:
            carbs += k1['carb']
            protein += k1['protein']
        print("  carbs = %s" % str(carbs))
        print("  protein = %s" % str(protein))

main()

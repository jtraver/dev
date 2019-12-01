#!/usr/bin/env python3
#!/usr/bin/python3

import bs4

def main():
    filename = '0.html'
    file1 = open(filename, 'r')
    bsObj = bs4.BeautifulSoup(file1.read(), "html.parser")
    print(("bsObj = %s" % str(bsObj)))
    print(("bsObj.option = %s" % str(bsObj.option)))
    for option in bsObj.option:
        print(("  option = %s" % str(option)))
    optionList = bsObj.findAll('option')
    print(" ")
    print("option list")
    for option in optionList:
        print(("  option = %s" % str(option)))
    selectList = bsObj.findAll('select')
    print(" ")
    print("select list")
    for select in selectList:
        print(("  select = %s" % str(select)))

main()

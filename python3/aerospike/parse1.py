#!/usr/bin/env python3

REALLY_VERBOSE = False

def get_value(s1):
    if REALLY_VERBOSE:
        print ("def get_value(s1):")
        sys.stdout.flush()
    if s1 == None:
        return None
    if s1 == "true":
        return True
    if s1 == "false":
        return False
    if s1 == "null":
        return None
    try:
        return int(s1)
    except ValueError:
        pass
    try:
        return float(s1)
    except ValueError:
        pass
    fields1 = s1.split(":")
    if len(fields1) == 2:
        return fields1[0], get_value(fields1[1])
    return str(s1)

def get_item(res1, pos1):
    str1 = ""
    while pos1 < len(res1):
        # print("get_item: pos1 = %s" % str(pos1))
        ch1 = res1[pos1]
        # print("get_item: ch1 = %s" % str(ch1))
        if ch1 == "," or ch1 == "]":
            item1 = get_value(str1)
            # print("get_item: returning item1 %s at pos1 %s" % (str(item1), str(pos1)))
            return item1, pos1 + 1
        elif ch1 == "[":
            list1, pos1 = get_list(res1, pos1 + 1)
            # print("get_item: returning list1 %s at pos1 %s" % (str(list1), str(pos1)))
            return list1, pos1
        else:
            str1 += ch1
            pos1 += 1
    item1 = get_value(str1)
    return item1, pos1 + 1

def get_list(res1, pos1):
    list1 = []
    while pos1 < len(res1):
        # print("get_list: pos1 = %s" % str(pos1))
        ch1 = res1[pos1]
        # print("get_list: ch1 = %s" % str(ch1))
        if ch1 == ",":
            lch1 = res1[pos1 - 1]
            if lch1 == "]":
                # print("get_list: returning list1 %s at pos1 %s" % (str(list1), str(pos1)))
                return list1, pos1 + 1
            list1.append("")
            pos1 += 1
        elif ch1 == "[":
            list2, pos1 = get_list(res1, pos1 + 1)
            list1.append(list2)
        elif ch1 == "]":
            # print("get_list: returning list1 %s at pos1 %s" % (str(list1), str(pos1)))
            return list1, pos1 + 1
        else:
            item1, pos1 = get_item(res1, pos1)
            list1.append(item1)
    return list1, pos1 + 1

def main():
    print("parse")
    list1 = []
    list1.append(6)
    list1.append(3000)
    list2 = []
    list3 = []
    list3.append("BB9F22F0B6B1FAC")
    list3.append("")
    list4 = []
    list4.append("255.254.253.251")
    list4.append("255.254.252.251")
    list3.append(list4)
    list2.append(list3)
    list3 = []
    list3.append("BB9C62F0B6B1FAC")
    list3.append("")
    list4 = []
    list4.append("255.254.253.250")
    list4.append("255.254.252.250")
    list3.append(list4)
    list2.append(list3)
    list3 = []
    list3.append("BB9A0300B6B1FAC")
    list3.append("")
    list4 = []
    list4.append("255.254.253.249")
    list4.append("255.254.252.249")
    list3.append(list4)
    list2.append(list3)
    list1.append(list2)
    print("     res1 = 6,3000,[[BB9F22F0B6B1FAC,,[255.254.253.251,255.254.252.251]],[BB9C62F0B6B1FAC,,[255.254.253.250,255.254.252.250]],[BB9A0300B6B1FAC,,[255.254.253.249,255.254.252.249]]]")
    print("    list1 = %s" % str(list1))
    res1 = "6,3000,[[BB9F22F0B6B1FAC,,[255.254.253.251,255.254.252.251]],[BB9C62F0B6B1FAC,,[255.254.253.250,255.254.252.250]],[BB9A0300B6B1FAC,,[255.254.253.249,255.254.252.249]]]"
    list2 = []
    pos1 = 0
    while pos1 < len(res1):
        item1, pos1 = get_item(res1, pos1)
        list2.append(item1)
    print("    list2 = %s" % str(list2))
    # if str(list1) == str(list2):
    if list1 == list2:
        print("PASS")
    else:
        print("FAIL")

main()

#!/usr/bin/env python3
#!/usr/bin/python

import os

home1 = os.path.expanduser("~")

# /Users/jtraver/dev/git/jtraver/english-words
# Johns-MacBook-Pro-3:english-words jtraver$ ls
# CONTRIBUTING.md				README.md				word_list_moby_README.txt		word_list_moby_credits.txt		words.zip				words_alpha.zip				words_dictionary.zip
# LICENSE.md				read_english_dictionary.py		word_list_moby_all_moby_words.icss.yaml	words.txt				words_alpha.txt				words_dictionary.json


fives = []
filename = os.path.join(home1, "dev", "git", "jtraver", "english-words", "words_alpha.txt")
file1 = open(filename, 'r')
# print "file1 = %s" % str(file1)
# print "file1 = %s" % str(type(file1))
# print "file1 = %s" % str(dir(file1))
for line in file1.xreadlines():
# for line in file1.readlines():
    line = line.rstrip()
    if len(line) == 5:
        # print "%s" % line
        fives.append(line)
file1.close()

word = "groan"
# w1 = groin
# w1 = groat
# w1 = grown
groan = list(word)
# print "word = %s" % str(word)
alphas = "abcdefghijklmnopqrstuvwxyz"
#print "alphas len = %s" % str(len(alphas))
for a1 in alphas:
    print "a1 = %s" % str(a1)
    for l1 in word:
        if l1 == "g":
            w1 = a1 + "roan"
            if w1 != word and w1 in fives:
                print "w1 = %s" % str(w1)
        elif l1 == "r":
            w1 = "g" + a1 + "oan"
            if w1 != word and w1 in fives:
                print "w1 = %s" % str(w1)
        elif l1 == "o":
            w1 = "gr" + a1 + "an"
            if w1 != word and w1 in fives:
                print "w1 = %s" % str(w1)
        elif l1 == "a":
            w1 = "gro" + a1 + "n"
            if w1 != word and w1 in fives:
                print "w1 = %s" % str(w1)
        elif l1 == "n":
            w1 = "groa" + a1
            if w1 != word and w1 in fives:
                print "w1 = %s" % str(w1)

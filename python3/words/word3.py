#!/usr/bin/env python3
#!/usr/bin/python

import os

stack_limit = 900

def main():
    global fives
    global words
    global todo
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
    print "len fives = %s" % str(len(fives))
    words = ["groan"]
    todo = []
    print "len words = %s" % str(len(words))
    #for word in words:
    #    # print "word = %s" % str(word)
    #    get_words(word)
    get_words(0, words[0])
    print "len words = %s" % str(len(words))
    for word in todo:
        get_words(0, word)
    print "len words = %s" % str(len(words))
    print "\ncheck fives"
    for word in fives:
        if not word in words:
            print "did not find %s" % str(word)

def get_words(depth, word):
    global words
    global todo
    # print "START depth = %s, word = %s" % (str(depth), str(word))
    list1 = list(word)
    alphas = "abcdefghijklmnopqrstuvwxyz"
    # #print "alphas len = %s" % str(len(alphas))
    for a1 in alphas:
        # print "a1 = %s" % str(a1)
        for i1 in xrange(len(word)):
            l1 = list1[i1]
            # print "%s l1 = %s" % (str(i1), str(l1))
            w1 = ""
            for i2 in xrange(0, i1):
                l2 = list1[i2]
                w1 += l2
            w1 += a1
            for i3 in xrange(i1 + 1, len(word)):
                l3 = list1[i3]
                w1 += l3
            # print "w1 = %s" % str(w1)
            # if w1 != word and w1 in fives:
            if not w1 in words and w1 in fives:
                # print "    \"%s\"," % str(w1)
                print "depth %s %s -> %s by %s at %s" % (str(depth), str(word), str(w1), str(a1), str(i1))
                words.append(w1)
                if depth < stack_limit:
                    get_words(depth + 1, w1)
                else:
                    todo.append(w1)

main()

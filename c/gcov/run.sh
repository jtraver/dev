
# 
# make main
# ./main


# https://en.wikipedia.org/wiki/Gcov


rm a.out
rm cov.c.gcov
rm cov.gcda
rm cov.gcno


gcc -Wall -fprofile-arcs -ftest-coverage cov.c
./a.out
gcov cov.c
vi cov.c.gcov

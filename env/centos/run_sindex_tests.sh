cd ../../../qa_tests/unit_tests/sindex

NTEST=8

rm sindex.log
date > sindex.log
echo >> sindex.log
# rm jenkins_sindex_test.log

# basic
./sindex.sh "-C 1 -h 192.168.75.206 -n test -p 3000 -d 1 -s $NTEST -e $NTEST"

echo ----------------------------------------------------------------------------------------------------
echo START BACKGROUND RUN
echo ----------------------------------------------------------------------------------------------------
sleep 2

# ./sindex.sh "-h 192.168.75.206,192.168.75.205 -n test -p 3000 -d 1 -s 5 -e 5" > sindex.log 2>&1 &
# ./sindex.sh "-C 2 -h 192.168.75.206,192.168.75.205 -n test -p 3000 -d 1 -s 5 -e 5" > sindex.log 2>&1 &

# test N
./sindex.sh "-C 1 -h 192.168.75.206 -n test -p 3000 -d 1 -s $NTEST -e $NTEST" >> sindex.log 2>&1 &

# test 6
# ./sindex.sh "-C 1 -h 192.168.75.206 -n test -p 3000 -d 1 -s 6 -e 6" >> sindex.log 2>&1 &

# test 5
# ./sindex.sh "-C 1 -h 192.168.75.206 -n test -p 3000 -d 1 -s 5 -e 5" > sindex.log 2>&1 &


# ./sindex.sh "-P -h 192.168.75.206,192.168.75.205 -n test -p 3000 -d 1 -s 5 -e 5" > sindex.log 2>&1 &

tail -f sindex.log

vi sindex.log

# vi jenkins_sindex_test.log

kill %1

jobs
pwd
# S5
# ./run_assertions_jenkins.sh sindex 5 5 -P 1 -u jenkins -h 192.168.75.206,192.168.75.205 -j sindex_tests -n test -p 3000 -d 1

cd -

jobs
pwd

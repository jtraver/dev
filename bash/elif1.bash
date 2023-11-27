#!/bin/bash

echo "grep RC4 get_process_return_code.bash"
grep RC4 get_process_return_code.bash
RC1=$?
echo RC1 $RC1


echo grep junkandstuff func1.bash
grep junkandstuff func1.bash
RC2=$?
echo RC2 $RC2

echo ls
ls
RC3=$?
echo RC3 $RC3

echo ls biz.not
ls biz.not
RC4=$?
echo RC4 $RC4


#     0     One or more lines were selected.
#     1     No lines were selected.
#     >1    An error occurred.
if ((RC1 == 0)); then
    echo "if              " RC1 STATUS found RC4 in get_process_return_code.bash
elif ((RC1 == 1)); then
    echo "elif              " RC1 STATUS did not find RC4 in get_process_return_code.bash
else
    echo "else             " RC1 STATUS encountered error grepping RC4 in get_process_return_code.bash
fi

#     0     One or more lines were selected.
#     1     No lines were selected.
#     >1    An error occurred.
if ((RC2 == 0)); then
    echo "if             " RC2 STATUS found junkandstuff in get_process_return_code.bash
elif ((RC2 == 1)); then
    echo "elif             " RC2 STATUS did not find junkandstuff in get_process_return_code.bash
else
    echo "else             " RC2 STATUS encountered error grepping junkandstuff in get_process_return_code.bash
fi

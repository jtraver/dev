#!/usr/bin/env bash

loopSCRIPT_NAME=grep.sh

loopSTARTTIME=$(date +%s)
loopDATE=`date +%y%m%d%H%M%S`
echo starting $loopSCRIPT_NAME at $loopDATE
echo

FILES=`ls`
echo FILES $FILES

loop_limit=`echo  $FILES | wc | awk -F' ' '{print $2; exit;}'`

echo $feo_tcount files

echo "test" >> tmp.tmp

grep test tmp.tmp
RC1=$?
echo RC1 $RC1
if (( RC1 == 0 )) ; then
    echo RC1 found test in tmp.tmp
else
    echo RC1 did not find test in tmp.tmp
fi

grep junk tmp.tmp
RC2=$?
echo RC2 $RC2
if (( RC2 == 0 )) ; then
    echo RC2 found junk in tmp.tmp
else
    echo RC2 did not find junk in tmp.tmp
fi

grep -v test tmp.tmp
RC3=$?
echo RC3 $RC3
if (( RC3 == 0 )) ; then
    echo RC3 found other than test in tmp.tmp
else
    echo RC3 found only test in tmp.tmp
fi

grep -v junk tmp.tmp
RC4=$?
echo RC4 $RC4
if (( RC4 == 0 )) ; then
    echo RC4 found other than junk in tmp.tmp
else
    echo RC4 found only junk in tmp.tmp
fi

loop_count=0
# loop_limit=3
# while [ $loop_count -le $loop_limit ]
for file in $FILES ; do
    loop_count=$(( $loop_count + 1 ))
    echo loop loop_count is $loop_count $file
    # echo sleeping $loop_count
    # sleep $loop_count
done
echo loop count is $loop_count

echo
loopENDDATE=`date +%y%m%d%H%M%S`
loopENDTIME=$(date +%s)
echo finishing $loopSCRIPT_NAME at $loopENDDATE in $(($loopENDTIME - $loopSTARTTIME)) seconds



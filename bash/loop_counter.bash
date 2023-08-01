#!/usr/bin/env bash

loopSCRIPT_NAME=loop.sh

loopSTARTTIME=$(date +%s)
loopDATE=`date +%y%m%d%H%M%S`
echo starting $loopSCRIPT_NAME at $loopDATE
echo

FILES=`ls`
echo FILES $FILES

loop_limit=`echo  $FILES | wc | awk -F' ' '{print $2; exit;}'`

echo $feo_tcount files


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



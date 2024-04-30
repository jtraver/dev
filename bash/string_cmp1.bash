#!/usr/bin/env bash

loopSCRIPT_NAME=string_cmp1.bash

loopSTARTTIME=$(date +%s)
loopDATE=`date +%y%m%d%H%M%S`
echo starting $loopSCRIPT_NAME at $loopDATE
echo

FILES=`ls`
echo FILES $FILES

loop_limit=`echo  $FILES | wc | awk -F' ' '{print $2; exit;}'`

echo $feo_tcount files

echo "test" > tmp.tmp

FOUND=FOUND
notFOUND=notFOUND

echo
echo "---------------------------------------------------------------------------------"
grep test tmp.tmp
RC1=$?
echo RC1 $RC1
if (( RC1 == 0 )) ; then
    echo PASS 1RC1 found test in tmp.tmp
    aRC1=FOUND
else
    echo 1RC1 did not find test in tmp.tmp
    aRC1=notFOUND
fi



echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 == "FOUND" ]] ; then
    echo 1 1 PASS 2aRC1 found test in tmp.tmp
else
    echo 1 1 FAIL 2aRC1 did not find test in tmp.tmp
fi
echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 == "notFOUND" ]] ; then
    echo 2 2 FAIL 2aRC1 found test in tmp.tmp
else
    echo 2 2 PASS 2aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 != "FOUND" ]] ; then
    echo 1 3 FAIL 2aRC1 found test in tmp.tmp
else
    echo 1 3 PASS 2aRC1 did not find test in tmp.tmp
fi
echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 != "notFOUND" ]] ; then
    echo 2 4 PASS 2aRC1 found test in tmp.tmp
else
    echo 2 4 FAIL 2aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 == $FOUND ]] ; then
    echo 3 5 PASS 2aRC1 found test in tmp.tmp
else
    echo 3 5 FAIL 2aRC1 did not find test in tmp.tmp
fi
echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 == $notFOUND ]] ; then
    echo 4 6 FAIL 2aRC1 found test in tmp.tmp
else
    echo 4 6 PASS 2aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 != "FOUND" ]] ; then
    echo 3 7 FAIL 2aRC1 found test in tmp.tmp
else
    echo 3 7 PASS 2aRC1 did not find test in tmp.tmp
fi
echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ $aRC1 != "notFOUND" ]] ; then
    echo 4 8 PASS 2aRC1 found test in tmp.tmp
else
    echo 4 8 FAIL 2aRC1 did not find test in tmp.tmp
fi



echo
echo "---------------------------------------------------------------------------------"
echo 2 RC1 $RC1
echo 2 aRC1 $aRC1
if [[ ${aRC1} == ${FOUND} ]] ; then
    echo PASS 2aRC1 found test in tmp.tmp
else
    echo FAIL 2aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 3 RC1 $RC1
echo 3 aRC1 $aRC1
# if [[ $aRC1 == $FOUND ]] ; then
if [[ $aRC1 == "FOUND" ]] ; then
    echo PASS true 1 3aRC1 $FOUND test in tmp.tmp
else
    echo FAIL false 3aRC1 $notFOUND test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 3 RC1 $RC1
echo 3 aRC1 $aRC1
# if [[ $aRC1 == $notFOUND ]] ; then
if [[ $aRC1 == "notFOUND" ]] ; then
    echo FAIL true 1 3aRC1 $FOUND test in tmp.tmp
else
    echo PASS false 3aRC1 $notFOUND test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 3 RC1 $RC1
echo 3 aRC1 $aRC1
if [[ $aRC1 == "FOUND" ]] ; then
    echo PASS true 2 3aRC1 found test in tmp.tmp
else
    echo FAIL false 3aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 4 RC1 $RC1
echo 4 aRC1 $aRC1
if [[ $aRC1 == "FOUND" ]] ; then
    echo PASS 4aRC1 found test in tmp.tmp
else
    echo FAIL 4aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
echo 5 RC1 $RC1
echo 5 aRC1 $aRC1
if [[ $aRC1 == "FOUND" ]] ; then
    echo PASS 5aRC1 found test in tmp.tmp
else
    echo FAIL 5aRC1 did not find test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
grep junk tmp.tmp
RC2=$?
echo RC2 $RC2
if (( RC2 == 0 )) ; then
    echo FAIL RC2 found junk in tmp.tmp
else
    echo PASS RC2 did not find junk in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
grep -v test tmp.tmp
RC3=$?
echo RC3 $RC3
if (( RC3 == 0 )) ; then
    echo FAIL RC3 found other than test in tmp.tmp
else
    echo PASS RC3 found only test in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"
grep -v junk tmp.tmp
RC4=$?
echo RC4 $RC4
if (( RC4 == 0 )) ; then
    echo PASS RC4 found other than junk in tmp.tmp
else
    echo FAIL RC4 found only junk in tmp.tmp
fi

echo
echo "---------------------------------------------------------------------------------"

#loop_count=0
## loop_limit=3
## while [ $loop_count -le $loop_limit ]
#for file in $FILES ; do
#    loop_count=$(( $loop_count + 1 ))
#    echo loop loop_count is $loop_count $file
#    # echo sleeping $loop_count
#    # sleep $loop_count
#done
#echo loop count is $loop_count

echo
loopENDDATE=`date +%y%m%d%H%M%S`
loopENDTIME=$(date +%s)
echo finishing $loopSCRIPT_NAME at $loopENDDATE in $(($loopENDTIME - $loopSTARTTIME)) seconds



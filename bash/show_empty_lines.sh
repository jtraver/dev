#!/usr/bin/env bash

# awk '!NF' export.sh



TOP=`pwd`

echo
echo "---------------------------------------------------------------------------------"
for x in `find . ` ; do
    WC1=`awk '!NF' $x | wc`
    if [ "$WC1" != "       0       0       0" ]
    then
        echo FAIL $x WC1 $WC1
    else
        echo PASS $x WC1 $WC1
    fi
done
echo "---------------------------------------------------------------------------------"

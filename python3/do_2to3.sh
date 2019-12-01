#!/usr/bin/env bash

for x in `ls`; do
    if [[ -d $x ]] ;  then
        echo $x
        cd $x
        for y in `ls *.py`; do
            echo $y
            /Library/Developer/CommandLineTools/usr/bin/2to3-3.7 $y > $y.diff
            patch < $y.diff
        done
        cd ..
    fi
done


# # for x in `ls *`; do
# for x in `ls`; do
#     if [[ -d $x && -d ${x}/.git ]] ;  then
#         echo ; echo $x ; cd $x ; git checkout master ; git pull ; cd ..
#     fi
# done
# cd qe.go
# pwd
# git checkout v2
# git pull
# cd ..
# for x in `ls -d SFGREP` ; do
#     echo $x
#     cd $x
#     ln -s ~/SFGREP/*.sh .
#     ./setup.sh
#     cd -
# done
# for x in `ls -d */SFGREP` ; do
#     echo $x
#     cd $x
#     ln -s ~/SFGREP/*.sh .
#     ./setup.sh
#     cd -
# done
# echo ""

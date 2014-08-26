#!/bin/sh

OS=`cat /etc/issue`

if [ $? -eq 0 ] ; then
    cat /etc/issue | grep "6."
    if [ $? -eq 0 ] ; then
        OS=centos6
    fi
fi

echo $OS

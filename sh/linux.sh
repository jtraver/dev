#!/bin/sh

OS=`cat /etc/issue`

cat /etc/issue | grep CentOS
RES1=$?
if [ $RES1 -eq 0 ] ; then
    cat /etc/issue | grep "6."
    RES2=$?
    if [ $RES2 -eq 0 ] ; then
        OS=centos6
    fi
else
    echo not a linux box
fi

cat /etc/issue | grep Debian
RES1=$?
if [ $RES1 -eq 0 ] ; then
    cat /etc/issue | grep "6."
    RES2=$?
    if [ $RES2 -eq 0 ] ; then
        OS=debian6
    fi
else
    echo not a linux box
fi

cat /etc/issue | grep Ubuntu
RES1=$?
if [ $RES1 -eq 0 ] ; then
    cat /etc/issue | grep "12."
    RES2=$?
    if [ $RES2 -eq 0 ] ; then
        OS=ubuntu12
    fi
else
    echo not a linux box
fi

echo $OS

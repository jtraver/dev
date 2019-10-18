#!/usr/bin/env bash

if [[ -d "array1" ]]; then
    echo array1 is a directory
else
    echo array1 is not a directory
fi

if [[ ! -d "array1" ]]; then
    echo array1 is not a directory
else
    echo array1 is a directory
fi

#    if [[ "$OSTYPE" == "linux"* ]]; then
#        echo LINUX
#    elif [[ "$OSTYPE" == "darwin"* ]]; then
#        echo MAC
#    else
#        echo do not recognize OS $OSTYPE
#        exit 1
#    fi

#!/usr/bin/env bash

main() {
    if [[ "$OSTYPE" == "linux"* ]]; then
        echo LINUX
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo MAC
    else
        echo do not recognize OS $OSTYPE
        exit 1
    fi
}

main $@

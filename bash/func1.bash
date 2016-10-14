#!/bin/bash


gradle_test() {
    echo " gradle test " $1
}

main() {
    cmd="$1"
    case "${cmd}" in 
        gradle:* )
            for c in "$@"; do
                case "${c}" in
                    'gradle:test' ) gradle_test $2;;
                esac
            done
            ;;
        * )
            exec $@
            ;;
    esac
}

main $@

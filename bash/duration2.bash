#!/usr/bin/env bash

dur2SCRIPT_NAME=duration2.bash

dur2STARTTIME=$(date +%s)
dur2DATE=`date +%y%m%d%H%M%S`
echo starting $dur2SCRIPT_NAME at $dur2DATE
echo



# Function: track_elapsed
# Usage: track_elapsed [optional_id]
# Description: Prints the number of seconds since the last call for this ID.
#              If first call, prints 0 and initializes timer.

track_elapsed() {
    local id="${1:-default}"
    local now
    now=$(date +%s)

    # Use an associative array if available (bash 4+)
    if [[ -z "${__last_call_time[$id]+_}" ]]; then
        # First time for this ID
        __last_call_time[$id]=$now
        echo "0"
    else
        local last=${__last_call_time[$id]}
        local diff=$(( now - last ))
        __last_call_time[$id]=$now
        echo "$diff"
    fi
}

# Declare the global associative array once
declare -A __last_call_time



track_elapsed foo   # → 0 (first call)
sleep 2
track_elapsed foo   # → 2
sleep 3
track_elapsed foo   # → 3

track_elapsed bar   # → 0 (separate timer)
sleep 1
track_elapsed bar   # → 1


echo
dur2ENDDATE=`date +%y%m%d%H%M%S`
dur2ENDTIME=$(date +%s)
echo finishing $dur2SCRIPT_NAME at $dur2ENDDATE in $(($dur2ENDTIME - $dur2STARTTIME)) seconds



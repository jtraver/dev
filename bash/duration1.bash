#!/usr/bin/env bash

dur1SCRIPT_NAME=duration1.bash

dur1STARTTIME=$(date +%s)
dur1DATE=`date +%y%m%d%H%M%S`
echo starting $dur1SCRIPT_NAME at $dur1DATE
echo



# Function: track_elapsed
# Usage: track_elapsed [optional_id]
# Description: Prints the number of seconds since the last call for this ID.
#              If first time, initializes and prints 0.

track_elapsed() {
    local id="${1:-default}"          # Optional identifier (default = 'default')
    local state_file="/tmp/elapsed_${id}.timestamp"
    local now
    now=$(date +%s)

    if [[ -f "$state_file" ]]; then
        local last
        last=$(cat "$state_file")
        local diff=$(( now - last ))
        echo "$diff"
    else
        echo "0"
    fi

    # Update timestamp
    echo "$now" > "$state_file"
}

track_elapsed
sleep 1
track_elapsed
sleep 10
track_elapsed

echo
dur1ENDDATE=`date +%y%m%d%H%M%S`
dur1ENDTIME=$(date +%s)
echo finishing $dur1SCRIPT_NAME at $dur1ENDDATE in $(($dur1ENDTIME - $dur1STARTTIME)) seconds



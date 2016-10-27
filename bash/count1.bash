#!/bin/bash

out=`ls`

count=0
while read -r line; do
	((count+=1))
    echo $line
done <<< "$out"

echo count is $count

count=0
while read -r line; do
	((count+=1))
	if [ "$count" -gt 1 ]
	then
		break
	fi
    echo $line
done <<< "$out"

echo count is $count

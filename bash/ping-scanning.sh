#!/bin/bash


subnet=$1

for i in $(seq 1 254); do
    (
        if ping -c 1 $subnet.$i 1>/dev/null 2>/dev/null ; then
            echo $subnet.$i
        fi
    ) &
done

#!/bin/sh

for file in $(ls *.log)
do
        echo $file
        DROPPED=$(cat "$file" | grep -c "dropped")
        FAILED=$(cat "$file" | grep -c "!=")
        echo "Dropped buffers >= $DROPPED"
        echo "Failed buffers = $FAILED"
done

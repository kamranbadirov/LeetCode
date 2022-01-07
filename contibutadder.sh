#!/bin/bash


for i in {1..5}
do
    if (($i % 2))
    then
        touch testtt
        git add .
        git commit -m "testing ${i}th commit"
        git push
    else
        rm testtt
        git add .
        git commit -m "testing ${i}th commit"
        git push
    fi
done

echo "completed"
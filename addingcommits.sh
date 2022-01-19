#!/bin/bash



for i in {1..25}
do
   if {{ $i % 2 == 0}}
   then
   touch testfile.txt
   else rm -rf testfile.txt
   fi
   git add .
   git commit -m "testing git commands"
   git push

done
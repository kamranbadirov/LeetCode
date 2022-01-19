#!/bin/bash



for i in {1..25}
do
   touch testfile.txt
   git add .
   git commit -m "testing git commands"
   git push
   rm -rf testfile.txt
done
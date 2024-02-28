#!/bin/bash
#Create a script that will print "Even Day" if current date is an even number ?

DATE=`date +'%d'`

if [ $((DATE % 2)) -eq 0 ]
then
echo "Even Day"
fi

#!/bin/bash

#Create a script that will print "OK" if current hour is an even number ?
CURRENTTIME=`date +'%H'`
if [$((CURRENTTIME % 2)) -eq 0]
then
echo "OK"
fi

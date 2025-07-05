#!/bin/bash
n=100
if [ $((n % 10)) -eq 0 ]
then
echo " divisible by 10"
else
echo " not divisible by 10"
fi

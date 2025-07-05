#!/bin/bash

i=0
while [ $i -lt 10 ]
do
((i++))
if [[ "$i" == "3" ]]
then
continue
fi
echo "$i"
done

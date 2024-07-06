#!/bin/bash

i=0
while [ $i -lt 10 ]
do
echo "$i"
((i++))
if [[ "$i" == '2' ]]
then
break
fi
done

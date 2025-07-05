#! /bin/bash
VAR=`date +%d`
if [[ $VAR -gt 10 ]]
then
echo "Greater than 10"
elif [[ $VAR -eq 10 ]]
then
echo "Equals to 10"
else
echo "Less than 10"
fi

#!/bin/bash
function sum()
{
echo -n "enter first number "
read num
echo -n "enter second number "
read num1
echo "Sum : $(( num+num1 ))"
}
sum

  GNU nano 6.2                                                      divide-by-3-or-5.sh                                                               
  GNU nano 6.2                                                     divide-by-3-and-5.sh
#!/bin/bash

#Write a script that will ask a number from user and then using if condition verify if number is divisible by 3 and 5 both , if condition meets then >
echo "Enter a number"
read num
if [[ $((num % 3)) == 0 || $((num % 5)) == 0 || $((num % 7)) == 0 ]]
then
echo "Divisible"
else
echo "Not divisible"
fi


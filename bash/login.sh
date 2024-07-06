#!/bin/bash

#Write a script that will ask username and password from user and then using if condition verify if username="admin" and password="admin" , if condition meets then print "Login Success" else print "Wrong Login" ?

echo "Enter username"
read username
echo "Enter password"
read password
if [[ ($username == 'admin' && $password == 'admin') ]]
then
echo "Login success"
else
echo "Wrong login"
fi


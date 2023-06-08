#!/bin/bash
read -p "Enter number 1 :" x
read -p "Enter number 2 :" y
read -p "enter number 3:" z
if [ $x -ge $y ] && [ $x -ge $y ]
then 
echo $x
elif [ $y -ge $x ] && [ $y -ge $z ] 
then
echo $y
else 
echo $z 
fi

# !/bin/bash
a=1
while [ $a == 1 ]
do
read -p "enter number:" x 
read -p "enter number:" y
read -p "choose operation + - * / " ch
case $ch in
"+")
 val=$(($x+$y));;
"-")
 val=$(($x-$y));;
"*")
 val=$(($x*$y));;
"/")
 val=` echo "scale=4;$x/$y" | bc`
 #val=$((bc<<"scale=2;($x/$y)"));;
esac
echo $val
read -p "Do you want to continue?(1):" a
done







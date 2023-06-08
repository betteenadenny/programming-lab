# !/bin/bash
read -p "Enter a number:" num
fact=1
n=$num;
while [ $num -ge 1 ]
do
	fact=`expr $fact \* $num`
	num=`expr $num - 1`
done
echo "Factorial of $n is $fact"

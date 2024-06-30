#Shell script to find factorial of a number
echo "Enter the number"
read num
f=1
for (( i = 1 ; i <= num ; i ++ ))
do 
f=`expr $i \* $f`
done
echo "Factorial of a number is :"$f

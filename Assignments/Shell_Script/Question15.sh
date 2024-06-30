#Shell script to check whether a give number is prime or not
echo "Enter a number:"
read num
c=0 
for (( i=1 ; i<=$num ; i++))
do 
if [ `expr $num % $i` = 0 ]
then 
c=`expr $c + 1`
fi
done
if [ $c -gt 2 ]
then 
echo "The number is not prime"
else
echo "The number is prime"
fi

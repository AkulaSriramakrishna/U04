#Shell script to add digit of a number

echo "Enter a number:"
read num
s=0
while [ $num != 0 ]
do 
d=`expr $num % 10`
s=`expr $s + $d`
num=`expr $num / 10`
done
echo $s

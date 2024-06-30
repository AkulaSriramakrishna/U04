#Shell programing to find odd and even number
echo "Enter the number:"
read num1
if [ `expr $num1 % 2` = 0 ]
then
echo "The give number is Even"
else
echo "Given number is odd"
fi

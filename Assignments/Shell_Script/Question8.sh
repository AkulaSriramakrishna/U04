#Shell script to find largest of three number
echo "Enter first number:"
read num1
echo "Enter secound number:"
read num2
echo "Enter third number:"
read num3
if  [ $num1 -gt $num2 ] && [ $num1 -gt $num3 ]  
then
echo "First number is greates i.e $num1"
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
echo "Secound number is greatest i.e $num2"
else
echo "Third number is greatest i.e $num3"
fi

#Shell program to create largest of two Numbers
echo "Enter First number:"
read num1
echo "Enter secound number:"
read num2
if [ $num1 -gt $num2 ];then
echo "First Number is greater:$num1"
else
echo "Secoundnumber is greater:$num2"
fi

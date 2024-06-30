#Shell program to perform arthimatic based on case
echo "Enter first number"
read num1
echo "Enter Secound number:"
read num2
echo "Enter 1)Add 2)sub 3)mul 4)div"
read n
case $n in
1) echo "Sum is `expr $num1 + $num2`";;

2) echo "Sub is `expr $num1 - $num2`";;

3) echo "Mul is `expr $num1 \* $num2`";;

4) echo "divison is `expr $num1 / $num2`";;

esac

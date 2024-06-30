#Shell program to check weathee the given number is palindrome or not

echo "Enter a number:"
read num
rev_num=$(echo $num | rev)
if [ "$num" == "$rev_num" ]
then
echo "$num is palindrom"
else
echo "$num is not palindrome"
fi


#Shell script to reverse a string
echo "Enter a string:"
read str
l=`expr length $str`
echo "Length of string is : $l"
c=0
p=""
while [ $c != $l ]
do 
e=`expr substr $str $c 1`
p=$e$p
c=`expr $c + 1`
done
echo "The reverse of the string is : $p"

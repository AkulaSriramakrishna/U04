#Shell program to check weather the given year is leap or not
echo "Enter the year:"
read Year
if  [ $( [ `expr $Year %  100` != 0 ]  && [ `expr $Year % 400` = 0 ] ) ] || [ `expr $Year % 4` = 0 ] 
then
echo "Its a leap year"
else
echo "Its not a leap year"
fi

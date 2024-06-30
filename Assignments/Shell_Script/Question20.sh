#Shell script to short based on secound coloumn

echo "Enter File for sorting:"
read file
if [ -f $file ]
then
echo "Select sorting order 1)Assending 2)descinding"
read n
case $n in 

1) sort -k3 $file;;

2) sort -k3 -r $file;;
esac
else
echo "No file found"
fi

#Shell script tp accept a file and display its content

echo "Enter File name:"
read file
if [ -f $file ]
then
cat $file
else
echo "File not found"
fi

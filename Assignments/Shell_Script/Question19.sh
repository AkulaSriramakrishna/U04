#sell program to copy file
echo "Enter source file:"
read Src
echo "Enter Destination File:"
read Dst
cp -i $Src $Dst
echo "File copied Successfully"

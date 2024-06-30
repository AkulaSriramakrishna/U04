#Shell script to count no of words,lines and characters in a file
echo "Enter file name:"
read FileName
if [ -f $FileName ]
then 
wc $FileName
else
echo "File does not exists"
fi

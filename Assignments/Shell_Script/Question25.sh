#Shell program to count vowel and consonent
echo "Enter a string:"
read str
l=`expr length $str`
vowels=$(echo "$str" | grep -o -i '[aeiou]' | wc -l)
consonants=$(echo "$str" | grep -o -i '[bcdfghjklmpqrstvwxyz]' | wc -l)
echo "No of vowels are :$vowels"
echo "No of Consonent are :$consonants"

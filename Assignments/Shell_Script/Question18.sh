#Shell script to greet user based on day

day=$( date +%u )
u=$( whoami )
case $day in
1) echo "Good morning $u, Today is Monday";;
2) echo "Good morning $u, Today is Tuesday";;
3) echo "Good morning $u, Today is Wednesday";;
4) echo "Good morning $u, Today is Thursday";;
5) echo "Good morning $u, Today is Friday";;
6) echo "Good morning $u, Today is Saturday";;
7) echo "Good morning $u, Today is Sunday";;
esac

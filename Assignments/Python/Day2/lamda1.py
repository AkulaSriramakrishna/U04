sea=[0,1,3,44,5,6,56,5,4,6,7]

tintin = lambda x:x%2!=0
res = filter(tintin,sea)

for temp in res:
    print(temp)
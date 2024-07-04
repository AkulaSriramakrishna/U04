list_fruit = ['apple','banana','cherry','kiwi','mango']
result_list =[]
for temp in list_fruit:
    if "a" in temp:
        result_list.append(temp)

print(result_list)

result_list1= [temp for temp in list_fruit if 'a' in temp]

print('shortest method',result_list1)
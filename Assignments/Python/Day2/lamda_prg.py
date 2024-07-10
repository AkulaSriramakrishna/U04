def fun(variable):
    letters = ['a','e','i','o','u']
    if variable in letters:
        return True
    else:
        return False

sequence = ['g','e','e','z','u']
filtered = filter(fun,sequence)


for temp in filtered:
    print(temp)
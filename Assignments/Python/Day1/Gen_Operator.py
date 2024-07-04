def sum(x,y):
    z = x+y
    return z

def multiplication(x,y):
    z = x * y
    return z

def my_func():
    yield 2+3
    yield 5+2
    yield 8+2


a = 10
b = 20
res = sum(a,b)
print('sum is :',res)

res = multiplication(a,b)
print("product is :",res)

res = my_func()

for temp in res:
    print(temp)

res =my_func()
print(next(res))
print(next(res))
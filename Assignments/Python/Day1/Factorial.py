def factorial(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact * i
    return fact

x = 3
res = factorial(x)
print('Factorial of a given number is :',res)
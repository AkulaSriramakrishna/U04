def primenumber():
    prime = None
    num = 1
    while True:
        num = num + 1
        for i in range(2,num):
            if (num % i) == 0:
                prime = False
                break
            else:
                prime = True
                if prime:
                    yield num


res = primenumber()
for temp in res:
    print(temp)
    if temp > 6:
        break

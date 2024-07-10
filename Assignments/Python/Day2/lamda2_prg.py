import functools
import operator

list={1,2,3}
print('Sum of the list is :')
print(functools.reduce(operator.add,list))
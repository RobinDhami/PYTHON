# def func(**a):
#     print(a)

# func(a=2,b=6)

from functools import reduce
from operator import mul

def factorial(n):
   return reduce(mul,range(1,n+1))

f=factorial(5)
print(f)

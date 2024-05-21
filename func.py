# def func(**a):
#     print(a)

# func(a=2,b=6)

# from functools import reduce
# from operator import mul

# def factorial(n):
#    return reduce(mul,range(1,n+1))

# f=factorial(5)
# print(f)

#recursive function

def fact(n):
   if n in range(0,1):
      return 1
   return fact(n-1)*n

f=fact(5)
print(f)

print(list(map(lambda *a:a,range(0,5),"abcd")))
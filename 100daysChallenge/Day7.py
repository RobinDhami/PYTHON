from functools import reduce
#Lambda Function

l=[1,2,3,4,5,6]

print(list(map(lambda a:a*a,l)))
res=filter(lambda a: a%2==0 ,l )
print(list(res))

b=[2,3,4]
squared = map(lambda a:a*a,l)
rem=filter(lambda a:a<10,squared)
print(list(rem))
print(reduce(lambda a,b:a+b,l))
from functools import reduce

radius=[1,2,3,4,5,6,7,8,9]

x = list(map(lambda r:r*r*3.14,radius))
print(x)

y = list(filter(lambda r:r%2==0,radius))
print(y)

z = reduce(lambda a,b:a+b,radius)
print(z)
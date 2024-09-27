#Day8 MAP

l=[2,3,4,5]
print(list(map(lambda x:x*x,l)))

#Filter 
print(list(filter(lambda x:x<=3,l)))

#Custom map function

def cumap(func,itr):
    res=[]
    for i in itr:
        res.append(func(i))
    return res   

def min(a):
    return a-1

lis=[2,3,4,5,6]
result=cumap(min,lis)
print(result)
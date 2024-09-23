arr=[1,2,3,4,5]
def ques(arr):
    dict = {}
    for x in arr:
        dict[x]=x*x
    return dict

res=ques(arr)
print(res)

#sets

setA = {1,2,3,4,5}
setB = {1,"a",2,"d",4,3}

def inter(setA,setB):
    res = setA.intersection(setB)
    return res

res = inter(setA,setB)
print(res)

def dup(arr):
    dup=set()
    for i in arr:
        if i not in dup:
            res=dup.add(i)
    return  res       
brr=[1,2,3,4,5,6,1,2,45,2,3]
res=dup(brr)
print(res)    
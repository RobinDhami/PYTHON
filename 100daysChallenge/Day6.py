arr=[1,2,3,4,5]
def ques(arr):
    dict = {}
    for x in arr:
        dict[x]=x*x
    return dict

res=ques(arr)
print(res)
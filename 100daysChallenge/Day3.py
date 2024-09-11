#List Comprehension
l=[1,2,3,4,5] 


print([x*x for x in l])

print([x for x in l if x%2==0])
print([x if x%2==0 else x+1 for x in l])
#Loop in the list is being done here

list = ["apple", "ball" , "cate" , "dog" , "rat"]

for x in list:
    print(x)

for i in range(len(list)):
    print(i ,list[i])

#Using while Loop:
i=0
while i<len(list):
    print(i)
    i = i+1

#Looping thorugh list
[print(f" this is {x}")  for x in  list]    

#Enumerate gives index and its content respectively :

# fruits = ["apple", "ball", "cat" , "dog"]

# for i,x in enumerate(fruits):
#     print(i,x)

# import math 
# a=math.sqrt(64)
# print(a)
# s=pow(4,3)
# min(2,3,1)
# max(9,3,10)
# abs(-90)

# r=2
# p=math.pi
# area = p * r*r
# print(area)
# print(s)
# import datetime
# b= datetime.datetime.now()
# print(b)

student = ["ram", "shyam", "hari","gupta"]

for i,x in enumerate(student):

    try:
        if i==0:
            print("Found index and content")
    except Exception as e:
        print(e)        


# #palindrome 

# n=int(input("Enter a number"))
# print(n)
# while (n!=0):
#     reverse = 0
#     remainder = n%10
#     reverse = abs(reverse*10 + remainder)
#     n = n/10
#     print(n)
#     print(reverse)    
#     if(reverse==n):
#         print('palindrome')
     
#     else:
#         print("Not palindrome")    
  

a = 42 
print(id(a))
a = 43
print(id(a))

b=5
c=5
if id(b) == id(c):
    print("true")

fruits = "apple"
print(id(fruits))
fruits="ball"
print(id(fruits))
   
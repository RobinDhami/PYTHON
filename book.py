
# n=int(input("Enter a number"))
# original = n
# print(n)
# reverse = 0
# while (n!=0):
#     remainder = n%10
#     reverse = reverse*10 + remainder
#     n = n//10
# print(reverse)    
# if(reverse==original):
#     print("IS Palindrome")
# else:
#     print("Not ")   
  
# n=int(input("Enter a number"))
  


# a = 42 
# print(id(a))
# a = 43
# print(id(a))

# b=5
# c=5
# if id(b) == id(c):
#     print("true")

# fruits = "apple"
# print(id(fruits))
# fruits="ball"
# print(id(fruits))

# code = "I am a boy"
# r = code.encode('utf-8')
# print(r)
# print(type(r))

# tup = (3,4,2,0,5,7,9) # n  Immutable
# print(tup) 

# lis = [1,4,0,3,2,9]
# lis.sort()
# print(lis)
# x= max(lis)
# print(x)
# print(lis[2:4])

# l = list(range(1,6))
# print(type(l))

# dic =dict(zip("hello",range(1,6)))
# print(dic)

# database = {}
# database.update({"rabin":"dhami", "school":"grade"})
# database["rabin "]= "dhami"
# print(database)
# name = input("Enter your name")
# password = input("Enter Password")
# if name in database and database[name]==password:
#     print("Logged in successfully")
# elif name in database or name not in database:
#     print("Invalid name or password")
# else:
#     print("No such account . Create a login account")    


# fruits = ["apple","ball","cat", "dog","rat"]

# for i in range(len(fruits)):
#     print(i , fruits[i])

person = ["ram" , "laxman" , "hari" , "shyam" , "rabin"]
ages = [24,65,35,254,65]

for names,age in zip(person,ages):
    print( age,names)
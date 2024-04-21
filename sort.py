list = ["apple", "zebra" , "cat" ," ball"]
a = list.copy()
print(a)
list.sort()
print(list)

list.sort(reverse=True)
print(list)


#Palindrome 
a=input("Enter a word")
a=a.lower().replace(".","").replace(",","").replace(" ","")
b=a[::-1]
if (a==b):
    print("Palindrome")
else:
    print("Not palindrome")    
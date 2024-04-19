#Enter item in the list
list = ["apple" , "ball" , "cat" , "dog" , "egg" , "fish"]
n = len(list)
print(n)
print(list[2:4])
print(list[-4:-1])

if "ball" in list:
    print(f"ball is in list at location {list.index("ball")}")

a =input("Enter something to add item to list")
list.append(a)
print(list)

list.insert(4,"Futsal")
print (list)

tup = ("hell" , "yes")
list.extend(tup)
print(list)

#Remove items from list

list.remove("ball")
print(list)

list.pop()
print(list)

del list[2]
print(list)

list.clear()
print(list)
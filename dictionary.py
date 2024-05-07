# database = {}

# name = input("Enter your name: ")
# location = input("Enter your location: ")

# #Updating Dictionary
# database["name"] = name
# database["location"] = location

# print(database)

# a = input("Enter your name to check permission: ")
# b = input("Enter your location to check permission: ")

# # Check if the entered name and location match the database
# if name == a and location == b:
#     print("Permission Granted")
# else:
#     print("Permission Denied")



# Methods for dictionary 

dictionry = {
"car" :"tesla",
"bike" : "xpulse"
}

# Get specific value for a key 
x=dictionry.get("car")
print(x)

# add value to lasaat index
dictionry["rabin"] = "dhami"
print(dictionry)

dictionry.update({ "summer":"hot"})
# Get list if keys 
y=dictionry.keys()
print(y)

# Get list of values 
z = dictionry.values()
print(z)

a = dictionry.items()
print(a)

for i in a:
    if i == ("car","raa"):
        print(i)
    else:
        print("not found")    
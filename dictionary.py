database = {}

name = input("Enter your name: ")
location = input("Enter your location: ")

#Updating Dictionary
database["name"] = name
database["location"] = location

print(database)

a = input("Enter your name to check permission: ")
b = input("Enter your location to check permission: ")

# Check if the entered name and location match the database
if name == a and location == b:
    print("Permission Granted")
else:
    print("Permission Denied")

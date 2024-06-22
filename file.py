f = open("set.txt", "r")

print(f .readline())


import os
if os.path.exists("test.txt"):
  os.remove("test.txt")
else:
  print("The file does not exist.")
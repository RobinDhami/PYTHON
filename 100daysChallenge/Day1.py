#Enumerate
games=["cricket","futsal","tt","chess","volleyball"]

for i,v in enumerate(games):
    print(f"{i}:{v}")

for index,value in enumerate(games):
    print(len(games)-index-1,value)

print(dict(list(enumerate(games))))
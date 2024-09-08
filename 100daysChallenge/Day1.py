#Enumerate
games=["cricket","futsal","tt","chess","volleyball"]

for i,v in enumerate(games):
    print(f"{i}:{v}")

for index,value in enumerate(games):
    print(len(games)-index-1,value)

print(dict(list(enumerate(games))))

d={"abhijeet":9, "Mrinali":10,"kalu":7 , "samriddha":6 , "robin":"BSc CSIT"}

for i,key in enumerate(d):
    value=d[key]
    print(i,key,value)

input_list = ["apple", "banana", "apple", "orange", "banana", "pear"]

output_list=[]
for i,value in enumerate(input_list):
    if value not in output_list:
        output_list.append(value)

print(output_list)    

#Using set

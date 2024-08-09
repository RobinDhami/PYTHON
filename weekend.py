tup1 = (1,2,3,4)
tup2=(1,2,3,4)

print(tup1 is tup2) #True since tuple are immutable


f = open("weekendlog.txt","w")
f.write("Trying my best")
f.seek(20)
data=f.tell()
print(data)
f.truncate(20)
f.close()
f = open("func.py",'r')
x=f.read()
print(x)
f.close()

#When you write in existing file it will delete your all previous data before writing 
# f=open("list.txt",'w')
# f.write("Hello world")
# f.close

f=open("list.txt",'a') #Append just add data to the existing file data
f.write("Hello world")
f.close

with open("list.txt",'a') as f: #In this case we dont  need to add a f.close() it qutomatically the file everytime
    f.write("This is good")
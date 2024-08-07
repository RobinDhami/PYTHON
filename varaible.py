x="rabin"
y=10
def hello():
    global y
    y=45
    x="dhami"
    print(f"this is local variable{x}")

print(f" this is global variable {x}")
print(y)
hello()    #After the function hello is called the value of y changes to 45!!
print(y)

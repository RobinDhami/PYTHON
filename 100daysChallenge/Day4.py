#Funstion 
def sq(l):
    area = l*l
    print(f"Area of square is {area}")

sq(4)    

def circ(r):
    area = 3.14*r*r
    return area,3.14

res,pi=circ(5)
print(f"The area of circle is {res} with vakue of pie as {pi}")

name = "Robin Dhami" #Global variable
def sc():
    age = 30  #Local variable
    print(f"My name is {name} and i am {age} years old")
    print(len(locals()))
sc()
print(globals())

age=23
print(id(age))
age=32
print(id(age))

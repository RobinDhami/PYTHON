# class simple():
#     pass

# print(type(simple))

# simp = simple()
# print(type(simp)==simple()) #Here it checking if a object is equal to class type so false
# print(type(simp)==simple) 

# class Point():
#     x=10
#     y=12

# p =Point()
# del p.x
# print(p.x)  #This will throw an error cause we deleted this instance
# print(p.y)

# p.x=100
# print(p.x)

# class Area():
#     def square(self,side):
#         area=side**2 
#         print(area)   

# a =Area()
# l = int(input("Enter the length of sqaure"))
# a.square(l)

# class Rectangle:
#     def __init__(self,a,b): 
#         self.a=a
#         self.b=b
#     def area(self):
#         ar=self.a*self.b
#         print(ar)
        
# r=Rectangle(23,4)
# r.area()        


# Define the base class 'vehicle'
class Vehicle:
    def __init__(self, color, engine):
        self.color = color  # Initialize instance variable 'color'
        self.engine = engine  # Initialize instance variable 'engine'

# Define a subclass 'Tesla' inheriting from 'Vehicle'
class Tesla(Vehicle):
    def __init__(self, color, engine, autopilot):
        super().__init__(color, engine)  # Call the constructor of the superclass 'Vehicle'
        self.autopilot = autopilot  # Initialize instance variable 'autopilot'

# Example usage:
if __name__ == "__main__":
    # Create an instance of Tesla
    my_tesla = Tesla("red", "electric", True)

    # Accessing attributes
    print(f"Color: {my_tesla.color}")
    print(f"Engine: {my_tesla.engine}")
    print(f"Autopilot: {my_tesla.autopilot}")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()    


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

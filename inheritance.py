class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self, volume="medium", mood="happy"):
        print(f"Welcome to {self.name}. Volume: {volume}, Mood: {mood}")

class Cat(Animal):    
    def sound(self, volume="medium", mood="happy"):
        super().sound(volume, mood)
        print(f"I am a cat. My name is {self.name}. Volume: {volume}, Mood: {mood}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Bark", name)

    def sound(self, volume="medium", mood="happy"):
        super().sound(volume, mood)
        print(f"I am a dog. My name is {self.name}. Volume: {volume}, Mood: {mood}")

# Instantiate Cat and Dog
s = Cat("Whiskers")
a = Dog("Rex")

# Call the sound methods with parameters
s.sound(volume="loud", mood="playful")  # Output: Welcome to Whiskers. Volume: loud, Mood: playful
                                        #         I am a cat. My name is Whiskers. Volume: loud, Mood: playful

a.sound(volume="soft", mood="calm")     # Output: Welcome to Rex. Volume: soft, Mood: calm
                                        #         I am a dog. My name is Rex. Volume: soft, Mood: calm

class Parent:
    def leg(self,count):
        print(f"I have {count} legs")

class child(Parent):
    def leg(self, count):
        super().leg(count)
        if count>4 :
            print(" I am parasite")     
        else:
            print("I am a mammal")       

p = Parent()
c = child() 

c.leg(4)
p.leg(8)

#Multiple inheritance
class spiderman:
    def __init__(self,webs) -> None:
        self.webs=webs
class ironman:
    def __init__(self,ability) -> None:
            self.ability = ability

class mixed(spiderman,ironman):
    def __init__(self, ability,webs) -> None:
        self.webs=webs
        self.ability=ability

    def show(self):
        print(f"i have both {self.webs} and {self.ability} ability")

ob = spiderman("webshooter")
ob1= ironman("genius")
print(ob.webs)
print(ob1.ability)
ob3 = mixed("webshooter","machinegun")
ob3.show()

print(mixed.mro())

#Multilevel Inheritance
class A:
    def __init__(self,name) -> None:
        self.name=name

class B(A):
    def __init__(self, name,age) -> None:
        super().__init__(name)
        self.age=age    

    def show(self): 
        print(self.age)

class C(B):
    def __init__(self, name,age,location) -> None:
        self.location = location
        super().__init__(name,age)
    def display(self):
        print(f"I am {self.name} and I am {self.age} years old. I live in {self.location}" )


a = A("Hari")
b=B("Ram",20)
c=C("Laxman",90,"kalanki")
c.display()

# Base class
class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        return f"Name: {self.name}"

# Hierarchical classes
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    
    def display_employee(self):
        return f"{self.display()}, Employee ID: {self.employee_id}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def display_student(self):
        return f"{self.display()}, Student ID: {self.student_id}"

# Hybrid class
class Scholar(Student, Employee):
    def __init__(self, name, employee_id, student_id):
        Employee.__init__(self, name, employee_id)
        Student.__init__(self, name, student_id)
    
    def display_scholar(self):
        return f"{self.display_employee()}, {self.display_student()}"

class Person:
    def __init__(self,name,age) -> None: # parameterized Constructor
        self.name=name 
        self.age = age

    def employee(self):
        print(f"{self.name} is {self.age} years old")

a = Person("Rabin",24)
a.employee()
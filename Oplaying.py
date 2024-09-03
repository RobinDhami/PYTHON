class Employee():
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
        
    def welcome(self):
        print(f"Welcome  {self.name} as the possition of {self.position} ")
class Manager(Employee):
    def __init__(self,name,age,position,department,member):
        super().__init__(name,age,position)
        self.department=department
        self.member=member
    def welcome(self):
        print(f"Welcome  {self.name} at the department of {self.department} with total member of {self.member} ")    
        
class Engineer(Employee):
    def __init__(self,name,age,position,expertise,project):
        super().__init__(name,age,position)
        self.expertise=expertise
        self.project=project
    def welcome(self):
        print(f"Welcome  {self.name} as the expertise of {self.expertise} with project {self.project} ")    
e1 = Employee("John Doe", 30, "Employee")
e1.welcome()

m1 = Manager("Jane Smith", 40, "Manager", "IT", 10)
m1.welcome()

eng1 = Engineer("Alice Johnson", 28, "Engineer", "AI", 34)
eng1.welcome()

        #GG
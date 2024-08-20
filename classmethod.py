class Employee:
    company = "Apple"
    def show(self,name):
        self.name = name
        print(f"{self.name} works in {self.company}")

    @classmethod
    def changecompany(cls,changename):
        cls.company = changename
        print(f'the company has been changed to {cls.company}')    

emp = Employee()
emp.show("Rabin")
emp.changecompany("Tesla")

print(Employee.company)
print(emp.__dict__) #It wont return company name cause its the class varaible , it only return instance variable
print(dir(emp))

s ="Rabin-24-kalanki-CSIT"
l= s.split("-")
print(l)
print(dir(l))
l.sort() #Sorting is done directly on original list so it will return null if try to print it .
print(l)
print(help(Employee))
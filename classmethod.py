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
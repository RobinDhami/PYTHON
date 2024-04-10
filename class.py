# Example of class in Python . Class is encapsulation itself
class Sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b


a= int(input("Enter the first no"))
b= int(input("Enter the first no"))
s=Sum(a,b)
print(s.add())



# Lets try to solve a dsa question using class


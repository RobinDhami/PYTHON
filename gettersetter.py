class Students:
    def __init__(self) -> None:
        pass
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj = Students() 
obj.setname("Rabin")
name=obj.getname() 
print(name)      
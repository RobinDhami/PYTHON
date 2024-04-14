class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("I am a ",self.name)
#Dog child for animal parent 
class dog(Animal):
    def __init__ (self,bark):
        self.name= bark
        print("Bark" ,bark)        

s = Animal("cat")
a = dog("bark")
result = s.sound()

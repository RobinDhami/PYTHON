#Since the method overloading is not supported in python we have other ways to perform method overloading
# class polm:
#     def displayinfo(self,name=None,cast=None):
#         if name is not None and cast is not None:
#             print(f"My name is {name} {cast}")
#         elif name is not None:
#             print(f"My name is {name}")    
#         else:
#             print("I have no name")        

# obj= polm()
# obj.displayinfo()
# obj.displayinfo("rabin")
# obj.displayinfo("rabin","dhami")     

#Overriding
class animal:
    def sound(self):
        print('Animal make different sound')

class dog(animal):
    def sound(self):
        print("Bhou bhou")

class cat(animal):
    def sound(self):
        print("meow meow") 

obj = cat()
obj1 = dog()

obj.sound()
obj1.sound()


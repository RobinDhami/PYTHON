# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def sound(self, volume="medium", mood="happy"):
#         print(f"Welcome to {self.name}. Volume: {volume}, Mood: {mood}")

# class Cat(Animal):    
#     def sound(self, volume="medium", mood="happy"):
#         super().sound(volume, mood)
#         print(f"I am a cat. My name is {self.name}. Volume: {volume}, Mood: {mood}")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print("Bark", name)

#     def sound(self, volume="medium", mood="happy"):
#         super().sound(volume, mood)
#         print(f"I am a dog. My name is {self.name}. Volume: {volume}, Mood: {mood}")

# # Instantiate Cat and Dog
# s = Cat("Whiskers")
# a = Dog("Rex")

# # Call the sound methods with parameters
# s.sound(volume="loud", mood="playful")  # Output: Welcome to Whiskers. Volume: loud, Mood: playful
#                                         #         I am a cat. My name is Whiskers. Volume: loud, Mood: playful

# a.sound(volume="soft", mood="calm")     # Output: Welcome to Rex. Volume: soft, Mood: calm
#                                         #         I am a dog. My name is Rex. Volume: soft, Mood: calm

# class Parent:
#     def leg(self,count):
#         print(f"I have {count} legs")

# class child(Parent):
#     def leg(self, count):
#         super().leg(count)
#         if count>4 :
#             print(" I am parasite")     
#         else:
#             print("I am a mammal")       

# p = Parent()
# c = child() 

# c.leg(4)
# p.leg(8)

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
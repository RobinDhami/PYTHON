# class simple():
#     pass

# print(type(simple))

# simp = simple()
# print(type(simp)==simple()) #Here it checking if a object is equal to class type so false
# print(type(simp)==simple) 

# class Point():
#     x=10
#     y=12

# p =Point()
# del p.x
# print(p.x)  #This will throw an error cause we deleted this instance
# print(p.y)

# p.x=100
# print(p.x)

class Area():
    def square(self,side):
        area=side**2 
        print(area)   

a =Area()
l = int(input("Enter the length of sqaure"))
a.square(l)
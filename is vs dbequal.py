a= 4
b= "4"
print(a is b) #false
print(a==b) #false


l1 = [1,2,3,]
l2=[1,2,3]
print(l1 is l2) #False cause they are saved at differetnt memory location cause python is smart and it knows that list can be changed later
print(l1==l2) #True cause it checks value only currently

a=10
b=10
print(a is b) #True cause python is smart and it knows constant are immutable so it saves same constant at same meory location to utilize memory 

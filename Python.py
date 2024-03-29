name = input("Enter your name??\n")
if (name == "Rabin Dhami"):
    print("YOu are passed")
else:
    print("First Day")
class sum:
    def __init__(self,x,y):
        self.x = x
        self.y= y
        
    def display(self):
        sum = self.x+ self.y;
        print("sum is ",sum)
        
s = sum(2,3)

s.display()

class Fib:
    def __init__(self,n):
        self.n = n
    def calc(self):
        a,b=0,1
        print(a)
        for i in range(self.n-1):
           a = b
           b = a+b
           print(a)
           
f = Fib(20)
f.calc()

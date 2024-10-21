class Home:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mul(self):
        pro =self.x*self.y
        print(pro)

class Room(Home):
    def mul(self):
        b=self.x*self.y*5
        print(b)

h = Home(2,3)
h.mul()
r= Room(2,4)
r.mul()



        
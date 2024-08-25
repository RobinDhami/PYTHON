class Sum:
    def __init__(self, name):
        self.name = name
        print(f"My name is {self.name}")

    def add(self, x, y):
        self.x = x
        self.y = y
        result = self.x + self.y
        return f'Total sum is ({self.x} + {self.y}) = {result}'

# Create an instance of Sum
obj = Sum('Harry')

# Call the add method and print the result
print(obj.add(4, 5))

        


class Sum:
    def __init__(self,name):
        self.name=name
        print(f"My name is {self.name}")
    def _add__(self,x,y):
        self.x=x
        self.y= y
        print(f'Total sum is ({self.x}+{self.y})')


obj = Sum('Harry')
print(obj._add__(4,5))

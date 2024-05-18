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



# Lets try to solve a dsa question using class(Bubble sort)
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def display(self):
        for i in self.arr:
            print(i, end=" ")

# Example 
arr = [64, 34, 25, 12, 22, 11, 90]
b = BubbleSort(arr)
b.sort()
print("Sorted array is:")
b.display()


# Same thing but without using constructor
class BubbleSort:
    def sort(self,arr):
        n = len(arr)
        for i in range (n):
            for j in range (0,n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                   
                    
    def display(self,arr):
        for i in arr:
           print(i, end=" ")
        
        
arr = [64, 34, 25, 12, 22, 11, 90]
b = BubbleSort()
b.sort(arr)
print("Sorted array is:")
b.display(arr)        
        
                
    
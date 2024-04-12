class Surt: 
    def Bub(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

arr = [2, 4, 1, 8, 3, 0]
s = Surt()
res = s.Bub(arr)
print("Sorted arr:", res)

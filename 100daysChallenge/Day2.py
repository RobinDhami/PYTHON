import copy
l1 = [[1,2],[3,4],[4,5]]

l2 = copy.deepcopy(l1)
l3=copy.copy(l1)
l2[0].append(0)
l3[1][1]= 9

print("Original list:", l1)
print("Deep Copy list:", l2)
print("Shallow Copy",l3)
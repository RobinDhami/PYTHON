# Lets make game where we generate a random number and guess  until we get it right
import random
a = random.randint(1, 100)
flag = 0
while True:
    flag = flag+1
    key = int(input("Enter the number: "))
    if a > key:
        print("Enter higher number")
    elif a < key:
        print("Enter lower number")    
    elif a == key:
        print("Congratulations!")    
        break
print("You Guessed in try" , flag)
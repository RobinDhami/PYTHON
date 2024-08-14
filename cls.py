import random
l = ["scissor","paper","rock"]

a = input("Enter your choice : ")
data = random.choice(l)

if(a=="rock" and data=="paper"):
    print("You lost")
elif(a=="paper" and data=="scissor"):
    print("You lost")    
elif(a=="scissor" and data=="rock"):
    print("You lost") 
elif(a=="rock" and data=="rock"):
    print("You draw") 
elif(a=="paper" and data=="paper"):
    print("You draw")   
elif(a=="scissor" and data=="scissor"):
    print("You draw")             
else:
    print("You win")         
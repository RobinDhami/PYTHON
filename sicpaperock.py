import random 

game = ["scissor","paper", "rock"]
    
def main():
    choice = input("Enter your choice: ").strip().lower()
    rand = random.choice(game)
    if choice not in game:
        print("Invalid choice. Please choose 'scissor', 'paper', or 'rock'.")
        return
    print(f"Your opponent choose {rand}")
    if(choice == "scissor" and rand=="paper"):
            print("Hurray,You won ")
    elif(choice=="paper" and rand=="rock"):
        print("Hurray,You won ")
    elif(choice=="rock" and rand=="scissor"):
        print("Hurray,You won ")
    else:
        print(" You lose Try Again")
main()                    
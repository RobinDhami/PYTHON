from wordList import words
import random

def main():
    a = random.choice(words)
    b = list(a)
    n = len(b)
    print(f"Word is made up of {n} letters")
    flag=0
    while(flag>6):    
        value = input("Enter your Guess")

    
if __name__ == "__main__":
    main()
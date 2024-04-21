from wordList import words
import random

def main():
    a = random.choice(words)
    b = list(a)
    n = len(b)
    
    print(f"Word is made up of {n} letters")
    flag=0
    while(flag>5) :
        value = input("Enter your Guess")
        for x in value:
            x=x.lower()
            for y in a:
                y=y.lower()
                if x==y:
                    print(y)
                else:
                    print("_")
                    flag=flag+1
        
if __name__ == "__main__":
    main()
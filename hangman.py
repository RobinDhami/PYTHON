from wordList import words
import random

def main():
    a = random.choice(words)
    b = list(a)
    n = len(b)
    
    print(f"Word is made up of {n} letters")
    flag = 0
    guessed_word = ['_'] * n  # Initialize guessed word with underscores
    
    while flag < 5:
        value = input("Enter your Guess: ").lower()  # Convert input to lowercase
        found = False
        for i, x in enumerate(b):
            if x.lower() == value:
                guessed_word[i] = value  # Update guessed word
                found = True
        if not found:
            flag += 1  # Increase flag only if letter is not found
        print(' '.join(guessed_word))  # Print guessed word
        if '_' not in guessed_word:
            print("Congratulations! You won!")
            return
    
    print("You lost. The word was:", a)

if __name__ == "__main__":
    main()

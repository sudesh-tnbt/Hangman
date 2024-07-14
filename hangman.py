#Step 1 
import random
from hangman_words import *
from hangman_art import *

print(logo)
end_of_game = False
lives = 6
guesses = []
status = True

word = random.choice(word_list)
display = ["_"] * len(word)

while not end_of_game:
    while status:
        guess = input("Guess a letter: ")
        if guess not in guesses:
            guesses += guess
            status = False
        else:
            print(f"You've already guessed {guess}. Try again")
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                display[i] = guess
    else:
        print(f'You guessed {guess}, you lose a life')
        lives -= 1
    print(" ".join(display))
    print(stages[lives])
    if "_" not in display:
        print("You won")
        end_of_game = True
    elif lives == 0:
        print(f"You loose. Correct word was {word}")
        end_of_game = True

    status = True



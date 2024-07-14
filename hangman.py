#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
display = ["_"] * len(word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while "_" in display:
    guess = input("Guess a letter: ")
    for i in range(len(word)):
        if guess == word[i]:
            display[i] = guess
    print(display)


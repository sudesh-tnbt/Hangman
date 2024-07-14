#Step 1 
import random

end_of_game = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = random.choice(word_list)
display = ["_"] * len(word)

while not end_of_game:
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                display[i] = guess
    else:
        lives -= 1
    print(" ".join(display))
    print(stages[lives])
    if "_" not in display:
        print("You won")
        end_of_game = True
    elif lives == 0:
        print("You loose")
        end_of_game = True



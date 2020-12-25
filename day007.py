# Beginner - Hangman

# import 說明：https://www.askpython.com/python/python-import-statement

import random
# from replit import clear
# import hangman_words
from os import system
# 若只 import 檔案名稱，則使用時須加上檔名，eg. hangman_words.word_list
from hangman_words import word_list
# import hangman_art
from hangman_art import stages, logo

# 何謂 Hangman：https://en.wikipedia.org/wiki/Hangman_(game)
# Hangman 線上遊戲：https://hangmanwordgame.com/?fca=1&success=0#/
# Google for Education > Python：https://developers.google.com/edu/python/lists#for-and-in

# Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel", "education", "antenna"]
# word_list = ["aardvark", "baboon", "camel", "education", "antenna"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for _ in range(word_length):
    display.append("_")


# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
already_guessed = []
while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    
    # Use the clear() function imported from replit to clear the output between guesses.
    # clear()
    system("cls")

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for i in range(word_length):
        if guess == chosen_word[i]:
            display[i] = guess

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed the letter: {guess}")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(" ".join(display))

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1. 
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # 判斷 display 是否還包含 "_"，若未包含則表示已全部填滿，遊戲結束
    # if display.count("_") == 0:
    #     end_of_game = True
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

    
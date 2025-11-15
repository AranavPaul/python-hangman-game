#Hangman game
import random
import utility
import os
import hangman
import nltk
nltk.download('words')  # Contains english words from wordlist corpus
from nltk.corpus import words


random_words =  words.words()

# Setting chances
max_chances = 6

# Chossing random word from list
word = random.choice(random_words) 
blank_word = '_'* len(word)

checked_letter = []
#Game logic
while True:
    os.system('cls')
    
    hangman.draw_logo()
    hangman.draw_hangman(max_chances)
    utility.draw_blanks(blank_word) #Printing word's process

    #User letter choice
    user_choice = input("Guess a letter:").lower()

    #If user letter choice is in the word 
    if user_choice in word and user_choice not in checked_letter:
        checked_letter.append(user_choice)

        blank_word = utility.fill_blanks(word, blank_word, user_choice)

        #If user completes the word - Game over(win)
        if blank_word == word:
            utility.game_over("You won")
            break 

        #Next iteration of user choice starts 
        # if user does not complete the word 
        # but guess the correct letter in the word
        else:
            continue

    #If user letter choice is not in the word 
    else:
        max_chances = max_chances - 1

        if max_chances == 0:
            os.system('cls')
            hangman.draw_logo()
            hangman.draw_hangman(max_chances)
            utility.draw_blanks(blank_word) #Printing word's process
            utility.game_over(f"You lost. The word was {word}")
            break
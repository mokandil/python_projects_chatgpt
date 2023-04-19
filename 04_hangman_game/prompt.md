# ChatGPT Prompt to generate Hangman game code

Write a program that allows the user to play a game of Hangman.

The program should:

Create a list of words to be guessed.
Randomly choose a word from the list of words.
Create a list of underscores to represent the word to be guessed.
Ask the user to guess a character.
Check if the guessed character is in the word and update the list of underscores if it is.
Decrease the number of guesses left if the guessed character is not in the word.
If the user has guessed the word, print "You won" and ask the user if they want to play again.
If the user has run out of guesses, print "You lost" and ask the user if they want to play again.
If the user wants to play again, call the Hangman game function. If not, break out of the while loop and end the game.
Make sure to include docstrings for the functions and comment your code to explain how it works.
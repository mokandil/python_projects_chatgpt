import random
import os
import time

def hangman_game():
    """
    This function allows the user to play a game of Hangman.

    Parameters:
    None

    Returns:
    None
    """
    # create a list of words
    list_of_words = ["apple", "banana", "orange", "grapes", "mango", "watermelon", "pineapple", "strawberry", 
                    "blueberry", "kiwi", "pear", "peach", "cherry", "lemon", "lime", "coconut", "avocado", "papaya", "melon", "plum", "apricot", 
                    "fig", "pomegranate", "guava", "jackfruit", "tomato", "potato", "onion", "garlic", "ginger", "cucumber", "carrot", "broccoli", 
                    "cauliflower", "spinach", "cabbage", "peas", "beans", "corn", "rice", "wheat", "barley", "oats", "sugar", "salt", "pepper", "chilli", 
                    "turmeric", "cumin", "coriander", "mustard", "saffron", "vanilla", "cinnamon", "nutmeg", "cloves", "ginger", "chocolate", "coffee", "tea", 
                    "milk", "butter", "cheese", "yogurt", "cream", "egg", "meat", "fish", "pork", "beef", "chicken", "turkey", "duck", "goose", "lamb", "salmon",
                    "mouse", "printer", "remote control", "television", "video camera", "book", "envelope", "map", 
                    "newspaper", "paint", "paper", "pencil", "picture", "poster", "scissors", "stamps", "stapler", "tape"]


    def check_char_in_word(hidden_word, guessed_word, guessed_char):
        """
        This function checks if the guessed character is in the word and updates the list of underscores if it is.

        Parameters:
        hidden_word (str): The word to be guessed.
        guessed_word (list): A list of underscores representing the word to be guessed.
        guessed_char (str): The character guessed by the user.

        Returns:
        guessed_word (list): The updated list of underscores representing the word to be guessed.
        """
       
        for i in range(len(hidden_word)):
            if hidden_word[i] == guessed_char:
                guessed_word[i] = guessed_char
        return guessed_word

    # randomly choose a word from the list of words
    hidden_word = random.choice(list_of_words)
    # create a list of underscores to represent the word to be guessed
    guessed_word = ["_"] * len(hidden_word)

    # create a variable to keep track of the number of guesses
    nr_of_guesses = 6
    game_over = False

    # create a loop to keep the game running
    while nr_of_guesses > 0:
        os.system("cls")
        print(" ".join(guessed_word))
        print("\n\nYou have {} guesses left\n\n".format(nr_of_guesses))

        # ask the user to guess a character
        guessed_char = input("Guess a character: ")
        if guessed_char in hidden_word:
            guessed_word = check_char_in_word(hidden_word, guessed_word, guessed_char)

        else:
            nr_of_guesses -= 1

            # Alert the user that they have guessed the wrong character 
            os.system("cls")
            print("Wrong guess!!! You have {} guesses left".format(nr_of_guesses))
            time.sleep(1)

        # check if the user has guessed the word
        if "_" not in guessed_word:
            print(f"You won. The word was {hidden_word}")
            game_over = True

        # check if the user has run out of guesses
        if nr_of_guesses == 0:
            print(f"You lost. The word was {hidden_word}")
            game_over = True

        # check if the game is over
        if game_over:
            # ask the user if they want to play again
            play_again = input("Do you want to play again? (y/n): ")
            # if the user wants to play again, call the Hangman game function
            if play_again == "y":
                hangman_game()
            # if the user doesn't want to play again, break out of the while loop
            else:
                print("Thank you for playing the game")
                break



def main():
    """
    This function calls the hangman_game function and clears the screen.

    Parameters:
    None

    Returns:
    None
    """
    # clear the screen
    os.system("cls")
    # call the hangman game function
    hangman_game()

if __name__ == "__main__":
    main()

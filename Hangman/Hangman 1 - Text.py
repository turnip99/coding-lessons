import os

def hangman():
    clear = lambda: os.system('cls')
    play_again = "y"
    while play_again == "y":
        clear()
        print("Welcome to the hangman game!")
        word = input("Player 1 - enter a word: ")
        while not word.isalpha():
            word = input("The word must only contain letters. ")
        word = word.lower()
        guessed_letters = []
        guessed_word = "*" * len(word)
        lives = 7
        clear()
        while (lives > 0 and guessed_word != word):
            print("Lives remaining: " + str(lives))
            print("Guessed letters: " + str(guessed_letters))
            print("Word: " + str(guessed_word))
            guess = input("Player 2 - Guess a letter (lower case): ")
            while len(guess) != 1 or not guess.isalpha() or guess.lower() in guessed_letters:
                guess = input("Please enter a valid letter.")
            guess = guess.lower()
            guessed_letters.append(guess)
            clear()
            if guess in word:
                print("Success!")
                guessed_word = replace_characters(word, guessed_word, guess)
            else:
                print("Failure")
                lives-=1
        if lives == 0:
            print("You ran out of lives!")
        else:
            print("You guessed the word (with " + str(lives) + " to spare)")
        print("The word was: " + word)
        play_again = input("Play again? (y/n) ")
        while play_again != "y" and play_again != "n":
            play_again = input("Invalid input. Please enter 'y' or 'n'. ")


def replace_characters(word, guessed_word, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_word = guessed_word[:i] + letter + guessed_word[i + 1:]
    return guessed_word

hangman()
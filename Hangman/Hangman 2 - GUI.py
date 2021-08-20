from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image

lives = 0
guessed_letters = []
guessed_word = ""

class ImageLabel(Label):
    def __str__(self):
        return self.image

# Run setup window.
def run_setup_window():

    # Runs when new word is input in setup window.
    def word_input(event=None):
        word = txt_word_input.get().lower()
        # Validation.
        if not word.isalpha():
            lbl_word_input_error["text"] = "The word must only contain letters."
        else:
            lbl_word_input_error["text"] = ""
            run_guessing_window(word)  # Start guessing window configuration.

    # Configure UI.
    window_setup = Tk()
    window_setup.minsize(200, 200)
    window_setup.title("Welcome to the hangman game!")
    lbl_word_input = Label(window_setup, text="Player 1 - enter a word", font=(None, 15, BOLD))
    lbl_word_input.pack()
    txt_word_input = Entry(window_setup, font=(None, 12))
    txt_word_input.bind('<Return>', word_input)
    txt_word_input.focus_set()
    txt_word_input.pack()
    btn_word_input = Button(window_setup, text="Begin game", command=word_input, font=(None, 12))
    btn_word_input.pack()
    lbl_word_input_error = Label(window_setup, text="", fg="red", font=(None, 10))
    lbl_word_input_error.pack()
    # Start window process to launch program.
    window_setup.mainloop()


# Run guessing window.
def run_guessing_window(word):
    global lives
    global guessed_letters
    global guessed_word

    lives = 10
    guessed_letters = []
    guessed_word = "*" * len(word)

    def replace_characters(word, guessed_word, guess):
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word = guessed_word[:i] + letter + guessed_word[i + 1:]
        return guessed_word

    def show_image():
        filename = "State Images/Lives " + str(lives) + ".png"
        image = Image.open(filename)
        image_resize = image
        image_tk = ImageTk.PhotoImage(image=image_resize)
        window_guessing.update_idletasks()
        lbl_image.configure(image=image_tk)
        lbl_image.image = image_tk

    # Updates displayed game status.
    def update_details(): 
        lbl_lives["text"] = "Lives remaining: " + str(lives)
        lbl_guessed_letters["text"] = "Guessed letters: " + str(guessed_letters)
        lbl_guessed_word["text"] = "Guessed word: " + str(guessed_word)
        show_image()
        
    # Runs when a letter is guessed.
    def guess_input(event=None):
        global lives
        global guessed_letters
        global guessed_word
        guess = txt_guess_input.get().lower()
        # Validation.
        txt_guess_input.delete(0, "end")
        if len(guess) != 1 or not guess.isalpha() or guess.lower() in guessed_letters:
            lbl_guess_input_error["text"] = "Please enter a valid letter."
        else:
            lbl_guess_input_error["text"] = ""
            guessed_letters.append(guess)
            if guess in word:
                guessed_word = replace_characters(word, guessed_word, guess)
            else:
                lives-=1
            update_details()
            if guessed_word == word:
                lbl_win_lose["text"] = "You guessed the word (with " + str(lives) + " to spare)"
                lbl_win_lose.config(fg="green")
                lbl_answer.config(fg="green")
                end_game()
            elif lives == 0:
                lbl_win_lose["text"] = "You ran out of lives!"
                lbl_win_lose.config(fg="red")
                txt_guess_input.config(fg="red")
                end_game()

    # End of game process.
    def end_game():
        lbl_answer["text"] = "The word was: " + word
        btn_guess_input.config(state="disabled")
        txt_guess_input.config(state="disabled")
        txt_guess_input.unbind('<Return>')

    # Configure UI.
    window_guessing = Toplevel()
    window_guessing.minsize(400, 600)
    window_guessing.title("Guess the word!")
    lbl_lives = Label(window_guessing, text="", font=(None, 10))
    lbl_lives.pack()
    lbl_guessed_letters = Label(window_guessing, text="", font=(None, 10))
    lbl_guessed_letters.pack()
    lbl_guessed_word = Label(window_guessing, text="", font=(None, 15, BOLD))
    lbl_guessed_word.pack()

    lbl_image = Label(window_guessing)
    lbl_image.pack()

    lbl_guess_input = Label(window_guessing, text="Player 2 - Guess a letter", font=(None, 15, BOLD))
    lbl_guess_input.pack()
    txt_guess_input = Entry(window_guessing, font=(None, 12))
    txt_guess_input.bind('<Return>', guess_input)
    txt_guess_input.focus_set()
    txt_guess_input.pack()
    btn_guess_input = Button(window_guessing, text="Guess", command=guess_input, font=(None, 12))
    btn_guess_input.pack()
    lbl_guess_input_error = Label(window_guessing, text="", fg="red", font=(None, 10))
    lbl_guess_input_error.pack()
    lbl_win_lose = Label(window_guessing, text="", font=(None, 10))
    lbl_win_lose.pack()
    lbl_answer = Label(window_guessing, text="", font=(None, 15, BOLD))
    lbl_answer.pack()
    update_details()

run_setup_window()

"""
A simple program made to help me learn Japanese characters
@author Cole DenBleyker
"""
import tkinter as tk
import random

global CORRECT_POINTS
global INCORRECT_POINTS

CHARACTER_DICT = {
    "あ":"a",
    "い":"i",
    "う":"u",
    "え":"e",
    "お":"o",
    "か":"ka",
    "き":"ki",
    "く":"ku",
    "け":"ke",
    "こ":"ko",
    "が":"ga",
    "ぎ":"gi",
    "ぐ":"gu",
    "げ":"ge",
    "ご":"go"
}

class App:
    def __init__(self, window):
        window.title("Flashcards")
        window.rowconfigure([0,2], minsize=175, weight=1)
        window.columnconfigure([0, 4], minsize=100, weight=1)

        character_label = tk.Label(window, text="", font=("Serif Sans", 90))
        character_label.grid(row=0, column=0)

        correct_label = tk.Label(window, text="Correct: 0", font=("Serif Sans", 30))
        correct_label.grid(row=0, column=1)

        incorrect_label = tk.Label(window, text="Incorrect: 0", font=("Serif Sans", 30))
        incorrect_label.grid(row=1, column=1)

        answer_label = tk.Label(window, text="", font=("Serif Sans", 25))
        answer_label.grid(row=1, column=0)

        user_input = tk.Entry(window, font=("Serif Sans", 16), )
        user_input.grid(row=2, column=0)

        answer_button = tk.Button(master=window, text="Answer", command=lambda: answer(character_label, answer_label, user_input, correct_label, incorrect_label))
        answer_button.grid(row=4, column=0)

        next_button = tk.Button(master=window, text="Next Word", command=lambda: next_word(character_label, answer_label, user_input))
        next_button.grid(row=4, column=1)

        next_word(character_label, answer_label, user_input) # runs the next_word function when the program starts


def next_word(character_label, answer_label, user_input):
    """
    Gets the next character(s) at random
    """
    answer_label.config(text="")
    user_input.delete(0, 'end')
    rand_word = random.choice(list(CHARACTER_DICT.keys()))
    character_label.config(text=rand_word)

def answer(character_label, answer_label, user_input, correct_label, incorrect_label):
    """
    Checks to see if the user's input goes with the corresponding 
    """
    word = character_label['text']
    value = CHARACTER_DICT.get(word)
    if user_input.get() == value:
        answer_label.config(text="Correct Answer! \nClick the 'Next Word' \nbutton for a new word!")
        correct_score = correct_label['text']
        CORRECT_POINTS = int(''.join(filter(str.isdigit, correct_score)))
        CORRECT_POINTS +=1
        correct_label.config(text="Correct: " + str(CORRECT_POINTS))
    else:
        answer_label.config(text="Incorrect Answer. \nTry again or click the\n'Next Word' button\n for a new word!")
        incorrect_score = incorrect_label['text']
        INCORRECT_POINTS = int(''.join(filter(str.isdigit, incorrect_score)))
        INCORRECT_POINTS += 1
        incorrect_label.config(text="Incorrect: "+ str(INCORRECT_POINTS))


def score_ratio(correct, incorrect):
    pass


def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()



if __name__ == "__main__":
    main()
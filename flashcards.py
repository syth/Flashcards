"""
A simple program made to help me learn Japanese characters
@author Cole DenBleyker
"""
import tkinter as tk
import random

CORRECT_POINTS = 0
INCORRECT_POINTS = 0
TOTAL_POINTS = 0

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
        character_label.grid(row=0, column=1)

        correct_label = tk.Label(window, text="Correct: 0", font=("Serif Sans", 30))
        correct_label.grid(row=0, column=3)

        incorrect_label = tk.Label(window, text="Incorrect: 0", font=("Serif Sans", 30))
        incorrect_label.grid(row=1, column=3)

        ratio_label = tk.Label(window, text="% Accurate", font=("Sans Serif", 30))
        ratio_label.grid(row=2, column=3)

        answer_label = tk.Label(window, text="", font=("Serif Sans", 25))
        answer_label.grid(row=1, column=0)

        user_input = tk.Entry(window, font=("Serif Sans", 16), )
        user_input.grid(row=2, column=1)

        answer_button = tk.Button(master=window, text="Answer", command=lambda: answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        answer_button.grid(row=4, column=1)

        next_button = tk.Button(master=window, text="Skip Word", command=lambda: next_word(character_label, answer_label, user_input))
        next_button.grid(row=4, column=3)

        next_word(character_label, answer_label, user_input) # runs the next_word function when the program starts

        window.bind('<Return>', lambda command:answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        window.bind('<Shift_R>', lambda command:next_word(character_label, answer_label, user_input))


def next_word(character_label, answer_label, user_input):
    """
    Gets the next character(s) at random
    """
    answer_label.config(text="")
    user_input.delete(0, 'end')
    rand_word = random.choice(list(CHARACTER_DICT.keys()))
    character_label.config(text=rand_word)

def answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label):
    """
    Checks to see if the user's input goes with the corresponding 
    """
    word = character_label['text']
    global CORRECT_POINTS
    global INCORRECT_POINTS
    global TOTAL_POINTS

    value = CHARACTER_DICT.get(word)
    correct = CORRECT_POINTS
    incorrect = INCORRECT_POINTS
    total = TOTAL_POINTS

    if user_input.get() == value:
        answer_label.config(text="Correct Answer!")
        correct_score = correct_label['text']
        correct = int(''.join(filter(str.isdigit, correct_score)))
        correct +=1
        correct_label.config(text="Correct: " + str(correct))
        total += 1
    else:
        answer_label.config(text="Incorrect Answer.")
        incorrect_score = incorrect_label['text']
        incorrect = int(''.join(filter(str.isdigit, incorrect_score)))
        incorrect += 1
        incorrect_label.config(text="Incorrect: "+ str(incorrect))
        total += 1

    CORRECT_POINTS = correct
    INCORRECT_POINTS = incorrect
    TOTAL_POINTS = total

    score_ratio(correct, total, ratio_label)



def score_ratio(correct, total, ratio_label):
    """
    Creates an accuracy rating
    """
    accuracy = (correct / total)*100
    ratio = (round(accuracy, 2))
    ratio_string = str(ratio)
    ratio_label.config(text=ratio_string + "% Accurate")


def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()



if __name__ == "__main__":
    main()
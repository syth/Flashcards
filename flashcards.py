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
        window.geometry("800x650")
        window.title("Flashcards")
        window.rowconfigure([0,2], minsize=250, weight=1)
        window.columnconfigure([0, 2], minsize=250, weight=1)

        back = tk.Frame(master=window, bg="black")
        back.grid_propagate(0)


        character_label = tk.Label(window, text="", font=("Serif Sans", 130))
        character_label.grid(row=0, column=1, sticky="nsew")

        correct_label = tk.Label(window, text="Correct Guesses: 0", font=("Serif Sans", 30), fg="green", wraplength=130, justify="center")
        correct_label.grid(row=0, column=0, sticky="nsew")

        incorrect_label = tk.Label(window, text="Incorrect Guesses: 0", font=("Serif Sans", 30), fg="red", wraplength=130, justify="center")
        incorrect_label.grid(row=0, column=2, sticky="nsew")

        ratio_label = tk.Label(window, text="0.0% Accuracy", font=("Sans Serif", 25))
        ratio_label.grid(row=1, column=2, sticky="ns")

        guess_label = tk.Label(window, text="Previous Answer Result:", font=("Serif Sans", 30), wraplength=125, justify="center")
        guess_label.grid(row=1, column=0, sticky="nsew")

        answer_label = tk.Label(window, text="", font=("Serif Sans", 30))
        answer_label.grid(row=2, column=0, sticky="n")

        user_input = tk.Entry(window, font=("Serif Sans", 16), width=22)
        user_input.grid(row=2, column=1, padx=20)

        answer_button = tk.Button(master=window, text="Answer", command=lambda: answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        answer_button.grid(row=4, column=1)

        next_button = tk.Button(master=window, text="Skip Word", command=lambda: next_word(character_label, answer_label, user_input))
        next_button.grid(row=4, column=2)

        next_word(character_label, answer_label, user_input) # runs the next_word function when the program starts

        window.bind('<Return>', lambda command:answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        window.bind('<Shift_R>', lambda command:next_word(character_label, answer_label, user_input))


def next_word(character_label, answer_label, user_input):
    """
    Gets the next character(s) at random
    """

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
        answer_label.config(text="Correct Answer!", fg="green")
        correct_score = correct_label['text']
        correct = int(''.join(filter(str.isdigit, correct_score)))
        correct +=1
        correct_label.config(text="Correct Guesses: " + str(correct))
        total += 1
        next_word(character_label, answer_label, user_input)
    else:
        answer_label.config(text="Incorrect Answer.", fg="red")
        incorrect_score = incorrect_label['text']
        incorrect = int(''.join(filter(str.isdigit, incorrect_score)))
        incorrect += 1
        incorrect_label.config(text="Incorrect Guesses: "+ str(incorrect))
        total += 1
        next_word(character_label, answer_label, user_input)

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
    ratio_label.config(text=ratio_string + "% Accuracy")


def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()



if __name__ == "__main__":
    main()
"""
A simple program made to help me learn Japanese characters
@author Cole DenBleyker
"""
from tkinter import *
import random

CORRECT_POINTS = 0
INCORRECT_POINTS = 0
TOTAL_POINTS = 0

EASY_DICT = {
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
    "ご":"go",
    "さ":"sa",
    "し":"shi",
    "す":"su",
    "せ":"se",
    "そ":"so",
    "ざ":"za",
    "じ":"ji",
    "ず":"zu",
    "ぜ":"ze",
    "ぞ":"zo"
}

class App():
    def __init__(self):
        # Creates the window
        root = Tk()
        root.geometry("800x650")
        root.title("Flashcards")

        # Creates the grid for the labels
        root.rowconfigure([0,2], minsize=250, weight=1)
        root.columnconfigure([0, 2], minsize=250, weight=1)
        back = Frame(master=root, bg="black")
        back.grid_propagate(0)

        # Creates menubar 
        menubar = Menu(root)
        filemenu = Menu(menubar)
        helpmenu = Menu(menubar)
        difficulty_menu = Menu(filemenu, tearoff=0)
        language_menu = Menu(filemenu, tearoff=0)

        # Adds different sections for each menubar section
        menubar.add_cascade(menu=filemenu, label="Settings")
        menubar.add_cascade(menu=helpmenu, label="Help")

        # difficulty_menu commands
        menubar.add_command(label="Easy", command=lambda: change_difficulty(0))
        menubar.add_command(label="Medium", command=lambda: change_difficulty(1))
        menubar.add_command(label="Hard", command=lambda: change_difficulty(2))

        # language_menu commands

        # filemenu commands
        filemenu.add_cascade(label="Difficulty", menu=difficulty_menu)
        filemenu.add_cascade(label="Language", menu=language_menu)
        filemenu.add_command(label="Exit", command=lambda: root.quit())

        # helpmenu commands
        helpmenu.add_command(label="Help", command=lambda: help_section(root))
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command=lambda: about_section(root))

        # Character(s) label
        character_label = Label(root, text="", font=("Serif Sans", 130))
        character_label.grid(row=0, column=1, sticky="nsew")

        # Correct Guesses label
        correct_label = Label(root, text="Correct Guesses: 0", font=("Serif Sans", 30), fg="green", wraplength=130, justify="center")
        correct_label.grid(row=0, column=0, sticky="nsew")

        # Incorrect Guesses label
        incorrect_label = Label(root, text="Incorrect Guesses: 0", font=("Serif Sans", 30), fg="red", wraplength=130, justify="center")
        incorrect_label.grid(row=0, column=2, sticky="nsew")

        # Accuracy label
        ratio_label = Label(root, text="0.0% Accuracy", font=("Sans Serif", 25))
        ratio_label.grid(row=1, column=2, sticky="ns")

        # Previous answer label
        guess_label = Label(root, text="Previous Answer Result:", font=("Serif Sans", 30), wraplength=125, justify="center")
        guess_label.grid(row=1, column=0, sticky="nsew")

        # Previous answer result label
        answer_label = Label(root, text="", font=("Serif Sans", 30))
        answer_label.grid(row=2, column=0, sticky="n")

        # User's input
        user_input = Entry(root, font=("Serif Sans", 16), width=22)
        user_input.grid(row=2, column=1, padx=20)

        # Answer button
        answer_button = Button(master=root, text="Answer", command=lambda: answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        answer_button.grid(row=4, column=1)

        # Skip word button
        next_button = Button(master=root, text="Skip Word", command=lambda: next_word(character_label, user_input))
        next_button.grid(row=4, column=2)

        # Changes the current word
        next_word(character_label, user_input) # runs the next_word function when the program starts

        # Keybinds
        root.bind('<Return>', lambda command:answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label))
        root.bind('<Shift_R>', lambda command:next_word(character_label, user_input))
        
        root.config(menu=menubar)
        root.mainloop()


def change_difficulty(difficulty):
    """
    Change between difficulty levels
    """
    if difficulty == 0:
        # use EASY_DICT
        pass
    elif difficulty == 1:
        # use MED_DICT
        pass
    elif difficulty == 2:
        # use HARD_DICT
        pass
    else:
        # default to EASY_DICT
        pass
    

def help_section(root):
    """
    Displays a help menu
    """
    help_pop = Toplevel(root)
    help_pop.geometry("600x445")
    help_pop.title("Flashcards Help")
    Label(help_pop, text="Click settings to change settings.", font=("Serif Sans", 30), pady=20).pack()
    Label(help_pop, text="Press <Enter> to submit answer.", font=("Serif Sans", 30), pady=20).pack()
    Label(help_pop, text="Press <R-Shift> to skip the current word.", font=("Serif Sans", 30), pady=20).pack()
    Button(help_pop, text="Okay", font=("Serif Sans", 22), width=7, height=1, pady=20, command=lambda: help_pop.destroy()).pack()


def about_section(root):
    """
    Displays information pertaining about the program
    """
    about = Toplevel(root)
    about.geometry("600x445")
    about.title("About Flashcards")
    Label(about, text="Flashcards is a tool made to test memorization of Japanese.", font=("Serif Sans", 40), pady=20, wraplength=570, justify="center").pack()
    Label(about, text="This is a learning expecting - teaching me Japanese and new Python packages", font=("Serif Sans", 30), wraplength=500, justify="center", pady=10).pack()
    Button(about, text="Okay", font=("Serif Sans", 22), width=4, height=2, command=lambda: about.destroy()).place(x=300, y=400, anchor="s")
    Label(about, text="©Cole DenBleyker 2023-", font=("Serif Sans", 12), pady=-10).place(x=300, y=420, anchor="s")
    pass

def next_word(character_label, user_input):
    """
    Gets the next character(s) at random
    """
    user_input.delete(0, 'end')
    rand_word = random.choice(list(EASY_DICT.keys()))
    character_label.config(text=rand_word)

def answer(character_label, answer_label, user_input, correct_label, incorrect_label, ratio_label):
    """
    Checks to see if the user's input goes with the corresponding 
    """
    word = character_label['text']
    global CORRECT_POINTS
    global INCORRECT_POINTS
    global TOTAL_POINTS

    value = EASY_DICT.get(word)
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
        next_word(character_label, user_input)
    else:
        answer_label.config(text="Incorrect Answer.", fg="red")
        incorrect_score = incorrect_label['text']
        incorrect = int(''.join(filter(str.isdigit, incorrect_score)))
        incorrect += 1
        incorrect_label.config(text="Incorrect Guesses: "+ str(incorrect))
        total += 1
        next_word(character_label, user_input)

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



if __name__ == "__main__":
    App()
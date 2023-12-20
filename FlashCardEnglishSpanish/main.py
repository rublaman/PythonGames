import os
from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_list = {}

# ---------------------------- FILE & FILE PATHS ---------------------- #
current_dir = os.path.dirname(__file__)
csv_english_word = os.path.join(current_dir, 'data/english_words.csv')
csv_words_to_learn = os.path.join(current_dir, 'data/words_to_learn.csv')
img_path_card_back = os.path.join(current_dir, 'images/card_back.png')
img_path_card_front = os.path.join(current_dir, 'images/card_front.png')
img_path_right = os.path.join(current_dir, 'images/right.png')
img_path_wrong = os.path.join(current_dir, 'images/wrong.png')

try:
    df = pd.read_csv(csv_words_to_learn)
except FileNotFoundError:
    original_data = pandas.read_csv(csv_english_word)
    dict_list = original_data.to_dict(orient="records")
else:
    dict_list = df.to_dict(orient="records")


# ---------------------------- NEW WORD -------------------------------- #
def generate_new_word():
    global current_card
    global flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(dict_list)
    canvas.itemconfig(canvas_image, image=img_card_front)
    canvas.itemconfig(canvas_language, text="English", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="black")

    flip_timer = window.after(3000, show_result)


# ---------------------------- TRANSLATE WORD -----------+--------------- #
def show_result():
    canvas.itemconfig(canvas_language, text="Spanish", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["Spanish"], fill="white")
    canvas.itemconfig(canvas_image, image=img_card_back)


def is_known_card():
    dict_list.remove(current_card)
    data = pd.DataFrame(dict_list)
    data.to_csv(csv_words_to_learn, index=False)
    generate_new_word()


# ---------------------------- UI SETUP -------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file=img_path_card_front)
img_card_back = PhotoImage(file=img_path_card_back)
canvas_image = canvas.create_image(400, 263, image=img_card_front)
canvas_language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
img_wrong = PhotoImage(file=img_path_wrong)
button_wrong = Button(image=img_wrong, highlightthickness=0, command=generate_new_word)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file=img_path_right)
button_wrong = Button(image=img_right, highlightthickness=0, command=is_known_card)
button_wrong.grid(column=1, row=1)

flip_timer = window.after(3000, func=show_result)
generate_new_word()

window.mainloop()

import os
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FILE & FILE PATHS ---------------------- #
current_dir = os.path.dirname(__file__)
csv_english_word = os.path.join(current_dir, 'data/english_words.csv')
img_path_card_back = os.path.join(current_dir, 'images/card_back.png')
img_path_card_front = os.path.join(current_dir, 'images/card_front.png')
img_path_right = os.path.join(current_dir, 'images/right.png')
img_path_wrong = os.path.join(current_dir, 'images/wrong.png')

df = pd.read_csv(csv_english_word)
dict_list = df.to_dict(orient="records")


# ---------------------------- NEW WORD -------------------------------- #
def generate_new_word():
    canvas.itemconfig(canvas_image, image=img_card_front)
    current_card = random.choice(dict_list)
    canvas.itemconfigure(canvas_language, text="English")
    canvas.itemconfigure(canvas_word, text=current_card["English"])

    window.after(3000, show_result, current_card)


# ---------------------------- TRANSLATE WORD -------------------------- #
def show_result(current_card):
    canvas.itemconfigure(canvas_language, text="Spanish")
    canvas.itemconfigure(canvas_word, text=current_card["Spanish"])
    canvas.itemconfig(canvas_image, image=img_card_back)



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
button_wrong = Button(image=img_right, highlightthickness=0, command=generate_new_word)
button_wrong.grid(column=1, row=1)

generate_new_word()

window.mainloop()

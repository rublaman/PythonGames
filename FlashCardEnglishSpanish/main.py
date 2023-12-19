import os
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FILE PATHS ----------------------------- #
current_dir = os.path.dirname(__file__)
csv_english_word = os.path.join(current_dir, 'data/english_words.csv')
img_path_card_back = os.path.join(current_dir, 'images/card_back.png')
img_path_card_front = os.path.join(current_dir, 'images/card_front.png')
img_path_right = os.path.join(current_dir, 'images/right.png')
img_path_wrong = os.path.join(current_dir, 'images/wrong.png')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file=img_path_card_front)
canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Labels

# Buttons
img_wrong = PhotoImage(file=img_path_wrong)
button_wrong = Button(image=img_wrong, highlightthickness=0)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file=img_path_right)
button_wrong = Button(image=img_right, highlightthickness=0)
button_wrong.grid(column=1, row=1)

window.mainloop()

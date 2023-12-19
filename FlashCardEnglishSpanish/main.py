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
dict_list = [{element["English"]: element["Spanish"]} for element in dict_list]
print(dict_list)


# ---------------------------- NEW WORD -------------------------------- #
def generate_new_word():
    random_dict = random.choice(dict_list)
    random_choose = random.choice(['key', 'value'])

    if random_choose == 'key':
        result = random.choice(list(random_dict.keys()))
    else:
        result = random.choice(list(random_dict.values()))
    canvas.itemconfigure(word, text=result)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = PhotoImage(file=img_path_card_front)
canvas.create_image(400, 263, image=img_card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
img_wrong = PhotoImage(file=img_path_wrong)
button_wrong = Button(image=img_wrong, highlightthickness=0, command=generate_new_word)
button_wrong.grid(column=0, row=1)

img_right = PhotoImage(file=img_path_right)
button_wrong = Button(image=img_right, highlightthickness=0, command=generate_new_word)
button_wrong.grid(column=1, row=1)

window.mainloop()

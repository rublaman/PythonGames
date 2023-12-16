import os.path
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
current_dir = os.path.dirname(__file__)
lock_path = os.path.join(current_dir, "logo.png")
lock_image = PhotoImage(file=lock_path)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1)

window.mainloop()

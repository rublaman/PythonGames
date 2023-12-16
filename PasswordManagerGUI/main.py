import os.path
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
current_dir = os.path.dirname(__file__)
lock_path = os.path.join(current_dir, "logo.png")
lock_image = PhotoImage(file=lock_path)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2)
input_password = Entry(width=21)
input_password.grid(column=1, row=3)

# Buttons
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=add_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()

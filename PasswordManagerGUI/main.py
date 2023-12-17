import os.path
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    matrix_of_characters = [letters, numbers, symbols]
    list_of_characters = [element for row in matrix_of_characters for element in row]
    list_password = [random.choice(list_of_characters) for _ in range(random.randint(10, 15))]

    password = ''.join(list_password)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Fields empty", message=f"You should fill website, username and password field")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \n"
                                                              f"Password: {password} \nIs it ok to save?")

        if is_ok:
            current_dir_password = os.path.dirname(__file__)
            file_path = os.path.join(current_dir_password, 'data.json')

            try:
                with open(file_path, "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file_path, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open(file_path, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                input_website.delete(0, END)
                input_username.delete(0, END)
                input_password.delete(0, END)


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
input_username.insert(0, "example@mail.com")
input_password = Entry(width=17)
input_password.grid(column=1, row=3)

# Buttons
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)
button_add = Button(text="Add", width=36, command=add_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()

from tkinter import *
import os

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Lorem ipsum quest",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        current_dir = os.path.dirname(__file__)
        tomato_path = os.path.join(current_dir, 'images')
        true_image = PhotoImage(file=f"{tomato_path}/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0)
        self.button_true.grid(row=2, column=0)
        false_image = PhotoImage(file=f"{tomato_path}/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0)
        self.button_false.grid(row=2, column=1)

        self.window.mainloop()

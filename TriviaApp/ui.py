from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Lorem ipsum quest",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        current_dir = os.path.dirname(__file__)
        tomato_path = os.path.join(current_dir, 'images')
        true_image = PhotoImage(file=f"{tomato_path}/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.press_true_button)
        self.button_true.grid(row=2, column=0)
        false_image = PhotoImage(file=f"{tomato_path}/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.press_false_button)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def press_true_button(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def press_false_button(self):
        self.quiz.check_answer("False")
        self.get_next_question()
import tkinter
from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.q_text = None
        self.quiz = quiz

        self.window = Tk()
        self.window.config(width=300, height=400, bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quiz")

        self.score_label = Label(text="Score: 0", fg="white")
        self.score_label.config(bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=260, height=200)
        self.q_text = self.canvas.create_text(130, 100, width=240, text="Question text", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=html.unescape(question_text), font=("Arial", 15, "italic"))
        else:
            self.window.destroy()



    def true_pressed(self):
        self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def false_pressed(self):
        self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def close_window(self):
        self.window.destroy()

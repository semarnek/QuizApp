from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.canvas_text = self.canvas.create_text(150,125, width=280, text="Helöö", font=("Arial", 15, "italic"), fill=THEME_COLOR)


        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.true_img = PhotoImage(file="./images/true.png")

        self.true_button = Button(image=self.true_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./images/false.png")

        self.false_button = Button(image=self.false_img, bg=THEME_COLOR, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_new_question()
        self.user_answer = True
        self.window.mainloop()

    def get_new_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.true_button.config(state="active")  # state="disabled" da yapabilirsin
            self.false_button.config(state="active")
            q_text = self.quiz.next_question()

            self.canvas.itemconfig(self.canvas_text, text=q_text)

        else:
            self.canvas.itemconfig(self.canvas_text, text=f"Quiz is Over\nYour score is {self.quiz.score}")
            self.window.after(5000, self.window.destroy)


    def is_true(self):
        self.user_answer = True
        ans = self.quiz.check_answer(str(self.user_answer))
        self.result(ans)

    def is_false(self):
        self.user_answer = False
        ans = self.quiz.check_answer(str(self.user_answer))
        self.result(ans)

    def result(self, answer):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if answer:
            self.canvas.configure(bg="green")

        else:
            self.canvas.configure(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_new_question)
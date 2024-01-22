from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -----------pandas-------------

data = pandas.read_csv("french_words.csv")
yet_to_learn = data.to_dict(orient="records")
current_card = {}


# --------------picking random word -----------

def next_word():
    global current_card
    window.after(3000, flip_card)
    current_card = random.choice(yet_to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_image)


# ----------- Flipping card ------------------

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    yet_to_learn.remove(current_card)
    next_word()


# --------------------UI----------------------

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy cards")

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 48, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# card_back = Canvas()
# card_back_image = PhotoImage(file="card_back.png")
# card_back.create_image(800, 526, image=card_back_image)

wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_word()
window.mainloop()

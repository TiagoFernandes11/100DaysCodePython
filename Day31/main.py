from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -----------pandas-------------

data = pandas.read_csv("french_words.csv")


# --------------picking random word -----------

def pick_word():
    random_word_index = random.randint(0, 100)
    return data["French"][random_word_index], data["English"][random_word_index]


word = pick_word()
print(word[0] + " " + word[1])

# --------------------UI----------------------

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy cards")

canvas = Canvas(width=800, height=526)
canvas_image = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=canvas_image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("Arial", 48, "italic"))
canvas.create_text(400, 263, text=word[0], font=("Arial", 60, "bold"))

# card_back = Canvas()
# card_back_image = PhotoImage(file="card_back.png")
# card_back.create_image(800, 526, image=card_back_image)

wrong_button_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="right.png")
right_button = Button(image=right_button_image, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()

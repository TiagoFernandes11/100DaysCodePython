from tkinter import *

THEME_COLOR = "#375362"

score = 0

window = Tk()
window.config(width=300, height=400, bg=THEME_COLOR, padx=20, pady=20)
window.title("Quiz")

score_label = Label(text=f"Score: {score}")
score_label.config(bg=THEME_COLOR, highlightthickness=0)
score_label.grid(column=1, row=0)

canvas = Canvas(width= 260, height=200)
canvas.create_text(130, 100, text="Frase vai aqui", font=("Arial", 22, "bold"))
canvas.grid(column=0, row=1, columnspan=2)

pad = Canvas(width=260, height=20)
pad.config(bg=THEME_COLOR, highlightthickness=0)
pad.grid(column=0, row=2, columnspan=2)

false_image = PhotoImage(file="images/false.png")
false_button = Button(image=false_image)
# false_button.config(height=50, width=50)
false_button.grid(column=0, row=3)

true_image = PhotoImage(file="images/true.png")
# true_image.config(height=50, width=50)
true_button = Button(image=true_image)
true_button.grid(column=1, row=3)


window.mainloop()



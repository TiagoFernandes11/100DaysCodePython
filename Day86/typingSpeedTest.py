from tkinter import Tk, Label, Text, Button
from time import *


def check_answer():
    if text_label.cget("text") == text.get(1.0, "end-1c"):
        print(str((time() - start) / len(text_label.cget("text"))) + "letters/ssecond")
    else:
        print("something wrong with your text")


window = Tk()
window.title("Typing Speed")
text_label = Label(text="Copy this text")
text_label.grid(row=0, column=1)
text = Text()
text.grid(row=1, column=1)
button = Button(text="check asnwer", command=check_answer)
button.grid(row=2, column=1)

start = time()

window.mainloop()

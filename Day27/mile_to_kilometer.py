from tkinter import *

window = Tk()
window.minsize(200, 100)
window.config(padx=20, pady=20)
window.title("Mile to kilometer")

kilometers = 0

input_miles = Entry()
input_miles.grid(column=0, row=0)


def convert():
    global kilometers
    kilometers = float(input_miles.get()) * 1.6
    is_equals_label = Label(text="is equals to " + str(kilometers) + " kilometers")
    is_equals_label.grid(column=0, row=1)


miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0)

is_equals_label = Label(text="is equals to " + str(kilometers) + " kilometers")
is_equals_label.grid(column=0, row= 1)

button = Button(text="convert", command=convert)
button.grid(column=0, row=2)

window.mainloop()
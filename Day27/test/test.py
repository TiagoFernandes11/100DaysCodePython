import tkinter

window = tkinter.Tk()
window.title("My first tkinter program")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label", font=("arial", 24, "italic"))
my_label.pack()


def button_clicked():
    my_label.config(text="Button got clicked")
    new_label = tkinter.Label(text=my_input.get(), font=("arial", 24, "bold"))
    new_label.pack()


my_button = tkinter.Button()
my_button.config(text="Click me", command=button_clicked)
my_button.pack()

my_input = tkinter.Entry()
my_input.pack()

window.mainloop()

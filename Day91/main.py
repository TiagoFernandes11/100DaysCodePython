import time
from tkinter import Tk, Label, Text

window = Tk()
window.title("Keep writing")

seconds_left = 5

label = Label(text="text will auto delete in 5s after you stop writing")
text_block = Text()

label.pack()
text_block.pack()


def restart_timer(event):
    global seconds_left
    seconds_left = 5
    print("time reseted")


while seconds_left >= 0:
    window.bind('<KeyPress>', restart_timer)
    if seconds_left == 0:
        window.destroy()
    time.sleep(1)
    seconds_left -= 1
    window.update()

window.mainloop()

from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = Canvas(width=260, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130, 80, image=logo_img)
canvas.grid(column=0, row=0)

website_input_label = Label(text="Website")
website_input_label.grid(column=0, row=1)

website_input = Entry()
website_input.grid(column=1, row=1)

username_input_label = Label(text="Email/Username")
username_input_label.grid(column=0, row=2)

username_input = Entry()
username_input.grid(column=1, row=2)

password_input_label = Label(text="Password")
password_input_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3)

generate_password_button = Button(text="generate password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="add")
add_button.grid(column=1, row=4)


window.mainloop()
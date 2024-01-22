from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    final_password = ""

    nr_letters = 4
    nr_numbers = 4
    nr_symbols = 4

    randomizer = []

    for i in range(nr_letters + nr_numbers + nr_symbols):
        randomizer.append(random.randint(0, 2))

    for i in range(len(randomizer)):
        if randomizer[i] == 0:
            final_password += letters[random.randint(0, len(letters) - 1)]
        elif randomizer[i] == 1:
            final_password += numbers[random.randint(0, len(numbers) - 1)]
        elif randomizer[i] == 2:
            final_password += symbols[random.randint(0, len(symbols) - 1)]

    return final_password


def complete_password_random():
    password_input.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if password_input.get() != "" and username_input.get() != "" and password_input.get() != "":
        with open("passwords.txt", "a") as file:
            file.write(website_input.get() + " | " + username_input.get() + " | " + password_input.get() + "\n")
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)
        messagebox.showinfo("Success", "Entry was saved")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

website_input_label = Label(text="Website")
website_input_label.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input_label = Label(text="Email/Username")
username_input_label.grid(column=0, row=2)

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)

password_input_label = Label(text="Password")
password_input_label.grid(column=0, row=3)

password_input = Entry()
password_input.grid(column=1, row=3)

generate_password_button = Button(text="generate password", command=complete_password_random)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="add", width=10, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()

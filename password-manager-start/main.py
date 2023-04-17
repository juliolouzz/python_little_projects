from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # data_file.write(f"{website} | {email} | {password}\n") # this is for .txt file

                    # Reading old data
                    data = json.load(data_file)

            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD FUNCTION ------------------------------- #

def find_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

            try:
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} "
                                                           f"\nPassword: {data[website]['password']}")
            except KeyError:
                messagebox.showwarning(title="Error", message="No details for the website exists.")

    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning(title="Error", message="No Data File Found.")

# Other way to do find password function, if you can solve with if else, prefer it!!!
# def find_password():
#     website = entry_website.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showwarning(title="Error", message="No Data File Found.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
#         else:
#             messagebox.showwarning(title="Error", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels

website_txt = Label(text="Website:")
website_txt.grid(row=1, column=0)

email_username_txt = Label(text="Email/Username:")
email_username_txt.grid(row=2, column=0)

password_txt = Label(text="Password:")
password_txt.grid(row=3, column=0)

# Entry

entry_website = Entry(width=33)
entry_website.grid(row=1, column=1)
entry_website.focus()

entry_email = Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "julio.cdl.vet@gmail.com")

entry_password = Entry(width=33)
entry_password.grid(row=3, column=1)

# Buttons

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

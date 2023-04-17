# this import make easier when you call a lot of classes on your code

from tkinter import *


# Button function

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Creating a window

window = Tk()
window.title("My First GUI program")
window.wm_minsize(width=500, height=300)
window.config(padx=50, pady=50)  # space inside the window around text, buttons, etc...

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # space between label and widgets inside the window

# update or change label config

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)

# New button

button2 = Button(text="New Button")
button2.grid(column=2, row=0)







window.mainloop()

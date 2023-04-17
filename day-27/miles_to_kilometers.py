from tkinter import *


def convert():
    n_miles = float(miles_input.get())
    n_km = round(n_miles * 1.609344, 2)
    result.config(text=f"{n_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to ")
is_equal_to.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()

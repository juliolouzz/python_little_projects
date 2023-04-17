from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Reading and applying data to the flashcard with pandas

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  # create a random dict of French word an English word
    # print(current_card["French"]) # to test it
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    generate_word()


# Create window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create canvas for images

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
language_txt = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

wrong_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=wrong_image, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR,
                     command=generate_word)
left_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR,
                      command=is_known)
right_button.grid(row=1, column=1)

generate_word()  # to start the card as soon you start the program

window.mainloop()

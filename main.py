from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# -----------------------READ DATA------------------------------------
data = pandas.read_csv("./data/french_words.csv")
data_as_dict = pandas.DataFrame.to_dict(data, orient="records")
print(data_as_dict)
current_card = {}
known_words = []
unknown_words = []

# flip_timer = 0

def next_card():
    global current_card, flip_timer
    #reset the timer
    # window.after_cancel(flip_timer)
    current_card = random.choice(data_as_dict)
    print(current_card)
    #modify canvas text
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    #set the timer to flip after 3 second
    flip_timer = window.after(3000, flip_flashcard())


def flip_flashcard():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


# def known_words():
#     global known_words
#     return known_words.append(current_card)


# -----------------------UI--------------------------------------


window = Tk()
window.title("Flashy")
window.minsize(width=900, height=626)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_flashcard)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410, 270, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=known_words)
right_button.grid(row=1, column=1)

# call this function so to show a card when start
next_card()

window.mainloop()

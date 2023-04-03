from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(width=900, height=626)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(410, 270, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Label
title = Label(canvas, text="Title", font="Arial 40 italic")
title.place(x=400, y=150)

word = Label(canvas, text="word", font="Arial 60 bold")
word.place(x=400, y=263)

# Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, bd=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, bd=0, padx=0, pady=0)
right_button.grid(row=1, column=1)


window.mainloop()


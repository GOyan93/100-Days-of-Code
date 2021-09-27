from tkinter import *
import pandas as pd
import random

# Variables
BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv("data/french_words.csv")
list_word_pairs = df.to_dict("records")


### FUNCTIONS ###

def generate_word():
    chosen_pair = random.choice(list_word_pairs)
    french_word = chosen_pair['French']
    english_word = chosen_pair["English"]
    canvas.itemconfig(displayed_word, text=f"{french_word}")





### UI INTERFACE ###
window = Tk()
window.config(bg= BACKGROUND_COLOR, padx= 50, pady= 50)
window.title("Flashy")



# UI Widget Creation
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file= "images/card_back.png")
image_correct_button = PhotoImage(file= "images/right.png")
image_wrong_button = PhotoImage(file= "images/wrong.png")

canvas = Canvas(width= 800, height= 525)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.create_image(400, 251, image= image_card_front)
title = canvas.create_text(400, 150, text="French", font= ("Arial", 40, "italic"))
displayed_word = canvas.create_text(400, 263, text= "trouve", font= ("Arial", 40, "bold"))

button_correct = Button(image= image_correct_button, bg = BACKGROUND_COLOR, highlightthickness= 0, relief= "flat", command=generate_word)
button_wrong = Button(image= image_wrong_button, bg = BACKGROUND_COLOR, highlightthickness= 0, relief= "flat", command=generate_word)


# UI Widget Layout
canvas.grid(row=0, column= 0, columnspan=2)
button_correct.grid(row= 1, column= 1)
button_wrong.grid(row= 1, column= 0)



window.mainloop()

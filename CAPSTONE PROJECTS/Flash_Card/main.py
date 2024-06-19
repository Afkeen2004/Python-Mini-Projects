import csv
import random
import os
import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_word = ""
current_word_loc = None
eng_mode = False
timer = None

def load_words():
    if os.path.exists('data/words_to_learn.csv'):
        file_path = 'data/words_to_learn.csv'
    else:
        file_path = 'data/french_words.csv'
    words = pd.read_csv(file_path).values.tolist()
    return words

def save_words(words):
    df = pd.DataFrame(words, columns=["French", "English"])
    df.to_csv('data/words_to_learn.csv', index=False)

def new_french_word():
    global current_word, current_word_loc, words
    if words:
        current_word, english_word = random.choice(words)
        current_word_loc = words.index([current_word, english_word])
        return current_word
    else:
        return "No more words!"

def english_translate_word():
    global current_word, current_word_loc, words
    if words:
        return words[current_word_loc][1]
    else:
        return "No more words!"

def right_press():
    global words, current_word_loc, timer
    if words:
        words.pop(current_word_loc)
        save_words(words)
        new_word = new_french_word()
        canvas.itemconfig(word, text=new_word)
        if eng_mode:
            switch_lang()
        if timer is not None:
            window.after_cancel(timer)
        timer = window.after(3000, switch_lang)

def wrong_press():
    global timer
    new_word = new_french_word()
    canvas.itemconfig(word, text=new_word)
    if eng_mode:
        switch_lang()
    if timer is not None:
        window.after_cancel(timer)
    timer = window.after(3000, switch_lang)

def switch_lang():
    global eng_mode, current_word
    if not eng_mode:
        translated_word = english_translate_word()
        canvas.itemconfig(image_on_canvas, image=english_img)
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(word, text=translated_word, fill="white")
    else:
        new_word = new_french_word()
        canvas.itemconfig(image_on_canvas, image=french_img)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=new_word, fill="black")
    eng_mode = not eng_mode
    global timer
    timer = window.after(3000, switch_lang)

words = load_words()

window = Tk()
window.title("Flash Cards - French")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

img1 = PhotoImage(file="images/right.png")
button1 = Button(image=img1, highlightthickness=0, command=right_press)
button1.grid(row=1, column=1)
img2 = PhotoImage(file="images/wrong.png")
button2 = Button(image=img2, highlightthickness=0, command=wrong_press)
button2.grid(row=1, column=0)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
french_img = PhotoImage(file="images/card_front.png")
english_img = PhotoImage(file="images/card_back.png")

image_on_canvas = canvas.create_image(400, 270, image=french_img)
title = canvas.create_text(400, 150, text="French", font=TITLE_FONT)
word = canvas.create_text(400, 263, text=new_french_word(), font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

timer = window.after(3000, switch_lang)

window.mainloop()

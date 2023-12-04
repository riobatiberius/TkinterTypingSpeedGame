from tkinter import *
from tkinter import messagebox
import random

timeleft = 60


def timer():
    global timeleft,i
    if timeleft > 0:

        timeleft -= 1
        time_countLabel.config(text=timeleft)
        time_countLabel.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        result = correct_word - wrong_word
        instructionLabel.config(text=f"Correct words {correct_word}\n Wrong Words {wrong_word}\n Final Score {result}")
        res=messagebox.askyesno("Confirm," "Do you want to play?")
        if res:
            i=0
            timeleft=60
            countLabel.config(text="0")
            time_countLabel.config(text="60")
            wordEntry.config(state=NORMAL)
            instructionLabel.config(text="Type Word And Hit Enter")


correct_word = 0
wrong_word = 0
i = 0


def play_game(event):
    if wordEntry.get()!="":
        global i, correct_word, wrong_word
        i += 1
        countLabel.config(text=i)

        instructionLabel.config(text="")
        if timeleft == 60:
            timer()

        if wordEntry.get() == word_List_Label["text"]:
            correct_word += 1
        else:
            wrong_word += 1

        random.shuffle(word_list)
        word_List_Label.config(text=word_list[0])
        wordEntry.delete(0, END)

word_list = [
    "keyboard", "mouse", "Intelligent", "philosophy", "love", "retire", "abandoned",
             "lied", "abc", "Nairobi","lwanda", "rwanda", "micky", "death","speed", "index", "icon",
             "project", "December", "May", "come", "loved", "suicide", "cried", "moving",
             "cargo", "birds", "hen", "died", "digest", "railway", "run",
             "nice", "potato", "Killer", "Name", "bring", "pen", "index"
             ]
sliderwords = ''
count = 0


def slider():
    global sliderwords, count
    text = "Welcome To Rioba's Typing Speed Game"
    if count >= len(text):
        count = 0
        sliderwords = ""
    sliderwords = sliderwords + text[count]
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(200, slider)


root = Tk()

root.title("HELLO THIS IS THE TYPING GAME")
root.iconbitmap("favicon.ico")
root.geometry("800x700+200+5")
root.resizable(0, 0)
root.config(background="green")

logoImage = PhotoImage(file="bot.png")
logoLabel = Label(root, image=logoImage, background="yellow")
logoLabel.place(x=250, y=50)

movingLabel = Label(root, text="Welcome To Rioba's Typing Speed Game", background="green", font=("arial", 25, "bold italic"),
                    foreground="red",width=30)
movingLabel.place(x=0, y=10)
slider()

random.shuffle(word_list)
word_List_Label = Label(root, text=word_list[0], font=("cooper black", 38, "italic bold "), background="yellow")
word_List_Label.place(x=350, y=350, anchor=CENTER)

wordLabel = Label(root, text="Words", font=("Castellar", 28, "italic bold"), background="green")
wordLabel.place(x=80, y=100)

countLabel = Label(root, text="0", font=("Castellar", 28, "bold"), background="yellow")
countLabel.place(x=100, y=170)

timeLabel = Label(root, text="Timer", font=("Castellar", 28, "italic bold"), background="green")
timeLabel.place(x=550, y=100)

time_countLabel = Label(root, text="60", font=("Castellar", 28, "bold"), background="yellow")
time_countLabel.place(x=570, y=170)

wordEntry = Entry(root, font=("arial", 25, "bold"), bd=8, justify=CENTER)
wordEntry.place(x=200, y=400)
wordEntry.focus_set()

instructionLabel = Label(root, text="Type Word And Hit Enter", font=("Chiller", 28, "italic bold"), background="green",
                         foreground="red")
instructionLabel.place(x=200, y=490)

root.bind("<Return>", play_game)

root.mainloop()
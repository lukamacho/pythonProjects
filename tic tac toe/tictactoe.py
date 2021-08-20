# This is a sample Python program for playing well-known game tic tac toe.
from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = 'x'

            if check_winner() is False:
                player = players[1]
                label.config(text=player+"'s turn")
            elif check_winner() is True:
                label.config(text=player+" won")
            elif check_winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]['text'] = 'o'

            if check_winner() is False:
                player = players[0]
                label.config(text=player + "'s turn")
            elif check_winner() is True:
                label.config(text=player + " won")
            elif check_winner() == "Tie":
                label.config(text="Tie")


def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] !="":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        return "Tie"
    else:
        return False

def empty_spaces():

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return True;

    for row in range(3):
        for col in range(3):
             buttons[row][col].config(bg="yellow")
    return False

def new_game():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

    global player
    player = random.choice(players)
    label.config(text=player+"'s turn")

window = Tk()
window.title("Tic-Tac-Toe game.")

players = ["luka", "akaki"]

player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + "'s turn",font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame,  text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda row=row, column=col: next_turn(row,column))
        buttons[row][col].grid(row=row,column=col)
window.mainloop()

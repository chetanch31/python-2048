from tkinter import *
from PIL import ImageTk, Image
import random
import numpy as np
import constants


root = Tk()
root.title("2048")
root.geometry("600x600")

gameTitle = Label(root, text="Game-2048")
gameTitle.config(font=("Times New Roman", 30))
gameTitle.pack()

gameWindow = Frame(root)
gameWindow.pack()

canvas = Canvas(gameWindow, height=400, width=400, bg='white')
canvas.pack(fill=BOTH, expand=False)

Board = np.zeros((4,4))

num0 = ImageTk.PhotoImage(Image.open("images/0.jpg"))
num2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
num4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
num8 = ImageTk.PhotoImage(Image.open("images/8.jpg"))
num16 = ImageTk.PhotoImage(Image.open("images/16.jpg"))
num32 = ImageTk.PhotoImage(Image.open("images/32.jpg"))
num64 = ImageTk.PhotoImage(Image.open("images/64.jpg"))
num128 = ImageTk.PhotoImage(Image.open("images/128.jpg"))
num256 = ImageTk.PhotoImage(Image.open("images/256.jpg"))
num512 = ImageTk.PhotoImage(Image.open("images/512.jpg"))
num1024 = ImageTk.PhotoImage(Image.open("images/1024.jpg"))
num2048 = ImageTk.PhotoImage(Image.open("images/2048.jpg"))

ImageNames = {
	0:num0,
	2:num2,
	4:num4,
	8:num8,
	16:num16,
	32:num32,
	64:num64,
	128:num128,
	256:num256,
	512:num512,
	1024:num1024,
	2048:num2048
}



def get_x_y_coordinate(row, column):
	x = column * 100
	y = (3-row) * 100
	return x, y

def create_board():
	for row in range(4):
		for column in range(4):
			x1, y1= get_x_y_coordinate(row, column)
			x2, y2= x1 + 100, y1+100
			canvas.create_rectangle(x1, y1, x2, y2)

create_board()

def get_key(dict_name, val):
	for key, value in dict_name.items():
		if val == value:
			return key

def drawEmpty():
	for i in constants.positions.values():
		canvas.create_image(i, image=num0)

def placeRandomTile():
	if not np.any(Board == 0):
		pass
	randomVal = random.choice([2,4])
	blank = np.argwhere(Board == 0)
	randpos = random.choice(blank)
	inlist = randpos.tolist()
	pos = get_key(constants.BoardPos, inlist)
	
	canvas.create_image(constants.positions[pos], image=ImageNames[randomVal])

def getStartBoard():

	drawEmpty()

	randPos1 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)
	randNo1 = random.choice([2, 4])
	if randNo1 == 2:
		canvas.create_image(constants.positions[randPos1], image=num2)
	else:
		canvas.create_image(constants.positions[randPos1], image=num4)

	randPos2 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)
	if randPos1 == randPos2:
		randPos2 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)

	randNo2 = random.choice([2, 4])
	if randNo2 == 2:
		canvas.create_image(constants.positions[randPos2], image=num2)
	else:
		canvas.create_image(constants.positions[randPos2], image=num4)

	x1,y1 = constants.BoardPos[randPos1]
	x2,y2 = constants.BoardPos[randPos2]

	Board[x1,y1] = randNo1
	Board[x2,y2] = randNo2

	print(Board)

getStartBoard()

def moveleft(Event):
	global Board
	for row_index, row in enumerate(Board):
		Board[row_index] = sorted(row, key=bool, reverse=True)
		current_index = Board[row_index][0]
		for i in range(1, 4):
			if current_index == Board[row_index][i] and Board[row_index][i] != 0:
				Board[row_index][i-1] *= 2
				Board[row_index][i] = 0
			current_index = Board[row_index][i]
		Board[row_index] = sorted(row, key=bool, reverse=True)
	for row_index,row in enumerate(Board):
		for index, element in enumerate(row):
			pos = get_key(constants.BoardPos, [row_index, index])
			canvas.create_image(constants.positions[pos], image=ImageNames[element])
	placeRandomTile()
	print(Board)

root.bind("<Left>",moveleft)


root.mainloop()


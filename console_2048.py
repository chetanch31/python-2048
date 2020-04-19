import numpy as np 
import constants
import random
import sys

Board = np.zeros((4,4))

def Start():
        randPos1 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)
        randNo1 = random.choice([2, 4])
        randPos2 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)
        if randPos2 == randPos1:
                randPos2 = random.choice(constants.y_axis_labels) + random.choice(constants.x_axis_labels)
        randNo2 = random.choice([2, 4])

        x1,y1 = constants.BoardPos[randPos1]
        x2,y2 = constants.BoardPos[randPos2]

        Board[x1,y1] = randNo1
        Board[x2, y2] = randNo2

        print(Board)

def isValid():
    for row in Board:
        for index in range(len(row)-1):
            if row[index] == row[index+1]:
                return True

    for column in range(4):
        row = Board[:, column]
        for index in range(len(row)-1):
            if row[index] == row[index+1]:
                return True

def endGame():
    sys.exit("Game Over")

def placeRandom():
    try:
        blank = np.argwhere(Board == 0)
        randomVal = random.choice([2,4])
        randompos = random.choice(blank)
        x1, y1 = randompos
        Board[x1,y1] = randomVal
        print(Board)
    except IndexError:
        if isValid():
            pass
        else:
            endGame()


def slide_row(row):
    nonzero = row[row!=0]
    if len(nonzero) == 4 and nonzero[0] == nonzero[1] and nonzero[2]== nonzero[3]:
        return np.array([nonzero[:2].sum(), nonzero[2:].sum(),0,0])
    for i in range(len(nonzero)-1):
        if nonzero[i] == nonzero[i+1]:
            nonzero[i] += nonzero[i+1]
            nonzero[i+1] = 0
            nonzero = nonzero[nonzero!=0]
            break
    new_row = np.zeros(4)
    new_row[:len(nonzero)] = nonzero
    return new_row           

def moveLeft():
    for row_index, row in enumerate(Board):
        newRow = slide_row(row)
        Board[row_index] = newRow
    placeRandom()

def moveRight():
    for row_index, row in enumerate(Board):
        getrow = slide_row(row[::-1])
        newrow = getrow[::-1]
        Board[row_index] = newrow
    placeRandom()

def moveUp():
    for column in range(4):
        row = Board[:, column]
        newrow = slide_row(row)
        Board[:, column] = newrow
    placeRandom()


def moveDown():
    for column in range(4):
        row = Board[:, column]
        getrow = slide_row(row[::-1])
        newrow = getrow[::-1]
        Board[:, column] = newrow
    placeRandom()


def main():
        Start()
        GameOver = False
        while not GameOver:
                move = input("Enter your next move: ")
                if move.lower() == "d":
                        moveRight()
                elif move.lower() == "s": 
                        moveDown()
                elif move.lower() == "a": 
                        moveLeft()
                elif move.lower() == "w":
                        moveUp()
                else:
                        print("Invalid Move")

if __name__ == "__main__":
    main()

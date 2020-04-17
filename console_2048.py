import numpy as np 
import constants
import random

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

def placeRandom():
    blank = np.argwhere(Board == 0)
    randomVal = random.choice([2,4])
    randompos = random.choice(blank)
    x1, y1 = randompos
    Board[x1,y1] = randomVal
    print(Board)

def operateRowleft(row):
    output_array = []
    num_zeros_to_append = 0
    current_value = 0
    for elem in row:
        if elem == 0:
            num_zeros_to_append += 1
        elif current_value == 0:
            current_value = elem
        else:
            if elem == current_value:
                current_value = 0
                num_zeros_to_append += 1
                output_array.append(2 * elem)
            else:
                output_array.append(current_value)
                current_value = elem
    if current_value != 0:
        output_array.append(current_value)
    for _ in range(num_zeros_to_append):
        output_array.append(0)
    return output_array

def operateRowRight(row):
    output_array = []
    num_zeros_to_append = 0
    current_value = 0
    for elem in row:
        if elem == 0:
            num_zeros_to_append += 1
        elif current_value == 0:
            current_value = elem
        else:
            if elem == current_value:
                current_value = 0
                num_zeros_to_append += 1
                output_array.insert(0, 2 * elem)
            else:
                output_array.insert(0, current_value)
                current_value = elem
    if current_value != 0:
        output_array.insert(0, current_value)
    
    for _ in range(num_zeros_to_append):
        output_array.insert(0, 0)
    return output_array
           

def moveLeft():
        for row_index, row in enumerate(Board):
                newRow = operateRowleft(row)
                Board[row_index] = newRow
        placeRandom()
        print(Board)

def moveRight():
        for row_index, row in enumerate(Board):
                newRow = operateRowRight(row)
                Board[row_index] = newRow
        placeRandom()
        print(Board)

def moveUp():
        pass

def moveDown():
        pass




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

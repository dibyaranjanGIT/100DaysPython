print("Welcome to the Treasuer Game !!")

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")

try:
    row, column = int(position[0]), int(position[1])
    map[row - 1][column - 1] = 'X  '
    print(f"{row1}\n{row2}\n{row3}")
except:
    print("The index is out of reach")


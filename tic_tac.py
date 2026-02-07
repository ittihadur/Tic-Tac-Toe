# Starting menu 

print("Welcome to Tic Tac Toe")

print("Choose game mode using numbers \n ")
print("1) Player vs Player")
print("2) Player vs computer")
while True:
    input_by_player = input()
    if input_by_player.isdigit() == True:
        conversion = int(input_by_player)
        if conversion == 1:
            print("Player vs Player")
            break
        elif conversion == 2:
            print("Player vs Computer")
            break
        else:
            print("Invalid Choice")
            continue
    else:
        print("Invalid choice")
        continue


#Creating the board.

print("Press X and O to play")

board = [i * 1 for i in range(0,9)]


print("+" + "---+" * 3)
for i in range(0, 9, 3):
    print("|", end="")
    for j in range(3):
        print(f" {board[i+j]} |", end="")
    print()
    print("+" + "---+" * 3)

place_X = input("Press x ONLY!! :")

while True:
    place_for_X = input("Choose froom position 0 to 8 to place X: " )
    if place_for_X.isdigit() == True:
        conversion = int(place_for_X)
        if conversion < 0 or conversion > 8:
            print("Write within the parameter 1 to 9 u dummy")
            continue
        
        else:
            print(f"Valid Input {conversion}")
            break
    else:
        print("Just a number bruv")
        continue

# Checking If X wins
# Top row
if board[0] == board [1] == board[2] :
    print("X wins")
# middle row
elif board[3] == board [4] and board[5] == "X":
    print("X wins")
# Last row
elif board[6] == board [7] and board[8] == "X":
    print("X wins")
# Left diagonal
elif board[0] == board [4] and board[8] == "X":
    print("X wins")
# Right diagonal
elif board[2] == board [4] and board[6] == "X":
    print("X wins")
# Left column
elif board[0] == board [3] and board[6] == "X":
    print("X wins")
# Right column
elif board[2] == board [5] and board[8] == "X":
    print("X wins")
elif board[1] == board [4] and board[7] == "X":
    print("X wins")


# Checking for O wins
# Top row
if board[0] == board [1] and board[2] == "O":
    print("O wins")
# middle row
elif board[3] == board [4] and board[5] == "O":
    print("O wins")
# Last row
elif board[6] == board [7] and board[8] == "O":
    print("O wins")
# Left diagonal
elif board[0] == board [4] and board[8] == "O":
    print("O wins")
# Right diagonal
elif board[2] == board [4] and board[6] == "O":
    print("O wins")
# Left column
elif board[0] == board [3] and board[6] == "O":
    print("O wins")
# Right column
elif board[2] == board [5] and board[8] == "O":
    print("O wins")
elif board[1] == board [4] and board[7] == "O":
    print("O wins")



    










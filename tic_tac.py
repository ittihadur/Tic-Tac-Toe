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

#place_X = input("Press x ONLY!! :")

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


    










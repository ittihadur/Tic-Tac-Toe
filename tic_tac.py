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

# Function to display the board
def display_board():
    print("+" + "---+" * 3)
    for i in range(0, 9, 3):
        print("|", end="")
        for j in range(3):
            print(f" {board[i+j]} |", end="")
        print()
        print("+" + "---+" * 3)

place_X = input("Press x ONLY!! :")


# Function for player move
def player_move(board, player):
    while True:
        try:
            position = int(input(f"Player {player}, choose position 0-8: "))
            if position < 0 or position > 8:
                print("Position must be between 0 and 8!")
            elif board[position] in ['X', 'O']:
                print("Position already taken! Choose another.")
            else:
                board[position] = player
                break
        except ValueError:
            print("Invalid input! Enter a number 0-8.")

#Function to check if a player has won
def check_win(board, player):
    # Check all winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False



# Function to check if the board is full (tie)
def check_tie(board):
    for cell in board:
        if cell not in ['X', 'O']:
            return False
    return True
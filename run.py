
from random import randint

# SECRET_BOARD 

# GUESSES_LEFT = 10

TOTAL_SHIPS = 8

SHOWN_BOARD = [["W"] * 8 for x in range(8)]
SECRET_BOARD = [["W"] * 8 for x in range(8)]


def make_game_board(board):

    """
    function to create Game Board
    """
    print("   1   2   3   4   5   6   7   8")
    print("   -----------------------------")

    row_num = 1
    for row in board:
        print(f"{row_num}", " | ".join(row))
        row_num += 1
        # board[2][2] = "S"    
    

def create_ships(board):

    """
    function to create computer ships
    """
    for S in range(8):
        # ship_row, ship_col = randint(0, 7), randint(0,7)
        ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "S"
        

# create_ships(SHOWN_BOARD)       
# # create_ships(SECRET_BOARD)
# make_game_board(SHOWN_BOARD)


def user_guesses(board):

    """
    Input function for user to place guesses:
    """
    user_guess_row = int(input("Enter your row coordinate: "))
    user_guess_column = int(input("Enter your column coordinate: "))
    if board[user_guess_row][user_guess_column] == "W":
        board[user_guess_row][user_guess_column]= "M"
    elif board[user_guess_row][user_guess_column] == "S":
         board[user_guess_row][user_guess_column]= "H"

         
create_ships(SHOWN_BOARD) 
make_game_board(SHOWN_BOARD)
user_guesses(SHOWN_BOARD)
create_ships(SHOWN_BOARD)       
make_game_board(SHOWN_BOARD)



# # def new_game(board):
# #     make_game_board(board)
# #     create_ships(board)
# #     user_guesses(board)
    

# print("Welcome to Battleships\n\n")

# print("rules\n\n")

# name = input("What is your name Captain?\n\n")

# print("\n")

# print(f"Welcome {name} , we hope you will guide us well in this war!")

# go = input("Press S to start game   ")

# if go == "S":
    # create_ships(BOARD)
    # make_game_board(BOARD)
# else:
#     print("Damn Daniel, at it again with the white vans")


# new_game(board)


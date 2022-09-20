
from random import randint

# SECRET_BOARD 

# GUESSES_LEFT = 10

# TOTAL_SHIPS = 5

BOARD = [[" W "] * 8 for x in range(8)]  


def make_game_board(board):

    """
    function to create Game Board
    """

    print("   1   2   3   4   5   6   7   8")
    print("   -----------------------------")

    # for A in range(0, 7):
    #     board.append([" W "] * 8)
    #     print(board)    

    row_num = 1
    for row in board:
        print(f"{row_num}", "|".join(row))
        row_num += 1
    

make_game_board(BOARD)
    # for B in board:
    #     print("".join(B))
        
    
# def create_ships(board):

#     """
#     function to create computer ships
#     """
#     for ship in range(5):
#         ship_row, ship_col = randint(0, 7), randint(0,7)
#         board.append(ship,row, ship,col)
    

# def user_guesses(board):

#     """
#     Input function for user to place guesses:
#     """
#     user_guess_row = input("Enter your row coordinate: ")
#     user_guess_column = input("Enter your column coordinate: ")
#     if board [row] [column] == "W":
#         board [row] [columm] = "X"


# def new_game(board):
#     make_game_board(board)
#     create_ships(board)
#     user_guesses(board)
    

# print("Welcome to Battleships\n\n")

# print("rules\n\n")

# name = input("What would you like to be reffered to as for the purpose of this mission?\n\n")

# print("\n")

# print(f"Welcome {name} , we hope you will guide us well in this war!")


# new_game(board)


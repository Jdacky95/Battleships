
from random import randint

board = []

turns_left = 10

total_ships = 4


def make_game_board(board):

    """
    function to create Game Board
    """

    print(" 1  2  3  4  5  6  7  8")
    print("-----------------------")

    for A in range(0, 7):
        board.append([" W "] * 8)
    for B in board:
            print("".join(B))


def ships(board):

    """
    function to create computer ships
    """
    
    def ship_rand_row(board):
        return randint(0, len(board))

    def ship_rand_col(board):
        return randint(0, len(board[0]))

    
    # ship_row = ship_rand_row(board)
    # ship_col = ship_rand_col(board)

    

    # print(ship_row, ship_col)



def user_guesses(board):

    """
    Input function for user to place guesses:
    """
    user_guess_row = input("Enter your row coordinate: ")
    user_guess_column = input("Enter your column coordinate: ")

    

def game(board):
    make_game_board(board)
    ships(board)
    user_guesses(board)


print("Welcome to Battleships\n\n")

print("rules\n\n")

name = input("What would you like to be reffered to as for the purpose of this mission?\n\n")

print("\n")

print(f"Welcome {name} , we hope you will guide us well in this war!")


game(board)


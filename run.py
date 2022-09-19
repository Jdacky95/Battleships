# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

board = []

turns_left = 10




def make_game_board(board):

    """
    function to create Game Board
    """

    print(" 1  2  3  4  5  6  7  8")
    print("-----------------------")
    
    num = 1

    # for A in range(7):
    #     print(num + 1)

    for A in range(0, 7):
        board.append([" W "] * 8)
    for B in board:
            print("".join(B))
    
        

    # for B in board:
    #     print(" ".join_row())

make_game_board(board)

# class Board:

#     for x in range(8):
#         print(-)

#     def __init__(self, row, column):
#         self.row = row
#         self.column = column

    
# class Player:
#     def __init__(self, name, selection)

# print("Welcome to Battleships\n\n")

# print("rules\n\n")

# name = input("What would you like to be reffered to as for the purpose of this mission?\n\n")

# print("\n")

# print(f"Welcome {name} , we hope you will guide us well in this war!")
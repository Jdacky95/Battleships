"""
random function to produce random coordinates when generating ships
"""
from random import randint


# SHOWN_BOARD = [["_"] * 8 for x in range(8)]
# SECRET_BOARD = [["W"] * 8 for x in range(8)]


def make_game_board(board):

    """
    function to create Game Board's
    """
    print("\n\n    0   1   2   3   4   5   6   7")
    print("   -----------------------------")

    row_num = 0
    for row in board:
        print(f"{row_num} |", " | ".join(row))
        row_num += 1


def create_ships(board):

    """
    function to randomly create computer ships and assign to board
    """
    for S in range(5):

        ship_row, ship_col = randint(0, 7), randint(0, 7)
        if board[ship_row][ship_col] == "S":
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = "S"


def user_guesses():

    """
    Input function for user to place guesses:
    """
    user_guess_row = input("\n Enter your row coordinate: ")

    while user_guess_row not in "0,1,2,3,4,5,6,7":
        print("\n Your guess is outside of the board")
        print(" please choose a coordinate between 0 and 7")
        user_guess_row = input("\n Enter your row coordinate: ")

    if user_guess_row == "":
        print("\n You need to select a row Captain!")
        user_guess_row = input("\n Enter your row coordinate: ")

    user_guess_column = input("\n Enter your column coordinate: ")

    while user_guess_column not in "0,1,2,3,4,5,6,7":
        print("\n Your guess is outside of the board")
        print(" please choose a coordinate between 0 and 7")
        user_guess_column = input("\n Enter your column coordinate: ")

    if user_guess_column == "":
        print("\n You need to select a column Captain!")
        user_guess_column = input("\n Enter your row coordinate: ")

    return int(user_guess_row), int(user_guess_column)


def run_game():

    """
    Run game function that calls other in-game functions
    """

    TURNS_LEFT = 15
    SHIPS_LEFT = 5

    SHOWN_BOARD = [["_"] * 8 for x in range(8)]
    SECRET_BOARD = [["W"] * 8 for x in range(8)]

    create_ships(SECRET_BOARD)
    make_game_board(SHOWN_BOARD)

    for x in range(300):

        print(f"\n There are {SHIPS_LEFT} enemy ships remaining ")

        print(f"\n You have {TURNS_LEFT} shots left, make them count!")

        make_game_board(SHOWN_BOARD)
        user_guess_row, user_guess_column = user_guesses()

        if SHOWN_BOARD[user_guess_row][user_guess_column] == "M":
            print("\n Focus Captain, we've already fired there, try again! ")

        elif SHOWN_BOARD[user_guess_row][user_guess_column] == "H":
            print("\n Focus Captain, we've already fired there, try again! ")

        elif SECRET_BOARD[user_guess_row][user_guess_column] == "S":
            SHOWN_BOARD[user_guess_row][user_guess_column] = "H"
            print("\n You got one!!")
            TURNS_LEFT -= 1
            SHIPS_LEFT -= 1

        elif SECRET_BOARD[user_guess_row][user_guess_column] == "W":
            SHOWN_BOARD[user_guess_row][user_guess_column] = "M"
            print("\n That's a miss Captain, let's try again!")
            TURNS_LEFT -= 1

        if SHIPS_LEFT == 0:
            print("\n WE GOT THEM!")
            print("Those pesky Sea dwellers won't be")
            print("bothering us again any time soon!")

            play_again = input("\n If you'd like to play again Enter R,\
 if you want to exit Enter any other key:   \n ")

            if play_again == "R":

                print("\n" * 20)
                new_game()

            else:
                exit()

        if TURNS_LEFT == 0:

            print("\n Captain we've run out of Shells,")
            print(" The crew are leaving on the boats.")
            print("\n But you must go down with your ship!")

            play_again = input("\n If you'd like to play again Enter R,\
 if you want to exit Enter any other key:   \n").upper()

            if play_again == "R":

                print("\n" * 20)
                new_game()

            else:
                exit()


def new_game():

    """
    New game function is the first function called,
     it prints a welcome message,
     the rules and an option to start or exit the game.
     It is also recalled at the end of the game.
    """

    print(" BATTLESHIPS ")

    print("\n Welcome to Battleships")

    print("\n You will have 15 shots to sink the 5 enemy battleships.")
    print("\n Act quickly before they overrun you!")
    print("\n Enter a Row and Column coordinate")
    print(" between 0 and 7 to take your shot")
    print("\n Good Luck!")

    name = input("\n What is your name Captain?\n\n")

    print(f"\n Welcome Captain {name}, to the war room")
    print(" we hope you will guide us well in this battle!")

    start = input("\n Enter S to start\
 or any other key to exit the game:\n\n   ").upper()

    if start == "S":
        run_game()
    else:
        exit()


new_game()

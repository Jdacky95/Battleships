
from random import randint


SHOWN_BOARD = [["_"] * 8 for x in range(8)]
SECRET_BOARD = [["W"] * 8 for x in range(8)]


def make_game_board(board):

    """
    function to create Game Board
    """
    print("\n\n    0   1   2   3   4   5   6   7")
    print("   -----------------------------")

    row_num = 0
    for row in board:
        print(f"{row_num} |", " | ".join(row))
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


def user_guesses():

    """
    Input function for user to place guesses:
    """
    user_guess_row = input("\n Enter your row coordinate: ")

    while user_guess_row not in "01234567":
        print("\n Your guess is outside of the board, choose again")
        user_guess_row = input("\n Enter your row coordinate: ")

    if user_guess_row == "":
        print("\n You need to select a row Captain!")
        user_guess_row = input("\n Enter your row coordinate: ")
    
    
    user_guess_column = input("\n Enter your column coordinate: ")

    while user_guess_column not in "01234567":
        print("\n Your guess is outside of the board, choose again")
        user_guess_column = input("\n Enter your column coordinate: ")

    if user_guess_column == "":
        print("\n You need to select a column Captain!")
        user_guess_column = input("\n Enter your row coordinate: ")

    return int(user_guess_row), int(user_guess_column)

    # if board[user_guess_row][user_guess_column] == "W":
    #         board[user_guess_row][user_guess_column]= "M"

    # elif board[user_guess_row][user_guess_column] == "S":
    #      board[user_guess_row][user_guess_column]= "H"


    



    #     if board[user_guess_row][user_guess_column] == "W":
    #         board[user_guess_row][user_guess_column]= "M"

    # elif board[user_guess_row][user_guess_column] == "S":
    #      board[user_guess_row][user_guess_column]= "H"
         


# create_ships(SHOWN_BOARD) 
# make_game_board(SHOWN_BOARD)
# user_guesses(SHOWN_BOARD)
# # create_ships(SHOWN_BOARD)       
# make_game_board(SHOWN_BOARD)



def run_game():

    TURNS_LEFT = 10
    SHIPS_LEFT = 5

    create_ships(SECRET_BOARD)

    for x in range(5):

        print(f"\n There are {SHIPS_LEFT} enemy ships remaining ")

        print(f"\n You have {TURNS_LEFT} shots left, make them count!")

        
        make_game_board(SHOWN_BOARD)
        user_guess_row, user_guess_column = user_guesses()
        
        if SHOWN_BOARD[user_guess_row][user_guess_column] == "M" :
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
            print("\n WE GOT THEM! Those pesky Sea dwellers won't be bothering us again any time soon!")

            play_again = input("\n If you'd like to play again press R, if you want to exit press any other key:   \n ")

            if play_again == "R":
                
                print("\n" * 20)
                new_game()
            
            else:
                exit()

        if TURNS_LEFT == 0:

            print("\nCaptain we've run out of Shells, you must go down with the ship!")

            play_again = input("\n If you'd like to play again press R, if you want to exit press any other key:   \n").upper()

            if play_again == "R":
                
                print("\n" * 20)
                new_game()
            
            else:
                exit()


def new_game():

    

    print("\nWelcome to Battleships\n\n")

    print("rules\n\n")

    name = input("What is your name Captain?\n\n")

    print("\n")

    print(f"Welcome Captain {name}, to the war room, we hope you will guide us well in this battle!")

    start = input("\nPress S to start or any other key to exit the game:\n\n   ").upper()

    if start == "S":
        run_game()
    else:
        exit()

new_game()
# new_game(board)


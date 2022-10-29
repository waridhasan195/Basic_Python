
board = [".", ".", ".",
         ".", ".", ".",
         ".", ".", "."]

# If game still going
game_still_going = True

#who won? or Tie?
winner = None

#whos trun is it
current_player = "x"

# Display the game board to the screen
def display_board():
    print(board[0] + " | " + board[1]+ " | " + board[2])
    print(board[3] + " | " + board[4]+ " | " + board[5])
    print(board[6] + " | " + board[7]+ " | " + board[8])

# Play a game of tic tac toe
def play_game():
    #display initial Board
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:

        # Handle a turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()
    
    # Since the game is over, print the winner or tie
    if winner == "x" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Match Tie.")

# Handle a turn for an arbitrary player
def handle_turn(player):
    print(player + " 's Turn. . . ")
    possition = input("Choose a position from 1-9: ")

    vaild = False
    while not vaild:
        while possition not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            possition = input("Choose a position from 1-9: ")
        possition = int(possition)-1

        if board[possition] == '.':
            vaild = True
        else:
            print("You Can't go there, Go Again.")
    board[possition] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_for_tie()

def check_for_winner():
    global winner

    #Check for rows
    row_winner = check_rows()

    #check for columns
    columns_winner = check_columns()

    #check for diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #There was a win
        winner = row_winner
    elif columns_winner:
        #There was a win
        winner = columns_winner
    elif diagonal_winner:
        #There was a win
        winner = diagonal_winner
    else:
        return None



def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    #row_1 alltime flase when all valu is same only that time is turn true
    row_1 = board[0] == board[1] == board[2] != "."
    row_2 = board[3] == board[4] == board[5] != "."
    row_3 = board[6] == board[7] == board[8] != "."
    
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #Return The winner (x or o) who won?!
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None

def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "."
    column_2 = board[1] == board[4] == board[7] != "."
    column_3 = board[2] == board[5] == board[8] != "."
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    #Return The winner (x or o)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "."
    diagonal_2 = board[2] == board[4] == board[6] != "."
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    #Return The winner (x or o)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    else:
        return None

def check_for_tie():
    global game_still_going
    if '.' not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "x":
        current_player = "O"
    elif current_player == "O":
        current_player = "x"

    return


play_game()


#Board
#Display Board
#Play Game
#Handle Turn
#Check Win
    #Check RoW
    #Check RoW
    #Check Diagonal
#Check tie
#Flip Player



import numpy as np
import itertools

Board = list()
Move_1_indices = list()
Move_0_indices = list()
Row_lists = list()
Col_lists = list()


def show_board():    # Print or Show the board after each move played by either player A or B
    '''
    Draw the Tic Tac Toe game board
    '''
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print "|", Board[i][j], '\t',
        print "\n"


def show_move_index():      # Show the indices of 0 and 1 in Board
    '''
    Handle a player move from user input
    '''
    for r, element in list(enumerate(Board)):  # r stands for row
        for c, e in list(enumerate(element)):   # c stands for col
            if e != -999:   # Show r and c for 0 and 1 move
                if e == 1:
                    if tuple([r, c]) not in Move_1_indices:
                        Move_1_indices.append(tuple([r, c]))
                else:
                    if tuple([r, c]) not in Move_0_indices:
                        Move_0_indices.append(tuple([r, c]))

    print "In Board, Player A's moves at indices : ", Move_1_indices
    print "In Board, Player B's moves at indices : ", Move_0_indices


def CheckVictory(row, col):   # Declare the Victory of from Present board condition...
    '''
     Checking whether a game board has a winner
    '''

    # check if previous move caused a win on vertical line
    if Board[0][col] == Board[1][col] == Board[2][col]:
        return True

    # check if previous move caused a win on horizontal line
    if Board[row][0] == Board[row][1] == Board[row][2]:
        return True

    # check if previous move was on the main diagonal and caused a win
    if row == col and Board[0][0] == Board[1][1] == Board[2][2]:
        return True

    # check if previous move was on the secondary diagonal and caused a win
    if row + col == 2 and Board[0][2] == Board[1][1] == Board [2][0]:
        return True

    return False


def Create_borad():
    ''' A board of Tic - Tac - Toe consists of 3 rows and 3 columns. Every cell is initially filled by arbitrary
    value -999 '''
    for row in range(3):
        col_list = list()
        for col in range(3):
            col_list.append(-999)
        Board.append(col_list)
        del col_list
    print "Board is :"
    show_board()


def Any_further_move(row_col_pairs):
    if len(row_col_pairs) == 0:
        return False
    else:
        return True


def play_Tic_Tac_Toe():
    ''' Player A is Computer and Player B is User. Player A start the game using '1' and then Player B put '0' in
    sub-sequent blank spaces...'''
    # Create a list of (r,c) pair to define row and col pair...
    row_col_pairs = [[r, c] for r in range(3) for c in range(3)]
    print "Possible (r,c) positions to play move in Tic -Tac - Toe board:"
    print row_col_pairs

    futher_move = True
    while len(row_col_pairs) != 0:          # Continue unless all (r,c) moves are utilized by Players A and B .

            further_move = Any_further_move(row_col_pairs)
            if further_move:
                print "Player A move:"
                print "Computer Choose a index of (r,c) pair from list:", row_col_pairs
                move_A_index  = int(np.random.choice(len(row_col_pairs), 1, replace=False))
                print "Index", int(move_A_index), " in row_col_pairs."

                ''' Handle a player move from user input '''
                Board_row = row_col_pairs[move_A_index][0]
                Board_col = row_col_pairs[move_A_index][1]
                global Board
                play_A = 1
                Board[Board_row][Board_col] = play_A         # Play the move by Player A.
                del row_col_pairs[move_A_index]         # Remove the move for further movement...

                show_board()
                show_move_index()
                Status = CheckVictory(Board_row, Board_col)

                if Status:
                    print "Player A is Winner !!"
                    exit(0)
                else:
                    # For Draw, there is no element -999 in Board and CheckVictory() returns False
                    # Check Draw Situation
                    Check_draw = True
                    for row in range(3):
                        for col in range(3):
                            if Board[row][col] == -999:
                                Check_draw = False
                    if Check_draw:
                        print "Match is Draw !!!"

            else:
                return

            further_move = Any_further_move(row_col_pairs)
            if further_move:
                print "Player B move:"
                print "You Choose a index of (r,c) pair from list:", row_col_pairs
                move_B_index = int(input("Enter an index:"))
                print "index", move_B_index, " in row_col_pairs."

                ''' Handle a player move from user input '''
                Board_row = row_col_pairs[move_B_index][0]
                Board_col = row_col_pairs[move_B_index][1]
                global Board
                play_B = 0
                Board[Board_row][Board_col] = play_B         # Play the move by Player B.
                del row_col_pairs[move_B_index]         # Remove the move for further movement...
                show_board()
                show_move_index()

                Status = CheckVictory(Board_row, Board_col)
                if Status:
                    print "Player B is Winner !!"
                    exit(0)
                else:
                     # For Draw, there is no element -999 in Board and CheckVictory() returns False
                    # Check Draw Situation
                    Check_draw = True
                    for row in range(3):
                        for col in range(3):
                            if Board[row][col] == -999:
                                Check_draw = False
                    if Check_draw:
                        print "Match is Draw !!!"

            else:
                return

            print "\n"


# Main Namespace...
Create_borad()
play_Tic_Tac_Toe()
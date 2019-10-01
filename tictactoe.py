#TICTACTOE
#XAVIER ROSADO

#---------------------------VARIABLES--------------------------------
#if game is running
game_running = True

#winner/tie
winner = None 

#current turn
current_player = "X"

#Using a list that looks like a board; each coma assigns a position starting from zero
board =["_","_","_",
        "_","_","_",       
        "_","_","_"]

#--------------------------FUNCTIONS-----------------------------------
#displays board
def board_display():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])


#manages turns
def turn_play(player):
        print(player + "'s turn.")
        position = input("Choose a position to play! Use numbers from 1-9!:")
        #turn into int and substract one since list starts at position 0
        position = int(position) - 1

        #verifys if input is valid and if spot is open
        valid = False
        while not valid:
                while position not in ["1","2","3","4","5","6","7","8","9"]:
                        print("Choose a position from 1-9: ")
                    if board[position] == "_":
                            valid = True
                    else:
                            print("That spot is unavaiable. Try again!")

        board[position] = player




        board[position] = 'X'
        board_display()


def check_game_over():
        win_check()
        tie_check()

def win_check():
        global winner 

        row_winner = check_rows()
        column_winner = check_column()
        diagonal_winner = check_diagonals()

        if row_winner:
                winner = row_winner
        elif column_winner:
                winner = column_winner
        elif diagonal_winner:
                winner = diagonal_winner
        else:
                winner = None

def check_rows():
        global game_running
        #Checks if rows have the same Value
        row1 = board[0] == board[1] == board[2] != "_"
        row2 = board[3] == board[4] == board[5] != "_"
        row3 = board[6] == board[7] == board[8] != "_"

        if row1 or row2 or row3:
                game_running = False
        if row1:
                return board[0]
        elif row2:
                return board[3]
        elif row3:
                return board[6]
        else:
                return None

#DO THIS
def check_columns:

#DO THIS        
def check_diagonal:


#DO THIS
def tie_check():
        return

#DO THIS
def flip_player():
        return


#starts game
def play_game():
     board_display()
     while game_running:
             turn_play(current_player)
             check_game_over()
             flip_player()

     


play_game()

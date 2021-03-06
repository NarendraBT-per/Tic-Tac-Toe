# To Print Board
from IPython.display import clear_output
def board_layout(board):
    
    clear_output()
    
    print(' '+board[1]+f"|{board[2]}|"+board[3])
    print('--|-|--')
    print(' '+board[4]+f"|{board[5]}|"+board[6])
    print('--|-|--')
    print(' '+board[7]+f"|{board[8]}|"+board[9])

#To Check if space, at the specified position is available or not
def space_check(board, position):
    return ' ' == board[position]

#To place the marker at the specified position
def place_marker(board, position, marker):
    board[position] = marker

#To check if there is, specific marker, appearing in sequence
def win_check(board, marker):
    return board[1] == board[2] == board[3] == marker or \
           board[4] == board[5] == board[6] == marker or \
           board[7] == board[8] == board[9] == marker or \
           board[1] == board[4] == board[7] == marker or \
           board[2] == board[5] == board[8] == marker or \
           board[3] == board[6] == board[9] == marker or \
           board[1] == board[5] == board[9] == marker or \
           board[3] == board[5] == board[7] == marker

#To check whether board is full or not.
def board_check(board):
    return ' ' in board[1:]

#To obtain player's choice
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 select 'X' or 'O': ").upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# To decide which player plays first
import random
def first_player():
    a = random.randint(1,2)
    return a
    
# To request whether either of the player is willing play again
def replay():
    reply = ''
    
    while not (reply == 'Y' or reply == 'N'):
        reply = input("Do you wish play again?\n'y' or 'n': ").upper()
    
    if reply == 'Y':
        return True
    else:
        return False
    
# The game-play logic
while True:
    game_board = [' ']*10
    player_1, player_2 = player_input()
    turn = first_player()
    game_on = True
    
    while game_on:
        if turn == 1:
            board_layout(game_board)
            position = int(input("Player 1, enter a number: "))
            if space_check(game_board, position):
                place_marker(game_board, position, player_1)
                board_layout(game_board)
                if win_check(game_board, player_2):
                    board_layout(game_board)
                    print("Player 2 Won!!")
                    game_on = False
                elif not board_check(game_board):
                    print("It's a Tie!")
                    game_on = False
                else:
                    turn = 2
            else:
                position = int(input("Player 1, enter a different number: "))
                if space_check(game_board, position):
                    place_marker(game_board, position, player_1)
                    board_layout(game_board)
                    if win_check(game_board, player_2):
                        board_layout(game_board)
                        print("Player 2 Won!!")
                        game_on = False
                    elif not board_check(game_board):
                        print("It's a Tie!")
                        game_on = False
                    else:
                        turn = 2
        
        else:
            board_layout(game_board)
            position = int(input("Player 2, enter a number: "))
            if space_check(game_board, position):
                place_marker(game_board, position, player_2)
                board_layout(game_board)
                if win_check(game_board, player_2):
                    board_layout(game_board)
                    print("Player 2 Won!!")
                    game_on = False
                elif not board_check(game_board):
                    print("It's a Tie!")
                    game_on = False
                else:
                    turn = 1
            else:
                position = int(input("Player 2, enter a different number: "))
                if space_check(game_board, position):
                    place_marker(game_board, position, player_2)
                    board_layout(game_board)
                    if win_check(game_board, player_2):
                        board_layout(game_board)
                        print("Player 2 Won!!")
                        game_on = False
                    elif not board_check(game_board):
                        print("It's a Tie!")
                        game_on = False
                    else:
                        turn = 1
    
    if replay():
        game_on = True
    else:
        break
board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)


def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now will write the main function which has all the gameplay functionality.
def main():

    turn = 'X'
    count = 0


    while True:
        print_board(board)
        move = input(f"It's your turn {turn} enter any number from 1-9. ")       

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # I  will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ': # across the top
                print_board(board)
                print("Game Over.")                               
                break

            elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                print_board(board)
                print("Game Over.")                
                break

            elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
                print_board(board)
                print("Game Over")              
                break

            elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                print_board(board)
                print("Game Over.")                
                break

            elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                print_board(board)
                print("Game Over.")                
                break

            elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                print_board(board)
                print("Game Over.")                
                break 

            elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
                print_board(board)
                print("Game Over.")                
                break

            elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                print_board(board)
                print("Game Over.")                
                break 

        # If neither X nor O wins and the board is full, will declare the result as 'tie'.
        if count == 9:
            print("Game Over.")                
            print("It's a Tie!!")

        # I will have to change the player after every move.
        if turn =='X':
             turn = 'O'
        else:
            turn == 'X'

    # I will ask if player wants to play the game or not.
    continue_to_play = input("Do want to play Again?(y/n)")
    if continue_to_play == "y" or continue_to_play == "Y":  
        for key in board_keys:
            board[key] = " "

        main()

if __name__ == "__main__":
    main()
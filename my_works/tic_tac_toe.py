def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    def show_board(board):                                          # dash board function

        print("=================")
        print('||', board[1], '||', board[2], '||', board[3], '||')
        print('||', board[4], '||', board[5], '||', board[6], '||')
        print('||', board[7], '||', board[8], '||', board[9], '||')
        print("=================")
    show_board(board)

    first = input("DO YOU WANT TO BE A FIRST PLAYER TO START A GAME? Y/N \n --->")
    if first == "Y":
        print("GREAT, YOU ARE THE FIRST PLAYER IN THE GAME.\n")
    elif first.upper == "N":
        print("COMPUTER WILL START GAME AS FIRST PLAYER.\n")

    def choose_player(board):                                           # player entry function
        valid_move = False
        try:
            while not valid_move:
                select = int(input("CHOOSE YOUR NUMBER BETWEEN 1 - 9\n --->"))
                if select !=0:
                    if (board[select]) != "X" and board[select] != "O":
                        if first == "Y":
                            board[select] = "X"
                        else:
                            board[select] = "O"
                        valid_move = True
                    else:
                        print("SORRY, IT IS ALREADY OCCUPIED,PLEASE CHOOSE DIFFERENT NUMBER.")
        except:
            print("PLEASE ENTER A VALID NUMBER.")
            choose_player(board)

    import random

    def choose_computer(board):                                          # computer entry function
        valid_move = False
        while not valid_move:
            select = random.randint(1, 10)
            if board[select] != "X" and board[select] != "O":
                if first == "Y":
                    board[select] = "O"
                else:
                    board[select] = "X"
                valid_move = True
                print("COMPUTER MADE A MOVE AT", select, "POSITION")

    def win_conditions(board):
        winner = False
        if(board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]):
            winner = True
        if (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[3] == board[6] == board[9]):
            winner = True
        if (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]):
            winner = True
        return winner
    turn = 0
    won = False

    while not won and turn <= 9:
        if win_conditions(board) is True:
            won = True
        elif first == "Y":                                        # turn = 0,2,4,6,8
            if turn % 2 == 0:
                won = choose_player(board)
            else:                                               # turn = 1,3,5,7
                won = choose_computer(board)
        elif first == "N":
            if turn % 2 == 0:
                won = choose_computer(board)
            else:
                won = choose_player(board)
        turn = turn + 1
        show_board(board)
        win_conditions(board)
    if turn > 9:
        print("THIS IS A TIE MATCH")
    elif win_conditions(board) is True:                           # CHECKING WHO WON THIS GAME USER/COMPUTER
        if first == "Y":
            if (board[1] == board[2] == board[3] == "X") or (board[4] == board[5] == board[6] == "X") or (
                        board[7] == board[8] == board[9] == "X"):
                print("CONGRATULATION, YOU WON THIS GAME from horizontal line\n")
            elif (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (
                        board[3] == board[6] == board[9] == "X"):
                print("CONGRATULATION, YOU WON THIS GAME from vertical line\n")
            elif (board[1] == board[5] == board[9] == "X") or (board[3] == board[5] == board[7] == "X"):
                print("CONGRATULATION, YOU WON THIS GAME from diagonal line\n")
            else:
                print("WOW! COMPUTER IS SMARTER THAN YOU\n")
        elif first == "N":
            if (board[1] == board[2] == board[3] == "X") or (board[4] == board[5] == board[6] == "X") or (
                        board[7] == board[8] == board[9] == "X"):
                print("WOW! COMPUTER IS SMARTER THAN YOU, won from horizontal line\n")
            elif (board[1] == board[4] == board[7] == "X") or (board[2] == board[5] == board[8] == "X") or (
                        board[3] == board[6] == board[9] == "X"):
                print("WOW! COMPUTER IS SMARTER THAN YOU, won from vertical line\n")
            elif (board[1] == board[5] == board[9] == "X") or (board[3] == board[5] == board[7] == "X"):
                print("WOW! COMPUTER IS SMARTER THAN YOU, won from diagonal line\n")
            else:
                print("CONGRATULATION, YOU WON THIS GAME\n \n")

main()
ask_again = input("WANT TO RESTART THE GAME?Y/N \n --->")
if ask_again == "Y":
    main()
else:
    print("THANK YOU FOR PLAYING THIS GAME:")
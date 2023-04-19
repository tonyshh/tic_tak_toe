def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("___|___|___")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("___|___|___")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        move = input(f"{current_player}'s turn. Enter a position (1-9): ")

        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1

            if board[move] == " ":
                board[move] = current_player

                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

        # check for game over conditions
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] != " ":
                print_board(board)
                print(f"Game over. {board[i]} wins!")
                game_over = True
                break

        for i in range(3):
            if board[i] == board[i+3] == board[i+6] != " ":
                print_board(board)
                print(f"Game over. {board[i]} wins!")
                game_over = True
                break

        if board[0] == board[4] == board[8] != " ":
            print_board(board)
            print(f"Game over. {board[0]} wins!")
            game_over = True

        if board[2] == board[4] == board[6] != " ":
            print_board(board)
            print(f"Game over. {board[2]} wins!")
            game_over = True

        if " " not in board:
            print_board(board)
            print("Game over. It's a tie!")
            game_over = True

    play_again = input("Do you want to play again? (y/n): ")

    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing Tic-Tac-Toe!")

play_game()

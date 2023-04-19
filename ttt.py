from tkinter import *

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.game_over = False
        self.board = [" "]*9

        self.board_buttons = []
        for i in range(9):
            button = Button(master, text=" ", font=("Helvetica", 24), width=3, height=1, command=lambda i=i: self.update_board(i))
            button.grid(row=i//3, column=i%3)
            self.board_buttons.append(button)

        self.reset_button = Button(master, text="Reset", font=("Helvetica", 14), command=self.reset_board)
        self.reset_button.grid(row=3, column=1)

        self.status_label = Label(master, text="X's turn", font=("Helvetica", 14))
        self.status_label.grid(row=4, column=1)

    def update_board(self, index):
        if not self.game_over and self.board[index] == " ":
            self.board[index] = self.current_player
            self.board_buttons[index].config(text=self.current_player)

            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

            self.check_game_over()

            if not self.game_over:
                self.status_label.config(text=self.current_player+"'s turn")

    def check_game_over(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                self.game_over = True
                self.status_label.config(text=self.current_player+" wins!")
                self.highlight_winning_row([i, i+1, i+2])
                break

        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                self.game_over = True
                self.status_label.config(text=self.current_player+" wins!")
                self.highlight_winning_row([i, i+3, i+6])
                break

        if self.board[0] == self.board[4] == self.board[8] != " ":
            self.game_over = True
            self.status_label.config(text=self.current_player+" wins!")
            self.highlight_winning_row([0, 4, 8])

        if self.board[2] == self.board[4] == self.board[6] != " ":
            self.game_over = True
            self.status_label.config(text=self.current_player+" wins!")
            self.highlight_winning_row([2, 4, 6])

        if " " not in self.board and not self.game_over:
            self.game_over = True
            self.status_label.config(text="It's a tie!")

    def highlight_winning_row(self, row):
        for i in row:
            self.board_buttons[i].config(bg="yellow")

    def reset_board(self):
        self.current_player = "X"
        self.game_over = False
        self.board = [" "]*9
        for button in self.board_buttons:
            button.config(text=" ", bg="white")
        self.status_label.config(text="X's turn")

root = Tk()
game = TicTacToe(root)
root.mainloop()

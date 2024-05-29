'''
Author: Karina Santos Felippe
Version: 1.0
About:
    The game is played on a grid of button cells, where each cell can either be empty or contain a hidden mine.
    The player's objective is to uncover all the empty cells on the grid without detonating any mines.
    The player selects a cell to reveal its content. If the revealed cell contains a mine, the game ends immediately, and the player loses.
    However, if the revealed cell is empty, it will display a number indicating the number of mines in adjacent cells. Using this information, the player must strategically reveal cells to deduce the locations of the mines.
    The game is won when all non-mine cells are revealed.
'''
import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, root, rows, columns, num_mines):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines
        self.not_openned_squares = rows * columns

        self.board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.create_board()
        self.plant_mines()
        self.create_squares()

    # Create the gameboard as a grid of tkinter StringVar
    # with the number of rows and columns as determined 
    # in the game construction
    def create_board(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.board[i][j] = tk.StringVar()

    # Determines the position of each mine on the grid of
    # the gameboard using a random index for row and 
    # column. The number of mines planted is determined
    # in the game construction
    def plant_mines(self):
        mines_planted = 0
        while mines_planted < self.num_mines:
            row = random.randint(0, self.rows - 1)
            column = random.randint(0, self.columns - 1)
            if self.board[row][column].get() != ' ':
                self.board[row][column].set(' ')
                mines_planted += 1

    # Create each square in the user interface as a button
    # with the text variable settle on the grid (empty or mine)
    def create_squares(self):
        for i in range(self.rows):
            for j in range(self.columns):
                button = tk.Button(self.root, textvariable=self.board[i][j], width=4, height=2,
                                command=lambda row=i, column=j: self.click_button(row, column))
                button.grid(row=i, column=j)

    # Each click will check whether if the user won or lost, if
    # non of those checks are true, then it will show the number
    # of mines around this clicked square button
    def click_button(self, row, column):
        if self.board[row][column].get() == ' ':
            self.board[row][column].set('X')
            self.open_all_squares()
            tk.messagebox.showerror(title="End game", message="You loose!")
            self.root.quit()
        elif not self.board[row][column].get().isdigit():
            adjacent_mines = self.count_adjacent_mines(row, column)
            self.board[row][column].set(str(adjacent_mines))
            self.not_openned_squares -= 1

        if self.not_openned_squares == self.num_mines:
            self.open_all_squares()
            tk.messagebox.showinfo(title="Well done!", message="You win!")
            self.root.quit()

    # Count the number of mines that are around this square on
    # the grid and returns this count.
    def count_adjacent_mines(self, row, column):
        count = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, column - 1), min(self.columns, column + 2)):
                if self.board[i][j].get() == ' ' or  self.board[i][j].get() == 'X':
                    count += 1
        return count

    # If the user won or lost, the mines will be revealed on the
    # gameboard and all adjacents counts will be shown.
    def open_all_squares(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j].get() == ' ':
                    self.board[i][j].set("X")
                    continue
                elif self.board[i][j].get() == 'X':
                    continue
                elif self.board[i][j].get() is '':
                    adjacent_mines = self.count_adjacent_mines(i, j)
                    self.board[i][j].set(str(adjacent_mines))

def main():
    # For this first version, the gameboard is an unique and
    # easy 5x5 grid with 5 mines planted
    rows = 5
    columns = 5
    num_mines = 5

    root = tk.Tk()
    root.title("Minesweeper")
    _ = Minesweeper(root, rows, columns, num_mines)
    root.mainloop()

if __name__ == "__main__":
    main()
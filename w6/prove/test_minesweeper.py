'''
Author: Karina Santos Felippe
'''
import pytest
import tkinter as tk
from minesweeper import Minesweeper
NUM_MINES_PLANTED = 5
NUM_GRID_ROWS = 5
NUM_GRID_COLUMNS = 5
# Fixtures - Pytest Docs:
#   When pytest goes to run a test, it looks at the parameters
#   in that test function’s signature, and then searches for fixtures
#   that have the same names as those parameters. Once pytest finds 
#   them, it runs those fixtures, captures what they returned (if
#   anything), and passes those objects into the test function as arguments.
# Source: https://docs.pytest.org/en/8.2.x/how-to/fixtures.html
@pytest.fixture
def game():
    root = tk.Tk()
    game = Minesweeper(root, NUM_GRID_ROWS, NUM_GRID_COLUMNS, NUM_MINES_PLANTED)
    yield game
    root.destroy()

# Count the number of mines planted on the board
# and compare with the number of mines settled in
# the constructor
def test_plant_mines(game):
    mines = 0
    for i in range(game.rows):
        for j in range(game.columns):
            if game.board[i][j].get() == ' ':
                mines += 1
    assert mines == game.num_mines
    assert mines == NUM_MINES_PLANTED

# Plant a mine in the first grid position and
# verify if the count of adjcent mines for the
# second grid position is greater than 1 (the
# one mine planted)
# Also, verify if the count is less then the
# number of mines planted in the construction
def test_count_adjacent_mines(game):
    game.board[0][0].set(' ')
    adjacent_mines = game.count_adjacent_mines(0, 1)
    assert adjacent_mines > 1
    assert adjacent_mines < NUM_MINES_PLANTED

# Verify the number of rows and columns of the
# grid is the same passed through the constructor
def test_create_board(game):
    assert len(game.board) == game.rows
    assert len(game.board) == NUM_GRID_ROWS
    assert len(game.board[0]) == game.columns
    assert len(game.board[0]) == NUM_GRID_COLUMNS

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
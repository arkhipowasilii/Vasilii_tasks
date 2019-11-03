from sudoku import append, get_dependent_indexes, main
from cell import Cell
from random import choice


def test_get_dependent_indexes():
    sudoku = [[0, 0, 0, 0, 6, 0, 7, 0, 0],
              [0, 5, 9, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [6, 0, 0, 5, 0, 0, 0, 0, 0],
              [3, 0, 0, 0, 0, 0, 4, 6, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 1],
              [8, 0, 0, 7, 4, 0, 0, 0, 0]]

    sudoku_cells = main(sudoku)
    for row in sudoku:
        for cell in row:
            candidat = choice(cell.ge)

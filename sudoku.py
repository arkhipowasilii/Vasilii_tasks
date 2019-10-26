from sudoku_helper import get_box_map, get_box_indexes, get_column_indexes, get_row_indexes
from typing import Dict, List, Tuple, Set
from random import choice
from cell import Cell, State


num_box = get_box_map()
box_indexes = get_box_indexes(num_box)
column_indexes = get_column_indexes()
row_indexes = get_row_indexes()


def exclude(sudoku, row_indexes, column_indexes, box_indexes, cell, candida):
    pass


def get_all_indexes(row_index: int, column_index: int) -> Set[Set[int, int]]:
    result = (row_indexes[row_index] + column_indexes[column_index]
              + box_indexes[num_box[(row_index, column_index)]])
    return result


def main(sudoku: List[List[int]]):
    sudoku_cells = [[Cell() for i in range(0, 9)] for j in range(0, 9)]

    num_box = get_box_map()

    box_nums = {i: [] for i in range(9)}
    column_nums = {i: [] for i in range(9)}
    row_nums = {i: [] for i in range(9)}

    for row_index in range(9):
        for column_index, element in enumerate(sudoku[row_index]):
            if element != 0:
                row_nums[row_index].append(element)
                column_nums[column_index].append(element)
                box_nums[num_box[(row_index, column_index)]].append(element)

                sudoku_cells[row_index][column_index].candidates = [element]

    for row_index in range(9):
        for column_index, cell in enumerate(sudoku_cells[row_index]):
            if len(cell.candidates) > 1:
                cell.delete_list(set(box_nums[num_box[(row_index, column_index)]] + row_nums[row_index]
                                     + column_nums[column_index]))

    is_correct = False
    row_index = 0
    column_index = 0
    direction_forward = True

    while not is_correct:
        cell = sudoku_cells[row_index][column_index]
        if direction_forward:
            if len(cell.candidates) > 1:
                candidat = choice(cell.candidates.keys())
                cell.candidates[candidat] = State.Used
            elif len(cell.candidates) == 0:
                pass
        else:
            pass


if __name__ == '__main__':
    sudoku = [[0, 0, 0, 6, 0, 9, 0, 0, 0],
              [5, 0, 0, 0, 7, 0, 0, 0, 3],
              [0, 0, 0, 3, 0, 0, 2, 8, 9],
              [0, 9, 5, 0, 4, 0, 0, 3, 0],
              [3, 0, 7, 0, 2, 0, 0, 0, 0],
              [2, 0, 1, 0, 0, 0, 7, 0, 0],
              [0, 0, 6, 4, 0, 0, 0, 0, 0],
              [9, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 5, 0, 0, 8]]
    print(get_all_indexes(0, 0))

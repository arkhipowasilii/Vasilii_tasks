from sudoku_helper import get_box_map, get_box_indexes, get_column_indexes, get_row_indexes
from typing import Dict, List, Tuple, Set
from random import choice
from cell import Cell, State

import logging


num_box = get_box_map()
box_indexes = get_box_indexes(num_box)
column_indexes = get_column_indexes()
row_indexes = get_row_indexes()

box_nums = {i: [] for i in range(9)}
column_nums = {i: [] for i in range(9)}
row_nums = {i: [] for i in range(9)}


def exclude(sudoku, candidate: int, row_index: int, column_index: int):
    for i_index, j_index in get_all_related_indexes(row_index, column_index):
        sudoku[i_index][j_index].exclude(candidate)

def append(sudoku, candidate: int, row_index: int, column_index: int):
    dependent_indexes = get_dependent_indexes(sudoku, candidate, row_index, column_index)
    logging.debug(f"{candidate} -> ({row_index}, {column_index}) : {dependent_indexes}")
    for i_index, j_index in dependent_indexes:
        sudoku[i_index][j_index].refresh_one(candidate)

def get_dependent_indexes(sudoku, candidate: int, old_row_index, old_column_index) -> Set[Tuple[int, int]]:
    result = set()
    old_indexes = (old_row_index, old_column_index)
    all_related_indexes = get_all_related_indexes(old_row_index, old_column_index)

    for row_index, column_index in all_related_indexes:
        if candidate in sudoku[row_index][column_index].candidates:
            current_indexes = get_all_related_indexes(row_index, column_index)

            if old_indexes in all_related_indexes:
                all_related_indexes.remove(old_indexes)
            for i, j in current_indexes:
                cell = sudoku[i][j]
                if cell.current() == candidate:
                    break
            else:
                result.add((row_index, column_index))

    return result


def get_all_related_indexes(row_index: int, column_index: int) -> Set[Tuple[int, int]]:
    result = set()
    all_indexes = set(row_indexes[row_index] + column_indexes[column_index]
              + box_indexes[num_box[(row_index, column_index)]])
    for element in all_indexes:
        result.add(element)
    result.remove((row_index, column_index))

    return result


def get_prev_indexes(row_index: int, column_index: int):
    if column_index > 0:
        return row_index, column_index - 1
    else:
        return row_index - 1, 8


def get_next_indexes(row_index: int, column_index: int):
    if column_index < 8:
        return row_index, column_index + 1
    else:
        return row_index + 1, 0


def main(sudoku: List[List[int]]):
    sudoku_cells = [[Cell() for i in range(0, 9)] for j in range(0, 9)]

    num_box = get_box_map()

    # 0(9*9) Сложность
    for row_index in range(9):
        for column_index, num in enumerate(sudoku[row_index]):
            if num != 0:
                row_nums[row_index].append(num)
                column_nums[column_index].append(num)
                box_nums[num_box[(row_index, column_index)]].append(sudoku_cells, old_candidate, row_index, column_index)
                exclude(sudoku_cells, candidate, row_index, column_index)

                direction_forward = True
                row_index, column_index = get_next_indexes(row_index, column_index)
            else:
                candidate = cell.current()
                append(sudoku_cells, candidate, row_index, column_index)

                cell.refresh_all([State.Expire, State.Used])

                row_index, column_index = get_prev_indexes(row_index, column_index)


if __name__ == '__main__':
    logging.setLevel(logging.DEBUG)
    sudoku = [[0, 0, 0, 0, 6, 0, 7, 0, 0],
              [0, 5, 9, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [6, 0, 0, 5, 0, 0, 0, 0, 0],
              [3, 0, 0, 0, 0, 0, 4, 6, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 1],
              [8, 0, 0, 7, 4, 0, 0, 0, 0]]

    solved_sudoku = main(sudoku)
    n = 0
    for row in solved_sudoku:
        for num in row:
            print(num.candidates)

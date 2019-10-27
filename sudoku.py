from sudoku_helper import get_box_map, get_box_indexes, get_column_indexes, get_row_indexes
from typing import Dict, List, Tuple, Set
from random import choice
from cell import Cell, State


num_box = get_box_map()
box_indexes = get_box_indexes(num_box)
column_indexes = get_column_indexes()
row_indexes = get_row_indexes()


def exclude(sudoku, candidate: int, row_index: int, column_index: int):
    for i_index, j_index in get_all_indexes(row_index, column_index):
        sudoku[i_index][j_index].exclude(candidate)


def append(sudoku, candidate: int, row_index: int, column_index: int):
    for i_index, j_index in get_all_indexes(row_index, column_index):
        sudoku[i_index][j_index].refresh_one(candidate)


def get_all_indexes(row_index: int, column_index: int) -> Set[Tuple[int, int]]:
    result = set()
    all_indexes = (row_indexes[row_index] + column_indexes[column_index]
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

    box_nums = {i: [] for i in range(9)}
    column_nums = {i: [] for i in range(9)}
    row_nums = {i: [] for i in range(9)}

    for row_index in range(9):
        for column_index, num in enumerate(sudoku[row_index]):
            if num != 0:
                row_nums[row_index].append(num)
                column_nums[column_index].append(num)
                box_nums[num_box[(row_index, column_index)]].append(num)

                cell = sudoku_cells[row_index][column_index]
                cell.use(num)

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
        unused_candidates = cell.get_unused()

        if column_index > 8 or row_index > 8:
            return sudoku_cells

        if direction_forward:
            if len(unused_candidates) >= 1:

                candidate = choice(unused_candidates)
                cell.use(candidate)
                exclude(sudoku_cells, candidate, row_index, column_index)
                row_index, column_index = get_next_indexes(row_index, column_index)

            else:

                row_index, column_index = get_prev_indexes(row_index, column_index)
                direction_forward = False
        else:
            if len(unused_candidates) >= 1:
                candidate = choice(unused_candidates)
                old_candidate = cell.change_used(candidate)

                append(sudoku_cells, old_candidate, row_index, column_index)
                exclude(sudoku_cells, candidate, row_index, column_index)

                direction_forward = True
                row_index, column_index = get_next_indexes(row_index, column_index)
            else:
                candidate = cell.current()
                if isinstance(candidate, int):
                    append(sudoku_cells, candidate, row_index, column_index)

                cell.refresh_all([State.Expire, State.Used])

                row_index, column_index = get_prev_indexes(row_index, column_index)


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
    solved_sudoku = main(sudoku)
    for row in solved_sudoku:
        for num in row:
            print(num)

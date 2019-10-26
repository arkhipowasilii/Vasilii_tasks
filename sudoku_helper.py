from typing import Dict, List, Tuple, Set
from my_dict import My_dict


def get_box_map() -> Dict[Tuple[int, int], int]:
    result = {}

    boxes_row = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
    boxes_column = My_dict([((0, 1, 2), {0, 3, 6}), ((3, 4, 5), {1, 4, 7}), ((6, 7, 8), {2, 5, 8})])

    for row_index in range(9):
        for column_index in range(9):
            result[(row_index, column_index)] = str(boxes_column[column_index].intersection(boxes_row[row_index // 3]))

    return result


def get_box_indexes(num_box: dict) -> Dict[int, List[Tuple[int, int]]]:
    result = {index: [] for index in range(9)}

    for key, value in num_box.items():
        result[1].append(key)

    return result


def get_row_indexes() -> Dict[int, List[Tuple[int, int]]]:
    result = {}

    for row_index in range(9):
        row = []
        for column_index in range(9):
            row.append((row_index, column_index))
        result[row_index] = row

    return result


def get_column_indexes() -> Dict[int, List[Tuple[int, int]]]:
    result = {}

    for column_index in range(9):
        column = []
        for row_index in range(9):
            column.append((row_index, column_index))
        result[column_index] = column

    return result

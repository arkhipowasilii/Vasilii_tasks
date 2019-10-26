from enum import Enum


class Cell:
    def __init__(self, candidates: list = None, up=None, right=None, down=None, left=None):
        self.candidates: list = candidates
        self.unused_candidates: list = []
        self.excluded_cadidates: list = []

        self.prev = prev

    def delete_candidate(self, candidate: int):
        if candidate in self.candidates:
            self.candidates.remove(candidate)

    def next(self):
        next_cell = self.neighbours[Direction.Right]
        pass  # ToDo

    def _exclude_candidates(self, direction: Direction, candidate: int):
        next_cell = self.neighbours[direction]
        if next_cell is not None:
            next_cell.delete_candidate(candidate)
            next_cell._exclude_candidates(direction, candidate)

    def exclude_row_column_candidates(self, candidate: Direction):
        for direction in Direction:
            self._exclude_candidates(direction, candidate)


def get_box_indexes() -> Dict[Tuple[int, int], int]:
    result = {}

    boxes_row = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
    boxes_column = {(0, 1, 2): {0, 3, 6}, (3, 4, 5): {1, 4, 7}, (6, 7, 8): {2, 5, 8})

    for row_index in range(9):
        for column_index in range(9):
            result[(row_index, column_index)] = boxes_column[column_index]).intersect(boxes_row[row_index // 3])

    return result


def exclude_all_candidates(candidate: int, sudoku_cells: list, i_index: int, j_index: int, current_cell: Cell):
    sudoku_cells[i_index][j_index].exclude_row_column_candidates(candidate)
    exclude_box_candidates(i_index, j_index, sudoku_cells, candidate, current_cell)


def solve_sudoku(sudoku: list) -> list:
    sudoku_cells = []

    for i in range(9):
        sudoku_cells.append([])

        for j in range(9):
            current_cell = Cell(candidates=list(range(1, 10)))

            if j > 0:
                current_cell.left = sudoku_cells[i][j - 1]
                sudoku_cells[i][j - 1].right = current_cell

            if i > 0:
                current_cell.up = sudoku_cells[i - 1][j]
                sudoku_cells[i - 1][j].down = current_cell

            sudoku_cells[i].append(current_cell)

    for row_cells in sudoku_cells:
        for cell in row_cells:
            cell.update_list_neighbours()

    for i in range(9):
        for j, element in enumerate(sudoku[i]):
            if element != 0:
                current_cell = sudoku_cells[i][j]
                current_cell.candidates = [element]
                exclude_all_candidates(element, sudoku_cells, i, j, current_cell)

    corect_sudoku = False
    current_cell = sudoku_cells[0][0]
    while not corect_sudoku:
        #    if len(current_candidates) > 1:
        #        candidate = current_candidates[0]
        #        cell.unused_candidates = current_candidates
        #        cell.unused_candidates.remove(candidate)
        #    elif len(current_candidates) == 0:
        pass
    current_cell = current_cell.next

    return sudoku_cells


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

    solved_sudoku = solve_sudoku(sudoku)
    for i in range(9):
        for j in range(9):
            print(solved_sudoku[i][j].candidates)
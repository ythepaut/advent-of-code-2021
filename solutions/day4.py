"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> tuple[np.array, np.array, np.array]:
    """Transforms each input to its integer value"""

    drawn_numbers = np.array(list(map(lambda n: int(n), inputs[0][:-1].split(","))))

    grids = []  # List of the grids containing the numbers : grids[i][j][k] = number in the i-th grid, line j, column k.
    mark_grids = []  # List of the grids with "marks", grids[i][j][k] == True <=> number in grids[i][j][k] is drawn.

    current_grid = []
    current_mark_grid = []
    for i in range(2, len(inputs)):
        line = inputs[i]
        if line == "\n":
            grids.append(current_grid)
            current_grid = []
            mark_grids.append(current_mark_grid)
            current_mark_grid = []
        else:
            current_grid.append(list(map(lambda n: int(n), line[:-1].split())))
            current_mark_grid.append([False for _ in range(len(current_grid[-1]))])

    if len(current_grid) > 0:
        grids.append(current_grid)
    if len(current_mark_grid) > 0:
        mark_grids.append(current_mark_grid)

    return drawn_numbers, np.array(grids), np.array(mark_grids)


def mark_drawn_number(drawn_number: int, grids: np.array, mark_grids: np.array) -> None:
    """Updates the mark grid for each grid given the drawn number"""
    for i in range(grids.shape[0]):
        for j in range(grids.shape[1]):
            for k in range(grids.shape[2]):
                if drawn_number == grids[i, j, k]:
                    mark_grids[i, j, k] = True


def find_winning_grids(mark_grids: np.array) -> np.array:
    """Returns the list of indexes where grids are completed"""
    winning_grids = []
    for i in range(len(mark_grids)):
        for j in range(mark_grids[i].shape[0]):  # line check
            if np.all(mark_grids[i, j, :]):
                winning_grids.append(i)
        for k in range(mark_grids[i].shape[1]):  # line check
            if np.all(mark_grids[i, :, k]):
                winning_grids.append(i)
    return np.unique(np.array(winning_grids))


def sum_unmarked_numbers(grid: np.array, mark_grid: np.array) -> int:
    """Returns the sum of all unmarked numbers in the grid"""
    result = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if not mark_grid[i, j]:
                result += grid[i, j]
    return result


def part1(drawn_numbers: np.array, grids: np.array, mark_grids: np.array) -> int:
    for number in drawn_numbers:
        mark_drawn_number(number, grids, mark_grids)
        winning_grids = find_winning_grids(mark_grids)
        if len(winning_grids) > 0:
            return sum_unmarked_numbers(grids[winning_grids[0]], mark_grids[winning_grids[0]]) * number
    return -1


def part2(drawn_numbers: np.array, grids: np.array, mark_grids: np.array) -> int:
    for number in drawn_numbers:
        mark_drawn_number(number, grids, mark_grids)
        winning_grids = find_winning_grids(mark_grids)
        if len(winning_grids) > 0:
            for winning_grid in winning_grids:
                if len(grids) == 1:
                    return sum_unmarked_numbers(grids[winning_grid], mark_grids[winning_grid]) * number
                else:
                    grids = np.array([grids[i] for i in range(len(grids)) if i != winning_grid])
                    mark_grids = np.array([mark_grids[i] for i in range(len(mark_grids)) if i != winning_grid])
    return -1


def solve(inputs: list) -> tuple[int, int]:
    drawn_numbers, grids, mark_grids = preprocess_inputs(inputs)
    return part1(drawn_numbers.copy(), grids.copy(), mark_grids.copy()), \
        part2(drawn_numbers.copy(), grids.copy(), mark_grids.copy())

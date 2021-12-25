"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> tuple[np.ndarray, list[tuple[str, int]]]:
    """
    Returns the grid of points and the instruction list such that instructions
    "fold along y=7 and fold along x=5  =>  [("y", 7), ("x", 5)]"
    """
    # Find grid size
    width = 0
    height = 0
    index = 0
    while len(inputs[index][:-1]) > 0:
        x, y = inputs[index][:-1].split(",")
        if int(x) > width:
            width = int(x)
        if int(y) > height:
            height = int(y)
        index += 1

    # Process coordinates and build grid
    grid = np.array([[" " for _ in range(width + 1)] for _ in range(height + 1)])
    index = 0
    while len(inputs[index][:-1]) > 0:
        x, y = inputs[index][:-1].split(",")
        grid[int(y), int(x)] = "#"
        index += 1

    # Process fold instructions
    instructions = []
    for i in range(index + 1, len(inputs)):
        instructions.append((inputs[i][11], int(inputs[i][13:-1])))
    return grid, instructions


def fold(grid: np.ndarray, instruction: tuple[str, int]) -> np.ndarray:
    offset_x = 0 if instruction[0] == "y" else instruction[1] + 1
    offset_y = 0 if instruction[0] == "x" else instruction[1] + 1
    for i in range(offset_x, grid.shape[1]):
        for j in range(offset_y, grid.shape[0]):
            if grid[j, i] == "#":
                new_x = i if instruction[0] == "y" else instruction[1] - (i - instruction[1])
                new_y = j if instruction[0] == "x" else instruction[1] - (j - instruction[1])
                grid[new_y, new_x] = "#"
    new_shape = (grid.shape[1], instruction[1]) if instruction[0] == "y" else (instruction[1], grid.shape[0])
    return grid[:new_shape[1], :new_shape[0]]


def part1(grid: np.ndarray, instructions: list[tuple[str, int]]) -> int:
    grid = fold(grid, instructions[0])
    return np.count_nonzero(grid == "#")


def part2(grid: np.ndarray, instructions: list[tuple[str, int]]) -> str:
    for i in range(len(instructions)):
        grid = fold(grid, instructions[i])
    return "\n" + np.array2string(grid, max_line_width=200)


def solve(inputs: list) -> tuple[int, str]:
    grid, instructions = preprocess_inputs(inputs)
    return part1(grid, instructions), part2(grid, instructions)

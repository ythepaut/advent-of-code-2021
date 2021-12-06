"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np

GRID_SIZE = 1000


def preprocess_inputs(inputs: list) -> None:
    """Transforms each input to its integer value"""
    for i in range(len(inputs)):
        points = inputs[i][:-1].split(" -> ")
        x1, y1, x2, y2 = int(points[0].split(",")[0]), \
                         int(points[0].split(",")[1]), \
                         int(points[1].split(",")[0]), \
                         int(points[1].split(",")[1])
        inputs[i] = ((x1, y1), (x2, y2))


def build_grid(segments: list[tuple[tuple[int]]], diagonal=False) -> np.ndarray:
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for segment in segments:
        x1, y1, x2, y2 = segment[0][0], segment[0][1], segment[1][0], segment[1][1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x, y1] += 1
        elif diagonal:
            stepX = 1 if x2 > x1 else -1
            stepY = 1 if y2 > y1 else -1
            x, y = x1, y1
            while x != x2 and y != y2:
                grid[x, y] += 1
                x += stepX
                y += stepY
            grid[x2, y2] += 1
    return grid


def part1(inputs: list[tuple[tuple[int]]]) -> int:
    grid = build_grid(inputs)
    return (grid >= 2).sum()


def part2(inputs: list[tuple[tuple[int]]]) -> int:
    grid = build_grid(inputs, diagonal=True)
    return (grid >= 2).sum()


def solve(inputs: list) -> tuple[int, int]:
    preprocess_inputs(inputs)
    return part1(inputs), part2(inputs)

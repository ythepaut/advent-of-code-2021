"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import math
import numpy as np


def preprocess_inputs(inputs: list) -> np.ndarray:
    """Transforms each input to its integer value"""
    for i in range(len(inputs)):
        inputs[i] = [int(d) for d in inputs[i][:-1]]
    return np.array(inputs)


def neighbours(matrix: np.ndarray, i: int, j: int) -> tuple[int, int, int, int]:
    """Returns the neighbours of (i, j) as (top, right, bottom, left)"""
    top = matrix[i - 1, j] if i - 1 >= 0 else math.inf
    right = matrix[i, j + 1] if j + 1 < matrix.shape[1] else math.inf
    bottom = matrix[i + 1, j] if i + 1 < matrix.shape[0] else math.inf
    left = matrix[i, j - 1] if j - 1 >= 0 else math.inf
    return top, right, bottom, left


def find_basin(heightmap: np.ndarray, i: int, j: int, explored: list) -> list:
    if i < 0 or i >= heightmap.shape[0] or j < 0 or j >= heightmap.shape[1]:
        return []
    if heightmap[i, j] >= 9:
        return []
    if (i, j) in explored:
        return []

    coordinates = [(i, j)]
    explored.append((i, j))
    sides = find_basin(heightmap, i - 1, j, explored), \
            find_basin(heightmap, i, j + 1, explored), \
            find_basin(heightmap, i + 1, j, explored), \
            find_basin(heightmap, i, j - 1, explored)

    for side in sides:
        if len(side) > 0:
            coordinates += side
    return coordinates


def coordinate_in_basins(basins: list, i: int, j: int) -> bool:
    """Returns True if a coordinate is found inside the list of basins"""
    for basin in basins:
        for coordinate in basin:
            if coordinate == (i, j):
                return True
    return False


def largest_bassin(bassins: list) -> list:
    """Returns the largest bassin in the bassins"""
    result = None
    for bassin in bassins:
        if result is None or len(result) < len(bassin):
            result = bassin
    return result


def part1(heightmap: np.ndarray) -> int:
    risk_level = 0
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if min(neighbours(heightmap, i, j)) > heightmap[i, j]:
                risk_level += heightmap[i, j] + 1
    return risk_level


def part2(heightmap: np.ndarray) -> int:
    # Get all basins
    basins = []
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            print(f"Finding bassins {round(((i * heightmap.shape[0] + j) / (heightmap.shape[0] * heightmap.shape[1])) * 100)}%", end="\r")
            if not coordinate_in_basins(basins, i, j):
                basin = find_basin(heightmap, i, j, [])
                if len(basin) > 0:
                    basins += [basin]

    # Multiplying the length of the 3 largest basins
    result = 1
    for _ in range(3):
        bassin = largest_bassin(basins)
        result *= len(bassin)
        basins.remove(bassin)
    return result


def solve(inputs: list) -> tuple[int, int]:
    heightmap = preprocess_inputs(inputs)
    return part1(heightmap), part2(heightmap)

"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import math
from typing import Callable
import numpy as np


Node = tuple[int, int]


def preprocess_inputs(inputs: list) -> np.ndarray:
    for i in range(len(inputs)):
        inputs[i] = [int(d) for d in inputs[i][:-1]]
    return np.array(inputs)


def get_neighbours(position: Node, shape: tuple[int, int]) -> list[Node]:
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:  # not self
                continue
            if not 0 <= position[0] + i < shape[0] or not 0 <= position[1] + j < shape[1]:  # out of bound
                continue
            if i != 0 and j != 0:  # no diagonal
                continue
            neighbours.append((position[0] + i, position[1] + j))
    return neighbours


def reconstruct_path(predecessors: dict[Node, Node], current: Node) -> list[Node]:
    path = [current]
    while current in predecessors.keys():
        current = predecessors[current]
        path.insert(0, current)
    return path


def dijkstra(grid: np.ndarray, start: Node, end: Node) -> list[Node]:
    open_set = [start]
    predecessors = {}

    weights = {(i, j): math.inf for j in range(grid.shape[1]) for i in range(grid.shape[0])}
    weights[start] = 0

    while len(open_set) > 0:
        current = min(open_set, key=weights.get)
        if current == end:
            return reconstruct_path(predecessors, current)

        open_set.remove(current)
        for neighbour in get_neighbours(current, grid.shape):
            tentative_g_score = weights[current] + grid[current[1], current[0]]

            if tentative_g_score < weights[neighbour]:
                predecessors[neighbour] = current
                weights[neighbour] = tentative_g_score

                if neighbour not in open_set:
                    open_set.append(neighbour)
    raise Exception("Could not find exit node")


def sum_weights(path: list[Node], grid: np.ndarray) -> int:
    total = 0
    for coord in path:
        if coord != (0, 0):
            total += grid[coord[1], coord[0]]
    return total


def expand_grid(grid: np.ndarray) -> np.ndarray:
    new_grid = grid.copy()
    row = np.hstack([new_grid + i for i in range(5)])
    new_grid = np.vstack([row + i for i in range(5)])
    new_grid %= 9
    new_grid[new_grid == 0] = 9
    return new_grid


def part1(grid: np.ndarray) -> int:
    path = dijkstra(grid, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1))
    return sum_weights(path, grid)


def part2(grid: np.ndarray) -> int:
    grid = expand_grid(grid)
    path = dijkstra(grid, (0, 0), (grid.shape[0] - 1, grid.shape[1] - 1))
    return sum_weights(path, grid)


def solve(inputs: list) -> tuple[int, int]:
    grid = preprocess_inputs(inputs)
    return part1(grid), part2(grid)

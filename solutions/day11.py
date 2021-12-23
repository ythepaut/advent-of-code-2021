"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> np.ndarray:
    """Transforms each input to its integer value"""
    for i in range(len(inputs)):
        inputs[i] = [int(d) for d in inputs[i][:-1]]
    return np.array(inputs)


def increase_neighbours_level(energy_levels: np.ndarray, x: int, y: int) -> None:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:  # Ignore if neighbour is (x, y)
                continue
            n_x, n_y = x + i, y + j
            if n_x < 0 or n_y < 0 or n_x >= energy_levels.shape[0] or n_y >= energy_levels.shape[1]:  # Ignore if out of range
                continue
            energy_levels[n_x, n_y] += 1 if 0 < energy_levels[n_x, n_y] < 10 else 0


def update_levels(energy_levels: np.ndarray) -> int:
    """Updates octopuses levels and returns the number of highlights"""
    energy_levels += 1
    # Update neighbours
    while np.isin(10, energy_levels):
        for x in range(energy_levels.shape[0]):
            for y in range(energy_levels.shape[1]):
                if energy_levels[x, y] > 9:
                    energy_levels[x, y] = 0
                    increase_neighbours_level(energy_levels, x, y)
    return (energy_levels == 0).sum()


def part1(energy_levels: np.ndarray) -> int:
    flashes = 0
    for i in range(100):
        flashes += update_levels(energy_levels)
    return flashes


def part2(energy_levels: np.ndarray) -> int:
    step = 1
    while update_levels(energy_levels) != energy_levels.shape[0] * energy_levels.shape[1]:
        step += 1
    return step


def solve(inputs: list) -> tuple[int, int]:
    energy_levels = preprocess_inputs(inputs)
    return part1(energy_levels.copy()), part2(energy_levels)

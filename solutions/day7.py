"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> np.ndarray:
    return np.array(list(map(lambda n: int(n), inputs[0][:-1].split(","))))


def get_fuel_cost_constant(positions: np.ndarray, desired_position: int) -> int:
    costs = np.array([abs(positions[i] - desired_position) for i in range(len(positions))])
    return costs.sum()


def sum_i(i: int) -> int:
    """Returns sum of 1 to i"""
    return round((i * (i + 1)) / 2)


def get_fuel_cost_linear(positions: np.ndarray, desired_position: int) -> int:
    costs = np.array([sum_i(abs(positions[i] - desired_position)) for i in range(len(positions))])
    return costs.sum()


def part1(positions: np.ndarray) -> int:
    optimal_position = int(np.median(positions))
    return get_fuel_cost_constant(positions, optimal_position)


def part2(positions: np.ndarray) -> int:
    optimal_position = int(np.mean(positions))
    return get_fuel_cost_linear(positions, optimal_position)


def solve(inputs: list) -> tuple[int, int]:
    positions = preprocess_inputs(inputs)
    return part1(positions), part2(positions)

"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> np.ndarray:
    """Transforms each input to its integer value"""
    return np.array(list(map(lambda n: int(n), inputs[0][:-1].split(","))))


def initialize_ages(states: np.ndarray) -> np.ndarray:
    """Initialize the age array, where age[i] = number of fishes at age i"""
    ages = np.array([0 for _ in range(9)])
    for state in states:
        ages[state] += 1
    return ages


def update_ages(ages: np.ndarray) -> None:
    carry = ages[0]
    for i in range(len(ages) - 1):
        ages[i] = ages[i + 1]
    ages[-1] = carry
    ages[6] += carry


def fish_count(ages: np.ndarray, days: int) -> int:
    for i in range(days):
        update_ages(ages)
    return sum(ages)


def solve(inputs: list) -> tuple[int, int]:
    ages = initialize_ages(preprocess_inputs(inputs))
    return fish_count(ages.copy(), 80), fish_count(ages, 256)

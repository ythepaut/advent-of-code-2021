"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np


def preprocess_inputs(inputs: list) -> tuple[np.ndarray, np.ndarray]:
    """Transforms each input to its integer value"""
    patterns = []
    outputs = []
    for i in range(len(inputs)):
        note = inputs[i].split("|")
        patterns.append(note[0].split())
        outputs.append(note[1].split())
    return np.array(patterns), np.array(outputs)


def part1(outputs: np.ndarray) -> int:
    count = 0
    for output in outputs:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count


def part2(patterns: np.ndarray, outputs: np.ndarray) -> int:
    return -1


def solve(inputs: list) -> tuple[int, int]:
    patterns, outputs = preprocess_inputs(inputs)
    return part1(outputs), part2(patterns, outputs)

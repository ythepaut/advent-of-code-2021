"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

import numpy as np

OPENING_SYMBOLS = ["(", "[", "{", "<"]
CLOSING_SYMBOLS = [")", "]", "}", ">"]
CORRUPTED_SCORES = [3, 57, 1197, 25137]
INCOMPLETE_SCORES = [1, 2, 3, 4]


def preprocess_inputs(inputs: list) -> np.ndarray:
    """Transforms each input to its integer value"""
    for i in range(len(inputs)):
        inputs[i] = inputs[i][:-1]
    return np.array(inputs)


def get_line_score_and_stack(line: str) -> tuple[int, list[str]]:
    score = 0
    stack = []
    for symbol in line:
        if symbol in OPENING_SYMBOLS:
            stack.append(symbol)
        else:
            if OPENING_SYMBOLS.index(stack[-1]) != CLOSING_SYMBOLS.index(symbol):
                score += CORRUPTED_SCORES[CLOSING_SYMBOLS.index(symbol)]
            stack.pop()
    return score, stack


def part1(lines: np.ndarray) -> int:
    score = 0
    for line in lines:
        score += get_line_score_and_stack(line)[0]
    return score


def part2(lines: np.ndarray) -> int:
    scores = []
    for line in lines:
        score, stack = get_line_score_and_stack(line)
        if score == 0:
            scores.append(0)
            stack.reverse()
            for symbol in stack:
                scores[-1] *= 5
                scores[-1] += INCOMPLETE_SCORES[OPENING_SYMBOLS.index(symbol)]
    scores.sort()
    return scores[len(scores) // 2]


def solve(inputs: list) -> tuple[int, int]:
    lines = preprocess_inputs(inputs)
    return part1(lines), part2(lines)

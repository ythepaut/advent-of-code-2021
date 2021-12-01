"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""


def preprocess_inputs(inputs: list) -> None:
    """Transforms each input to its integer value"""
    for i in range(len(inputs)):
        inputs[i] = int(inputs[i])


def count_increases(values: list[int]) -> int:
    """Counts the number of increases between each values"""
    count = 0
    previous = None
    for i in values:
        if previous is not None and i > previous:
            count += 1
        previous = i
    return count


def part1(inputs: list[int]) -> int:
    return count_increases(inputs)


def part2(inputs: list[int]) -> int:
    measurement_windows = []
    for i in range(len(inputs)):
        window = inputs[i:min(i + 3, len(inputs))]
        if len(window) == 3:
            measurement_windows.append(sum(window))
    return count_increases(measurement_windows)


def solve(inputs: list) -> tuple[int, int]:
    preprocess_inputs(inputs)
    return part1(inputs), part2(inputs)

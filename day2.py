"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""


def preprocess_inputs(inputs: list) -> None:
    """Transforms each input a tuple in the format (instruction, X)"""
    for i in range(len(inputs)):
        instruction = inputs[i].split(" ")
        inputs[i] = (instruction[0], int(instruction[1]))


def part1(instructions: list[tuple[str, int]]) -> int:
    x, y = (0, 0)
    for instruction in instructions:
        if instruction[0] == "forward":
            x += instruction[1]
        elif instruction[0] == "down":
            y += instruction[1]
        elif instruction[0] == "up":
            y -= instruction[1]
        else:
            raise Exception(f"Invalid instruction \"{instruction[0]}\".")
    return x * y


def part2(instructions: list[tuple[str, int]]) -> int:
    x, y, aim = (0, 0, 0)
    for instruction in instructions:
        if instruction[0] == "forward":
            x += instruction[1]
            y += instruction[1] * aim
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]
        else:
            raise Exception(f"Invalid instruction \"{instruction[0]}\".")
    return x * y


def solve(inputs: list) -> tuple[int, int]:
    preprocess_inputs(inputs)
    return part1(inputs), part2(inputs)

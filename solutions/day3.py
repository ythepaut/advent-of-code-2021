"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""


def preprocess_inputs(inputs: list) -> int:
    """Transforms each input to a binary number and returns the number of bits per line"""
    bits = len(inputs[0]) - 1
    for i in range(len(inputs)):
        inputs[i] = bin(int(inputs[i], 2))
    return bits


def bit(number: bin, i: int) -> bin:
    """Returns i-th bit of number"""
    return int(number, 2) >> i & 1


def number_of_ones(inputs: list[bin], bits: int) -> list[int]:
    """Returns an array with the number of ones for each bit position"""
    ones = [0 for _ in range(bits)]  # Stores the number of ones in each position
    for value in inputs:
        for i in range(bits):
            if bit(value, bits - i - 1) == 1:
                ones[i] += 1
    return ones


def part1(inputs: list[bin], bits: int) -> int:
    ones = number_of_ones(inputs, bits)

    # Calculate rates
    gamma_rate = 0
    for i in range(bits):
        if ones[i] > len(inputs) / 2:
            gamma_rate += 1 << bits - i - 1
    epsilon_rate = (1 << bits) - 1 - gamma_rate

    return gamma_rate * epsilon_rate


def part2(inputs: list[bin], bits: int) -> int:
    o2_candidates = inputs.copy()
    co2_candidates = inputs.copy()

    for i in range(bits):
        if len(o2_candidates) > 1:
            most_common_bit = 1 if number_of_ones(o2_candidates, bits)[i] / len(o2_candidates) >= 0.5 else 0
            o2_candidates = [candidate for candidate in o2_candidates if bit(candidate, bits - i - 1) == most_common_bit]
        if len(co2_candidates) > 1:
            least_common_bit = 0 if number_of_ones(co2_candidates, bits)[i] / len(co2_candidates) >= 0.5 else 1
            co2_candidates = [candidate for candidate in co2_candidates if bit(candidate, bits - i - 1) == least_common_bit]

    return int(o2_candidates[0], 2) * int(co2_candidates[0], 2)


def solve(inputs: list) -> tuple[int, int]:
    bits = preprocess_inputs(inputs)
    return part1(inputs, bits), part2(inputs, bits)

"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""


def preprocess_inputs(inputs: list) -> tuple[str, dict[str, str]]:
    template = inputs[0][:-1]
    rules = {}
    for i in range(2, len(inputs)):
        before, after = inputs[i][:-1].split(" -> ")
        rules[before] = after
    return template, rules


def polymer_to_pairs(template: str) -> dict[str, int]:
    pairs = {}
    for i in range(1, len(template)):
        pair = template[i - 1:i + 1]
        if pair in pairs.keys():
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    return pairs


def update_pairs(pairs: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    new_pairs = {}
    for pair in pairs.keys():
        inserted = rules[pair]
        left_pair, right_pair = pair[0] + inserted, inserted + pair[1]
        for new_pair in [left_pair, right_pair]:
            if new_pair in new_pairs.keys():
                new_pairs[new_pair] += pairs[pair]
            else:
                new_pairs[new_pair] = pairs[pair]
    return new_pairs


def get_freq_difference_from_pairs(pairs: dict[str, int], template: str) -> int:
    letters_frequency = {}
    for pair in pairs.keys():
        for letter in [pair[0], pair[1]]:
            if letter in letters_frequency.keys():
                letters_frequency[letter] += pairs[pair]
            else:
                letters_frequency[letter] = pairs[pair]
    letters_frequency[template[0]] += 1
    letters_frequency[template[-1]] += 1
    return max(letters_frequency.values()) // 2 - min(letters_frequency.values()) // 2


def run(polymer: str, rules: dict[str, str], steps: int) -> int:
    pairs = polymer_to_pairs(polymer)
    for _ in range(steps):
        pairs = update_pairs(pairs, rules)
    return get_freq_difference_from_pairs(pairs, polymer)


def solve(inputs: list) -> tuple[int, int]:
    template, rules = preprocess_inputs(inputs)
    return run(template, rules, 10), run(template, rules, 40)

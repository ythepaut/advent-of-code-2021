"""
Advent of code 2021 - https://adventofcode.com/2021
Yohann THEPAUT (ythepaut) <contact@ythepaut.com>
"""

from __future__ import annotations


class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbours: list[Node] = []

    def __eq__(self, other: Node):
        return self.name == other.name

    def __repr__(self):
        return self.name

    def add_neighbour(self, node: Node):
        self.neighbours.append(node)


def get_node_from_list(nodes: list[Node], name: str):
    for node in nodes:
        if node.name == name:
            return node
    return None


def construct_graph(vertices: list) -> list:
    nodes = []
    for vertex in vertices:
        from_node_name, to_node_name = vertex[:-1].split("-")

        from_node = get_node_from_list(nodes, from_node_name)
        if from_node is None:
            from_node = Node(from_node_name)
            nodes.append(from_node)

        to_node = get_node_from_list(nodes, to_node_name)
        if to_node is None:
            to_node = Node(to_node_name)
            nodes.append(to_node)

        from_node.add_neighbour(to_node)
        to_node.add_neighbour(from_node)
    return nodes


def multiple_small_node_visited_twice(path: list[Node]) -> bool:
    nodes_visited_multiple_times = []
    for node in path:
        if node.name.islower() and path.count(node) > 2:
            return True
        if node.name.islower() and path.count(node) == 2 and node not in nodes_visited_multiple_times:
            nodes_visited_multiple_times.append(node)
        if len(nodes_visited_multiple_times) >= 2:
            return True
    return False


def get_paths_list(nodes: list[Node], current_node: Node, current_path: list[Node], paths: list[list[Node]], visit_twice) -> None:
    if current_node.name == "end":
        paths.append(current_path)
    else:
        for neighbour in current_node.neighbours:

            new_path = current_path.copy()
            new_path.append(neighbour)

            if not visit_twice and neighbour.name.islower() and neighbour in current_path:
                continue  # cannot visit small nodes more than once
            if visit_twice and multiple_small_node_visited_twice(new_path):
                continue  # cannot visit multiple small nodes twice
            if visit_twice and neighbour.name in ["start", "end"] and neighbour in current_path:
                continue  # cannot visit start or end node more than once

            get_paths_list(nodes, neighbour, new_path, paths, visit_twice)


def part1(nodes: list[Node]) -> int:
    print("Processing part 1...", end="\r")
    paths = []
    start_node = get_node_from_list(nodes, "start")
    get_paths_list(nodes, start_node, [start_node], paths, False)
    return len(paths)


def part2(nodes: list[Node]) -> int:
    print("Processing part 2...", end="\r")
    paths = []
    start_node = get_node_from_list(nodes, "start")
    get_paths_list(nodes, start_node, [start_node], paths, True)
    return len(paths)


def solve(inputs: list) -> tuple[int, int]:
    nodes = construct_graph(inputs)
    return part1(nodes), part2(nodes)

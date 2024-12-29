"""""Task 8 solver."""
import dataclasses
from typing import Callable
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    city_map: list[list[str]]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    number_of_unique_antinode_locations: int = 0


def get_input_from_file(file_name: str) -> TaskInput:
    """Read input data form a file.

    Args:
        file_name: Path to the file with input data.
    """
    with open(file_name, encoding="ascii") as f:
        file_content = f.read()

    return get_input_from_string(file_content)


def get_input_from_string(input_string: str) -> TaskInput:
    """Read input data form a string.

    Args:
        input_string: Input data as a string.
    """
    city_map = []

    for line in input_string.split("\n"):
        city_map.append([x for x in line])

    return TaskInput(city_map=city_map)


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Represents coordinates on a map."""
    row: int
    col: int


def _is_coords_inside_map(coords: Coordinates, height: int, width: int) -> bool:
    """Check if the coordinates are beyond the map."""
    return coords.row >= 0 and coords.row < height and coords.col >= 0 and coords.col < width


def _get_antenna_coords(task_input) -> dict[str, list[Coordinates]]:
    antennas_locations = {}
    height = len(task_input.city_map)
    width = len(task_input.city_map[0])
    for row in range(height):
        for col in range(width):
            if task_input.city_map[row][col] == ".":
                continue
            antenna_freq = task_input.city_map[row][col]
            antenna_coords = Coordinates(row, col)
            antennas_locations.setdefault(
                antenna_freq, []).append(antenna_coords)

    return antennas_locations, height, width


def _get_antinode_coords(
        task_input: TaskInput,
        get_antinodes_for_antennas: Callable[[
            Coordinates, Coordinates, int, int], set[Coordinates]]
) -> set[Coordinates]:
    antennas_locations, height, width = _get_antenna_coords(task_input)
    antinode_locations = set()
    for coords in antennas_locations.values():
        for first_antenna_index in range(len(coords) - 1):
            for second_antenna_index in range(first_antenna_index + 1, len(coords)):
                antinode_locations |= get_antinodes_for_antennas(
                    coords[first_antenna_index],
                    coords[second_antenna_index],
                    height, width
                )

    return antinode_locations


def _get_antinodes_for_antennas_p1(
    first_antenna_coords: Coordinates,
    second_antenna_coords: Coordinates,
    height: int, width: int
) -> set[Coordinates]:
    d_row = second_antenna_coords.row - first_antenna_coords.row
    d_col = second_antenna_coords.col - first_antenna_coords.col
    antinode_locations = set()

    antinode_location = Coordinates(
        first_antenna_coords.row - d_row,
        first_antenna_coords.col - d_col
    )
    if _is_coords_inside_map(antinode_location, height, width):
        antinode_locations.add(antinode_location)

    antinode_location = Coordinates(
        second_antenna_coords.row + d_row,
        second_antenna_coords.col + d_col
    )
    if _is_coords_inside_map(antinode_location, height, width):
        antinode_locations.add(antinode_location)

    return antinode_locations


def _get_antinodes_for_antennas_p2(
    first_antenna_coords: Coordinates,
    second_antenna_coords: Coordinates,
    height: int, width: int
) -> set[Coordinates]:
    d_row = second_antenna_coords.row - first_antenna_coords.row
    d_col = second_antenna_coords.col - first_antenna_coords.col
    antinode_locations = set()

    antinode_location = dataclasses.replace(first_antenna_coords)

    while True:
        antinode_location = Coordinates(
            antinode_location.row - d_row,
            antinode_location.col - d_col
        )
        if _is_coords_inside_map(antinode_location, height, width):
            antinode_locations.add(antinode_location)
        else:
            break

    antinode_location = dataclasses.replace(second_antenna_coords)

    while True:
        antinode_location = Coordinates(
            antinode_location.row + d_row,
            antinode_location.col + d_col
        )
        if _is_coords_inside_map(antinode_location, height, width):
            antinode_locations.add(antinode_location)
        else:
            break
    antinode_locations.add(first_antenna_coords)
    antinode_locations.add(second_antenna_coords)

    return antinode_locations


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    antinode_locations = _get_antinode_coords(
        task_input, _get_antinodes_for_antennas_p1)

    return TaskSolution(
        number_of_unique_antinode_locations=len(antinode_locations)
    )


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."

    antinode_locations = _get_antinode_coords(
        task_input, _get_antinodes_for_antennas_p2)

    return TaskSolution(
        number_of_unique_antinode_locations=len(antinode_locations)
    )

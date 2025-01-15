"""""Task 20 solver."""
import dataclasses
import enum
from code_advent_2024.tasks import task

_WALL_CHAR = "#"
_START_POSITION_CHAR = "S"
_END_POSITION_CHAR = "E"


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Position in the map."""
    row: int = 0
    col: int = 0


@dataclasses.dataclass(frozen=True)
class CoordinatesDelta:
    """Position in the map."""
    d_row: int = 0
    d_col: int = 0


class Direction(enum.IntEnum):
    """Directions in the map."""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


_DIRECTION_DELTA = {
    Direction.NORTH: CoordinatesDelta(d_row=-1, d_col=0),
    Direction.EAST: CoordinatesDelta(d_row=0, d_col=1),
    Direction.SOUTH: CoordinatesDelta(d_row=1, d_col=0),
    Direction.WEST: CoordinatesDelta(d_row=0, d_col=-1)
}


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    start: Coordinates = None
    end: Coordinates = None
    walls: frozenset[Coordinates] = frozenset()
    min_number_of_saved_picoseconds: int = 100


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    number_of_cheats: int = 0


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
    walls = []
    start = None
    end = None
    for row_idx, line in enumerate(input_string.split("\n")):
        for col_idx, char in enumerate(line):
            coord = Coordinates(row=row_idx, col=col_idx)
            if char == _WALL_CHAR:
                walls.append(coord)
            elif char == _START_POSITION_CHAR:
                start = coord
            elif char == _END_POSITION_CHAR:
                end = coord

    return TaskInput(start=start, end=end, walls=frozenset(walls))


def _build_trail(
    walls: frozenset[Coordinates],
    start: Coordinates,
    end: Coordinates
) -> dict[Coordinates, int]:
    trail = {}
    current_position = start
    prev_position = None
    number_of_steps = 0
    trail[current_position] = number_of_steps
    while current_position != end:
        current_position, prev_position = _get_next_position(
            walls=walls,
            current_position=current_position,
            prev_position=prev_position
        )
        number_of_steps += 1
        trail[current_position] = number_of_steps

    return trail


def _get_next_position(
    walls: frozenset[Coordinates],
    current_position: Coordinates,
    prev_position: Coordinates
) -> Coordinates:
    for direction in Direction:
        next_position = Coordinates(
            row=current_position.row + _DIRECTION_DELTA[direction].d_row,
            col=current_position.col + _DIRECTION_DELTA[direction].d_col
        )
        if next_position not in walls and next_position != prev_position:
            return next_position, current_position

    return current_position, prev_position


def _calc_cheats(
    walls: frozenset[Coordinates],
    trail: dict[Coordinates, int],
    min_number_of_saved_picoseconds: int
) -> int:
    saved_time_to_number_of_cheats = {}
    for position, steps in trail.items():
        for direction in Direction:
            next_coord = Coordinates(
                row=position.row + _DIRECTION_DELTA[direction].d_row,
                col=position.col + _DIRECTION_DELTA[direction].d_col
            )
            next_next_coord = Coordinates(
                row=next_coord.row + _DIRECTION_DELTA[direction].d_row,
                col=next_coord.col + _DIRECTION_DELTA[direction].d_col
            )
            if (
                next_coord in walls
                and next_next_coord in trail
                and trail[next_next_coord] > steps
            ):
                saved_picoseconds = trail[next_next_coord] - steps - 2
                saved_time_to_number_of_cheats.setdefault(
                    saved_picoseconds, 0
                )
                saved_time_to_number_of_cheats[saved_picoseconds] += 1

    return sum(
        number_of_cheats
        for saved_time, number_of_cheats in saved_time_to_number_of_cheats.items()
        if saved_time >= min_number_of_saved_picoseconds
    )


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    trail = _build_trail(
        walls=task_input.walls,
        start=task_input.start,
        end=task_input.end
    )

    number_of_cheats = _calc_cheats(
        walls=task_input.walls,
        trail=trail,
        min_number_of_saved_picoseconds=task_input.min_number_of_saved_picoseconds
    )

    return TaskSolution(number_of_cheats=number_of_cheats)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    number_of_cheats = 0

    return TaskSolution(number_of_cheats=number_of_cheats)

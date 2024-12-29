"""""Task 10 solver."""
import dataclasses
from code_advent_2024.tasks import task


_TRAILHEAD = 0
_TRAILTAIL = 9

_DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    topographic_map: list[list[int]]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    sum_of_scores_of_all_trailheads: int = 0


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

    topographic_map = []
    for line in input_string.split("\n"):
        topographic_map.append([int(x) for x in line])

    return TaskInput(topographic_map=topographic_map)


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Represents coordinates on a map."""
    row: int
    col: int


def _is_coords_inside_map(coords: Coordinates, height: int, width: int) -> bool:
    """Check if the coordinates are beyond the map."""
    return coords.row >= 0 and coords.row < height and coords.col >= 0 and coords.col < width


def _get_all_trail_tails(task_input: TaskInput) -> set[Coordinates]:
    """Get all trailheads on the map."""
    trailtails = set()
    height = len(task_input.topographic_map)
    width = len(task_input.topographic_map[0])

    for row in range(height):
        for col in range(width):
            location_value = task_input.topographic_map[row][col]
            if location_value == _TRAILTAIL:
                trailtails.add(Coordinates(row=row, col=col))

    return trailtails


def _calc_reachable_trailheads(
    cur_position: Coordinates,
    topographic_map: list[list[int]]
) -> list[Coordinates]:
    """Calculate reachable trailheads for each trailtail."""
    if topographic_map[cur_position.row][cur_position.col] == _TRAILHEAD:
        return [cur_position]

    reachable_trailheads = []
    for direction in _DIRECTIONS:
        next_position = Coordinates(
            row=cur_position.row + direction[0],
            col=cur_position.col + direction[1]
        )

        if (
            _is_coords_inside_map(
                next_position, len(topographic_map), len(topographic_map[0])
            )
            and (
                topographic_map[cur_position.row][cur_position.col] - 1
                == topographic_map[next_position.row][next_position.col]
            )
        ):
            reachable_trailheads.extend(
                _calc_reachable_trailheads(next_position, topographic_map)
            )

    return reachable_trailheads


def _calc_all_trails(task_input):
    trailtails = _get_all_trail_tails(task_input)
    trails: dict[Coordinates, list[Coordinates]] = {}
    for trailtail in trailtails:
        reachable_trailheads = _calc_reachable_trailheads(
            trailtail,
            task_input.topographic_map
        )
        for trailhead in reachable_trailheads:
            trails.setdefault(trailhead, []).append(trailtail)
    return trails


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    trails = _calc_all_trails(task_input)

    sum_of_scores_of_all_trailheads = sum(
        [len(set(trails_from_head)) for trails_from_head in trails.values()]
    )

    return TaskSolution(sum_of_scores_of_all_trailheads=sum_of_scores_of_all_trailheads)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    trails = _calc_all_trails(task_input)

    sum_of_scores_of_all_trailheads = sum(
        [len(trails_from_head) for trails_from_head in trails.values()]
    )

    return TaskSolution(sum_of_scores_of_all_trailheads=sum_of_scores_of_all_trailheads)

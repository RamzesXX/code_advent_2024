"""""Task 16 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Position in the map."""
    x: int = 0
    y: int = 0


@dataclasses.dataclass(frozen=True)
class CoordinatesDeltas:
    """Position in the map."""
    dx: int = 0
    dy: int = 0


_COORD_DELTAS = (
    CoordinatesDeltas(0, 1),
    CoordinatesDeltas(0, -1),
    CoordinatesDeltas(1, 0),
    CoordinatesDeltas(-1, 0),
)


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    coordinates: list[Coordinates]
    start: Coordinates = Coordinates(0, 0)
    end: Coordinates = Coordinates(70, 70)


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    min_number_of_steps: int = 0


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
    coordinates = []
    for line in input_string.split("\n"):
        x, y = line.split(",")
        coordinates.append(Coordinates(int(x), int(y)))

    return TaskInput(coordinates=coordinates)


def find_the_shortes_path(
    obstacles: list[Coordinates],
    start: Coordinates,
    end: Coordinates
) -> int:
    """."""
    visited_coordinates = {}
    coord_to_process = [(start, 0)]
    while coord_to_process:
        current_coord, steps = coord_to_process.pop(0)
        visited_coordinates[current_coord] = steps

        if current_coord == end:
            return steps
        for direction in _COORD_DELTAS:
            next_coord = Coordinates(
                current_coord.x + direction.dx,
                current_coord.y + direction.dy
            )
            if (
                0 <= next_coord.x <= end.x
                and 0 <= next_coord.y <= end.y
                and next_coord not in obstacles
                and next_coord not in visited_coordinates
                and ((next_coord, steps + 1) not in coord_to_process)
            ):
                coord_to_process.append((next_coord, steps + 1))

    return -1


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    min_number_of_steps = find_the_shortes_path(
        obstacles=task_input.coordinates[:1024],
        start=task_input.start,
        end=task_input.end
    )

    return TaskSolution(min_number_of_steps=min_number_of_steps)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    min_number_of_steps = 0

    return TaskSolution(min_number_of_steps=min_number_of_steps)

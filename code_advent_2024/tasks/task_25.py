"""""Task 25 solver."""
import dataclasses
from code_advent_2024.tasks import task

_EMPTY = "."
_MAX_HEIGHT = 5


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    keys: tuple[tuple[int, int, int, int, int]] = tuple()
    locks: tuple[tuple[int, int, int, int, int]] = tuple()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    number_of_matching_key_lock_pairs: int = 0


def get_input_from_file(file_name: str) -> TaskInput:
    """Read input data form a file.

    Args:
        file_name: Path to the file with input data.
    """
    with open(file_name, encoding="ascii") as f:
        file_content = f.read()

    return get_input_from_string(file_content)


def _extract_element(lines: list[str]) -> tuple[int, int, int, int, int]:
    element = [0] * 5
    for line in lines:
        for i, char in enumerate(line):
            element[i] += 0 if char == _EMPTY else 1

    return tuple(element)


def get_input_from_string(input_string: str) -> TaskInput:
    """Read input data form a string.

    Args:
        input_string: Input data as a string.
    """
    keys = []
    locks = []
    for element_strings in input_string.split("\n\n"):
        lines = element_strings.split("\n")
        if element_strings[0] == _EMPTY:
            lines.reverse()
            collection = keys
        else:
            collection = locks
        element = _extract_element(lines=lines[1:-1])
        collection.append(element)

    return TaskInput(
        keys=tuple(keys),
        locks=tuple(locks)
    )


def _build_correcponding_element(
    element: tuple[int, int, int, int, int]
) -> tuple[int, int, int, int, int]:
    return tuple([(_MAX_HEIGHT - x) for x in element])


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    keys = set(task_input.keys)
    locks = set(task_input.locks)
    number_of_matching_key_lock_pairs = 0
    for key in keys:
        for lock in locks:
            if all(x + y <= _MAX_HEIGHT for x, y in zip(key, lock)):
                number_of_matching_key_lock_pairs += 1

    return TaskSolution(number_of_matching_key_lock_pairs=number_of_matching_key_lock_pairs)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(number_of_matching_key_lock_pairs=0)

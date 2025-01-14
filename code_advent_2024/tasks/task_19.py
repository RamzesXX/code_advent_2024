"""""Task 19 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    available_patterns: tuple[str] = tuple()
    designs_to_display: tuple[str] = tuple()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    number_of_possible_designs: int = 0


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
    available_patterns = []
    designs_to_display = []
    is_processing_designs = False
    for line in input_string.split("\n"):
        if not line:
            is_processing_designs = True
            continue
        if is_processing_designs:
            designs_to_display.append(line)
        else:
            available_patterns = line.split(", ")

    return TaskInput(
        available_patterns=tuple(available_patterns),
        designs_to_display=tuple(designs_to_display)
    )


def _check_if_design_can_be_built(available_patterns: dict[str, list[str]], design: str) -> bool:
    used_patterns = []

    pointer = 0
    index = 0
    while pointer < len(design):
        if pointer < 0:
            return False
        if design[pointer] not in available_patterns:
            if not used_patterns:
                return False
            index, used_pattern = used_patterns.pop(-1)
            index += 1
            pointer -= len(used_pattern)
            continue

        available_patterns_for_letter = available_patterns.get(design[pointer])

        if index >= len(available_patterns_for_letter):
            if not used_patterns:
                return False
            index, used_pattern = used_patterns.pop(-1)
            index += 1
            pointer -= len(used_pattern)
            continue

        pattern = available_patterns_for_letter[index]
        if design[pointer:].startswith(pattern):
            used_patterns.append((index, pattern))
            pointer += len(pattern)
            index = 0
            continue

        index += 1

    return True


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    available_patterns = {}
    for pattern in sorted(task_input.available_patterns):
        available_patterns.setdefault(pattern[0], []).append(pattern)
    number_of_possible_designs = 0
    for index, design in enumerate(task_input.designs_to_display):
        if _check_if_design_can_be_built(available_patterns, design):
            number_of_possible_designs += 1
        task.show_progress(index, len(task_input.designs_to_display))

    return TaskSolution(number_of_possible_designs=number_of_possible_designs)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(number_of_possible_designs=0)

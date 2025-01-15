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


def _mormalize_available_patterns(available_patterns: tuple[str]) -> dict[str, list[str]]:
    available_patterns = sorted(available_patterns, key=len)
    mormalized_available_patterns = {}
    for available_pattern in available_patterns:
        if not _check_if_design_can_be_built(mormalized_available_patterns, available_pattern):
            mormalized_available_patterns.setdefault(
                available_pattern[0], []).append(available_pattern)
    mormalized_available_patterns = {
        key: sorted(value)
        for key, value in mormalized_available_patterns.items()
    }

    return mormalized_available_patterns


def _check_if_design_can_be_built(available_patterns: dict[str, list[str]], design: str) -> bool:
    used_patterns = []

    pointer = 0
    index = 0
    while pointer < len(design):
        if pointer < 0:
            return False
        letter = design[pointer]
        if letter not in available_patterns:
            if not used_patterns:
                return False
            index, used_pattern = used_patterns.pop(-1)
            index += 1
            pointer -= len(used_pattern)
            continue

        available_patterns_for_letter = available_patterns.get(letter)
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
    available_patterns = _mormalize_available_patterns(
        task_input.available_patterns
    )
    number_of_possible_designs = 0
    for index, design in enumerate(task_input.designs_to_display):
        if _check_if_design_can_be_built(available_patterns, design):
            number_of_possible_designs += 1
        task.show_progress(len(task_input.designs_to_display), index)

    return TaskSolution(number_of_possible_designs=number_of_possible_designs)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(number_of_possible_designs=0)

"""Task solver."""
import dataclasses
import abc


@dataclasses.dataclass(frozen=True)
class TaskInput(abc.ABC):
    "Represents task's input."


@dataclasses.dataclass(frozen=True)
class TaskSolution(abc.ABC):
    "Represents task's solution."


def get_input_from_file(file_name: str) -> TaskInput:
    """Read input data form a file.

    Args:
        file_name: Path to the file with input data.
    """
    raise NotImplementedError()


def get_input_from_string(input_string: str) -> TaskInput:
    """Read input data form a string.

    Args:
        input_string: Input data as a string.
    """
    raise NotImplementedError()


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    raise NotImplementedError()


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    raise NotImplementedError()


def show_progress(total: int, current: int):
    "Show progress of the task."
    current_percent = min(100, int(100 * current / total))
    progress = f"Progress {current_percent}%"

    print(f"\r{progress}", end="")

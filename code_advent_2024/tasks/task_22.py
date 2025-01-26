"""""Task 22 solver.
Tip: don't do all 2000 iterations once find the cycle we can just
calculate index of the value.
"""
import dataclasses
from code_advent_2024.tasks import task

_NUMBER_OF_ITERATIONS = 2000


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    origin_secret_numbers: tuple[int] = ()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    sum_of_generated_secret_numbers: int = 0


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
    secret_numbers = tuple(int(x) for x in input_string.split())

    return TaskInput(origin_secret_numbers=secret_numbers)


def _prune(secret_number: int) -> int:
    return secret_number % 16777216


def _mix(secret_number: int, number) -> int:

    return secret_number ^ number


def calc_next_secret_number(secret_number: int) -> int:
    """Calculate next secret number."""
    secret_number = _prune(_mix(secret_number, secret_number << 6))
    secret_number = _prune(_mix(secret_number, secret_number >> 5))
    secret_number = _prune(_mix(secret_number, secret_number << 11))

    return secret_number


def get_secret_number_after_iterations(
    origin_secret_number: int,
    number_of_iterations: int
) -> int:
    """Get secret number after performed iterations."""
    number_of_iteration = 0
    secret_numbers = []
    secret_number = origin_secret_number
    while (
        number_of_iteration < number_of_iterations
        and secret_number not in secret_numbers
    ):
        secret_numbers.append(secret_number)
        secret_number = calc_next_secret_number(secret_number)
        number_of_iteration += 1

    if number_of_iteration == number_of_iterations:
        return secret_number

    index = number_of_iterations % number_of_iteration
    return secret_numbers[index]


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    sum_of_generated_secret_numbers = sum(
        get_secret_number_after_iterations(
            origin_secret_number=secret_number,
            number_of_iterations=_NUMBER_OF_ITERATIONS
        )
        for secret_number in task_input.origin_secret_numbers
    )

    return TaskSolution(sum_of_generated_secret_numbers=sum_of_generated_secret_numbers)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(sum_of_generated_secret_numbers=0)

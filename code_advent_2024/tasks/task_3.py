"""""Task 1 solver."""
import re
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    mul_string: str


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    sum_of_mul: int


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
    return TaskInput(mul_string=input_string)


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    sum_of_mul = 0
    mul_strings = re.findall(
        r"mul\((\d{1,3}),(\d{1,3})\)",
        task_input.mul_string
    )
    for a, b in mul_strings:
        sum_of_mul += int(a) * int(b)

    return TaskSolution(sum_of_mul=sum_of_mul)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    sum_of_mul = 0
    do_mul = True
    tokens = re.findall(
        r"(mul|do|don't)\(((\d{1,3}),(\d{1,3}))?\)", task_input.mul_string)
    for token in tokens:
        if token[0] == "mul" and do_mul:
            sum_of_mul += int(token[2]) * int(token[3])
        elif token[0] == "do":
            do_mul = True
        elif token[0] == "don't":
            do_mul = False

    return TaskSolution(sum_of_mul=sum_of_mul)

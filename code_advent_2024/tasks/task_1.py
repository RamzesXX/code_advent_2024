"""""Task 1 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    left: list[int]
    right: list[int]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    distance: int = None
    similarity_score: int = None


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
    left = []
    right = []
    for line in input_string.split("\n"):
        left_value, right_value = line.split()
        left.append(int(left_value))
        right.append(int(right_value))

    return TaskInput(left, right)


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    task_input = TaskInput(sorted(task_input.left),
                           sorted(task_input.right))

    diff = [
        abs(task_input.left[i] - task_input.right[i])
        for i in range(len(task_input.left))
    ]
    distance = sum(diff)

    return TaskSolution(distance=distance)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    occurences = {}
    for el in task_input.right:
        occurences.update({el: occurences.get(el, 0) + 1})

    similarity_score = sum(el * occurences.get(el, 0)
                           for el in task_input.left)

    return TaskSolution(similarity_score=similarity_score)

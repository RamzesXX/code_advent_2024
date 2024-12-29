"""""Task 1 solver."""
import dataclasses
from code_advent_2024.tasks import task

WORD_TO_SCAN_PART_1 = "XMAS"
DIRECTIONS_PART_1 = [
    [1,  1], [1,  0], [1, -1],
    [0,  1], [0, -1],
    [-1, 1], [-1, 0], [-1, -1],
]
WORDS_TO_SCAN_PART_2 = ["MAS", "SAM"]
DIRECTIONS_PART_2 = [
    [[-1,  -1], [0, 0], [1, 1]],
    [[-1,   1], [0, 0], [1, -1]],
]


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    puzzle: list[str]


@dataclasses.dataclass(frozen=True)
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    count: int


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
    puzzle = input_string.split("\n")

    return TaskInput(puzzle=puzzle)


def _count_for_position(task_input: TaskInput, x: int, y: int) -> int:
    if task_input.puzzle[y][x] != WORD_TO_SCAN_PART_1[0]:
        return 0

    count = 0
    word_len = len(WORD_TO_SCAN_PART_1)
    for direction in DIRECTIONS_PART_1:
        if (
            y + (word_len - 1) * direction[0] < 0
            or y + (word_len - 1) * direction[0] >= len(task_input.puzzle)
            or x + (word_len - 1) * direction[1] < 0
            or x + (word_len - 1) * direction[1] >= len(task_input.puzzle[y])
        ):
            continue
        for index, character in enumerate(WORD_TO_SCAN_PART_1):
            new_y = y + index * direction[0]
            new_x = x + index * direction[1]
            if task_input.puzzle[new_y][new_x] != character:
                break
        else:
            count += 1

    return count


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    count = 0
    for y, line in enumerate(task_input.puzzle):
        for x, _ in enumerate(line):
            count += _count_for_position(task_input=task_input, x=x, y=y)

    return TaskSolution(count=count)


def _check_for_x_mas(task_input: TaskInput, x: int, y: int) -> int:
    if (
            task_input.puzzle[y][x] != "A"
            or y - 1 < 0
            or y + 1 >= len(task_input.puzzle)
            or x - 1 < 0
            or x + 1 >= len(task_input.puzzle[y])
    ):
        return 0

    first_word_letters = []
    for direction in DIRECTIONS_PART_2[0]:
        new_y = y + direction[0]
        new_x = x + direction[1]
        first_word_letters.append(task_input.puzzle[new_y][new_x])
    second_word_letters = []
    for direction in DIRECTIONS_PART_2[1]:
        new_y = y + direction[0]
        new_x = x + direction[1]
        second_word_letters.append(task_input.puzzle[new_y][new_x])

    first_word = "".join(first_word_letters)
    second_word = "".join(second_word_letters)

    if first_word in WORDS_TO_SCAN_PART_2 and second_word in WORDS_TO_SCAN_PART_2:
        return 1

    return 0


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    count = 0
    for y, line in enumerate(task_input.puzzle):
        for x, _ in enumerate(line):
            count += _check_for_x_mas(task_input=task_input, x=x, y=y)

    return TaskSolution(count=count)

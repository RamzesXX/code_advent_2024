"""Task 5 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    page_ordering_rules_values_after: dict[int, set[int]]
    updates: list[list[int]]


@dataclasses.dataclass(frozen=True)
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    sum_of_middle_page_numbers: int


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
    rules_after = {}
    updates = []
    reading_page_ordering_rules = True
    for line in input_string.split("\n"):
        if not line.strip():
            reading_page_ordering_rules = False
            continue
        if reading_page_ordering_rules:
            before, after = line.split("|")
            before = int(before)
            after = int(after)
            rules_after.setdefault(before, set()).add(int(after))
        else:
            updates.append([int(x_) for x_ in line.split(",")])

    return TaskInput(page_ordering_rules_values_after=rules_after,
                     updates=updates)


def is_update_correct(update: list[int], values_after: dict[int, set[int]]) -> bool:
    """Check if update is correct."""
    for index in range(len(update) - 1):
        cur_value = update[index]
        next_value = update[index + 1]
        if next_value in values_after.get(cur_value, set()):
            continue
        return False

    return True


def _get_middle_of_the_correct_update(update: list[int]) -> int:
    return update[len(update) // 2]


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    sum_of_middle_page_numbers = sum(
        _get_middle_of_the_correct_update(update)
        for update in task_input.updates
        if is_update_correct(
            update,
            task_input.page_ordering_rules_values_after,
        )
    )
    return TaskSolution(sum_of_middle_page_numbers=sum_of_middle_page_numbers)


def correct_update(update: list[int], values_after: dict[int, set[int]]) -> list[int]:
    """Fixes update."""
    stat = []
    for el in update:
        elements_after = values_after.get(el, set())
        update_values_after = elements_after.intersection(set(update))
        stat.append((el, update_values_after))
    corrected_update = map(
        lambda el: el[0],
        sorted(stat, key=lambda el: len(el[1]), reverse=True)
    )
    return list(corrected_update)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    sum_of_middle_page_numbers = sum(
        _get_middle_of_the_correct_update(
            correct_update(
                update,
                task_input.page_ordering_rules_values_after,
            )
        )
        for update in task_input.updates
        if not is_update_correct(
            update,
            task_input.page_ordering_rules_values_after,
        )
    )
    return TaskSolution(sum_of_middle_page_numbers=sum_of_middle_page_numbers)

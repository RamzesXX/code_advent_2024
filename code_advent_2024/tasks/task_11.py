"""""Task 11 solver."""
import dataclasses
import math
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    stones: list[int]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    number_of_stones: int = 0


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

    stones = [int(x) for x in input_string.split()]

    return TaskInput(stones=stones)


def _blink(stones_frequency: dict[int, int]) -> dict[int, int]:
    """Blink stones with frequency."""
    new_stone_frequency = {}
    for stone, frequency in stones_frequency.items():
        if stone == 0:
            new_stone = 1
            new_stone_frequency[new_stone] = new_stone_frequency.get(
                new_stone, 0) + frequency
        elif int(math.log10(stone)) % 2:
            power = (int(math.log10(stone)) + 1) // 2
            new_stone = stone // 10 ** power
            new_stone_frequency[new_stone] = new_stone_frequency.get(
                new_stone, 0) + frequency
            new_stone = stone % 10 ** power
            new_stone_frequency[new_stone] = new_stone_frequency.get(
                new_stone, 0) + frequency
        else:
            new_stone = stone * 2024
            new_stone_frequency[new_stone] = new_stone_frequency.get(
                new_stone, 0) + frequency

    return new_stone_frequency


def _get_stone_frequency(stones: list[int]) -> dict[int, int]:
    stones_frequency = {}
    for stone in stones:
        stones_frequency[stone] = stones_frequency.get(stone, 0) + 1

    return stones_frequency


def _calc_number_of_stones_after_blinks(task_input: TaskInput, number_of_blinks: int) -> int:
    stone_frequency = _get_stone_frequency(task_input.stones)
    for blink_number in range(number_of_blinks):
        task.show_progress(total=number_of_blinks, current=blink_number+1)
        stone_frequency = _blink(stone_frequency)
    print()
    return sum(stone_frequency.values())


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    number_of_stones = _calc_number_of_stones_after_blinks(task_input, 25)

    return TaskSolution(number_of_stones=number_of_stones)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task. """
    number_of_stones = _calc_number_of_stones_after_blinks(task_input, 75)

    return TaskSolution(number_of_stones=number_of_stones)

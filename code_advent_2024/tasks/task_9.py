"""""Task 9 solver."""
import dataclasses
from code_advent_2024.tasks import task

_FREE_SPACE_ID = -1
_NOT_FOUND_POSITION = -1


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    disk_map: list[int]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    filesystem_checksum: int = 0


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
    disk_map = [int(x) for x in input_string.strip()]

    return TaskInput(disk_map=disk_map)


def _build_block_map(disk_map: list[int]) -> list[int]:
    block_map = []
    cur_file_id = -1
    for block_type_, block_length_ in enumerate(disk_map):
        if block_type_ % 2:
            cur_element = _FREE_SPACE_ID
        else:
            cur_file_id += 1
            cur_element = cur_file_id

        block_map.extend([cur_element] * block_length_)

    return block_map


def _calculate_checksum(block_map: list[int]) -> int:
    return sum(
        index * block
        for index, block in enumerate(block_map) if block != _FREE_SPACE_ID
    )


def _defrag_p1(block_map: list[int]) -> list[int]:
    left = 0
    right = len(block_map) - 1
    defragged_block_map = []
    while left <= right:
        if block_map[left] != _FREE_SPACE_ID:
            defragged_block_map.append(block_map[left])
            left += 1
        elif block_map[right] == _FREE_SPACE_ID:
            right -= 1
        elif block_map[right] != _FREE_SPACE_ID:
            defragged_block_map.append(block_map[right])
            left += 1
            right -= 1

    return defragged_block_map


def _calc_start_of_occupied_block(block_map: list[int], last_block: int) -> int:
    block_id = block_map[last_block]
    i = last_block
    while i >= 0 and block_map[i] == block_id:
        i -= 1

    return i + 1


def _find_start_of_free_space(
        block_map: list[int],
        start_index: int,
        end_index: int,
        file_length: int
) -> int:
    free_block_length = 0
    while start_index <= end_index:
        if block_map[start_index] != _FREE_SPACE_ID:
            free_block_length = 0
        else:
            free_block_length += 1
            if free_block_length >= file_length:
                return start_index - free_block_length + 1
        start_index += 1

    return _NOT_FOUND_POSITION


def _defrag_p2(block_map: list[int]) -> list[int]:
    print("Progress:")
    left = 0
    right = len(block_map) - 1
    length = len(block_map)
    defragged_block_map = list(block_map)
    task.show_progress(total=length, current=0)
    while left <= right:
        if defragged_block_map[left] != _FREE_SPACE_ID:
            left += 1
        elif defragged_block_map[right] == _FREE_SPACE_ID:
            right -= 1
        elif defragged_block_map[right] != _FREE_SPACE_ID:
            file_last_block = right
            file_first_block = _calc_start_of_occupied_block(
                block_map, file_last_block)
            file_length = file_last_block - file_first_block + 1
            free_block_start = _find_start_of_free_space(
                block_map, left, file_first_block - 1, file_length)
            if free_block_start != _NOT_FOUND_POSITION:
                free_block_end = free_block_start + file_length - 1
                defragged_block_map = (
                    defragged_block_map[:free_block_start] +
                    defragged_block_map[file_first_block:file_last_block + 1] +
                    defragged_block_map[free_block_end + 1:file_first_block] +
                    defragged_block_map[free_block_start:free_block_end + 1] +
                    defragged_block_map[file_last_block + 1:]
                )
            right = file_first_block - 1
        task.show_progress(total=length, current=length-right+left)
    print()

    return defragged_block_map


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    block_map = _build_block_map(task_input.disk_map)
    defragmented_block_map = _defrag_p1(block_map)
    checksum = _calculate_checksum(defragmented_block_map)

    return TaskSolution(filesystem_checksum=checksum)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    block_map = _build_block_map(task_input.disk_map)
    defragmented_block_map = _defrag_p2(block_map)
    checksum = _calculate_checksum(defragmented_block_map)

    return TaskSolution(filesystem_checksum=checksum)

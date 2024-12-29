"""Task runner for Advent of Code 2024."""
import importlib
import os
from types import ModuleType
from typing import Any


_INPUT_FILE_NAME_TEMPLATE = "input_{task_number}.txt"
_TASK_MODULE_NAME_TEMPLATE = "code_advent_2024.tasks.task_{task_number}"


def _get_task_module(task_number) -> ModuleType:
    """Get task package"""
    try:
        module_name = _TASK_MODULE_NAME_TEMPLATE.format(
            task_number=task_number)
        module = importlib.import_module(module_name)
        return module
    except ModuleNotFoundError as e:
        raise ValueError(
            "Task number should be in interval [1;50] inclusevely.") from e


def _build_input_file_name(task_number: int, path_to_input_files_folder: str) -> str:
    """Builds path to the file with input data for a specific task."""
    input_file_name = _INPUT_FILE_NAME_TEMPLATE.format(task_number=task_number)
    path_to_input_file_name = os.path.join(
        path_to_input_files_folder, input_file_name)

    return path_to_input_file_name


def solve_part1(task_number: int, path_to_input_files_folder: str) -> Any:
    """Solves part 1 of a specific task."""
    task_module = _get_task_module(task_number)
    path_to_input_file = _build_input_file_name(
        task_number, path_to_input_files_folder)
    task_input = task_module.get_input_from_file(path_to_input_file)

    return task_module.solve_part1(task_input)


def solve_part2(task_number: int, path_to_input_files_folder: str) -> Any:
    """Solves part 2 of a specific task."""
    task_module = _get_task_module(task_number)
    path_to_input_file = _build_input_file_name(
        task_number, path_to_input_files_folder)
    task_input = task_module.get_input_from_file(path_to_input_file)

    return task_module.solve_part2(task_input)

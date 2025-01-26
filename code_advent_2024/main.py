"""Entry point for python implementation of Advent code."""
from pathlib import Path

from absl import app
from absl import flags
from absl import logging

from code_advent_2024 import task_runner

_TASK_NUMBER = flags.DEFINE_integer(
    name="task_number",
    default=25,
    help="Task number",
    lower_bound=1,
    upper_bound=25,
    # required=True,
)

_PATH_TO_INPUT_FILES = flags.DEFINE_string(
    name="path_to_input_files",
    default=None,
    help="Path to input files folder",
)


def main(argv: list[str]):
    """Main function."""
    del argv

    task_number = _TASK_NUMBER.value
    if _PATH_TO_INPUT_FILES.present:
        path_to_input_files_folder = _PATH_TO_INPUT_FILES.value
    else:
        path_to_project_root = Path(__file__).parent.parent
        path = path_to_project_root.joinpath('input')
        path_to_input_files_folder = path.absolute()

    logging.info("Task number: %s", task_number)
    logging.info("Path to input files folder: %s", path_to_input_files_folder)

    solution = task_runner.solve_part1(task_number, path_to_input_files_folder)
    logging.info("Part 1: %s", solution)
    solution = task_runner.solve_part2(task_number, path_to_input_files_folder)
    logging.info("Part 2: %s", solution)


if __name__ == "__main__":
    app.run(main)

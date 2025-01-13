"""""Task 17 solver."""
import dataclasses
import enum
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    program_output: str = ""


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

    # maze_map = {}
    # start_postion = None
    # end_postion = None
    # reindeer = None
    # for row_idx,  line in enumerate(input_string.split("\n")):
    #     for col_idx, char in enumerate(line):
    #         if char == _WALL_CHAR:
    #             maze_map[Position(row=row_idx, col=col_idx)] = _WALL_CHAR
    #         elif char == _START_POSITION_CHAR:
    #             start_postion = Position(row=row_idx, col=col_idx)
    #             reindeer = DirectedPosition(
    #                 position=start_postion,
    #                 direction=Direction.EAST
    #             )
    #         elif char == _END_POSITION_CHAR:
    #             end_postion = Position(row=row_idx, col=col_idx)

    return TaskInput()


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    return TaskSolution(program_output="")


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(program_output="")

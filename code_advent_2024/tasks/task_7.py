"""""Task 7 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class CalibrationEquation:
    "Represents a calibration equation."
    result: int
    operands: list[int]


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    calibration_equations: list[CalibrationEquation]


@dataclasses.dataclass(frozen=True)
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    total_calibration_result: int


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
    calibration_equations = []
    for line in input_string.split("\n"):
        result, operands = line.split(":")
        result = int(result)
        operands = [int(operand) for operand in operands.split()]
        calibration_equations.append(CalibrationEquation(result, operands))

    return TaskInput(calibration_equations)


def _is_equasion_valid_p1(result: int, prev_result: int, operands: list[int]) -> bool:
    if operands:
        return (
            _is_equasion_valid_p1(result, prev_result *
                                  operands[0], operands[1:])
            or _is_equasion_valid_p1(result, prev_result + operands[0], operands[1:])
        )
    else:
        return result == prev_result


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    total_calibration_result = sum(
        calibration_equation.result
        for calibration_equation in task_input.calibration_equations
        if _is_equasion_valid_p1(
            calibration_equation.result,
            calibration_equation.operands[0],
            calibration_equation.operands[1:]
        )
    )

    return TaskSolution(total_calibration_result=total_calibration_result)


def _is_equasion_valid_p2(result: int, prev_result: int, operands: list[int]) -> bool:
    if operands:
        return (
            _is_equasion_valid_p2(result, prev_result *
                                  operands[0], operands[1:])
            or _is_equasion_valid_p2(result, prev_result + operands[0], operands[1:])
            or _is_equasion_valid_p2(result, int(str(prev_result) + str(operands[0])), operands[1:])
        )
    else:
        return result == prev_result


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    total_calibration_result = sum(
        calibration_equation.result
        for calibration_equation in task_input.calibration_equations
        if _is_equasion_valid_p2(
            calibration_equation.result,
            calibration_equation.operands[0],
            calibration_equation.operands[1:]
        )
    )

    return TaskSolution(total_calibration_result=total_calibration_result)

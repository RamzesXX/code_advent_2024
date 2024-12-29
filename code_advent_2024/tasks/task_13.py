"""""Task 13 solver."""
import dataclasses
import re
from code_advent_2024.tasks import task

_A_PRESS_COST = 3
_B_PRESS_COST = 1

_REGEXP_BUTTON_A = r"Button A: X\+(\d+), Y\+(\d+)"
_REGEXP_BUTTON_B = r"Button B: X\+(\d+), Y\+(\d+)"
_REGEXP_PRIZE = r"Prize: X=(\d+), Y=(\d+)"


@dataclasses.dataclass(frozen=True)
class ArcadeMachine:
    """."""
    a_dx: int
    a_dy: int
    b_dx: int
    b_dy: int
    prize_x: int
    prize_y: int


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    machines: list[ArcadeMachine]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    number_of_tokens: int = 0


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

    machines = []
    lines = input_string.split("\n")
    for line_idx in range(0, len(lines), 4):
        a_dx_str, a_dy_str = re.findall(_REGEXP_BUTTON_A, lines[line_idx])[0]
        b_dx_str, b_dy_str = re.findall(
            _REGEXP_BUTTON_B, lines[line_idx + 1])[0]
        prize_x_str, prize_y_str = re.findall(
            _REGEXP_PRIZE, lines[line_idx + 2])[0]
        machines.append(ArcadeMachine(
            a_dx=int(a_dx_str),
            a_dy=int(a_dy_str),
            b_dx=int(b_dx_str),
            b_dy=int(b_dy_str),
            prize_x=int(prize_x_str),
            prize_y=int(prize_y_str),
        ))

    return TaskInput(machines=machines)


def _solve_equation_sytem(machine: ArcadeMachine) -> tuple[int, int]:
    b = (machine.prize_x * machine.a_dy - machine.prize_y * machine.a_dx) / \
        (machine.b_dx * machine.a_dy - machine.b_dy * machine.a_dx)
    a = (machine.prize_x - b * machine.b_dx) / machine.a_dx

    return a, b


def _calc_cost(machine: ArcadeMachine) -> int:
    a, b = _solve_equation_sytem(machine)

    if (
        (a < 0 or b < 0)
        # or (a > 100 or b > 100)
        or int(a) != a
        or int(b) != b
    ):
        return 0

    a = int(a)
    b = int(b)

    return _A_PRESS_COST * a + _B_PRESS_COST * b


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    number_of_tokens = sum(
        _calc_cost(machine)
        for machine in task_input.machines
    )

    return TaskSolution(number_of_tokens=number_of_tokens)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    machines = [
        dataclasses.replace(
            machine,
            prize_x=machine.prize_x + 10000000000000,
            prize_y=machine.prize_y + 10000000000000
        )
        for machine in task_input.machines
    ]
    number_of_tokens = sum(
        _calc_cost(machine)
        for machine in machines
    )

    return TaskSolution(number_of_tokens=number_of_tokens)

"""""Task 17 solver."""
import dataclasses
import enum
import re
from code_advent_2024.tasks import task


_REGISTER_A_REGEXP = r"Register A: (\d+)"
_REGISTER_B_REGEXP = r"Register B: (\d+)"
_REGISTER_C_REGEXP = r"Register C: (\d+)"
_PROGRAM_REGEXP = r"Program: (.*)"


class Istructions(enum.IntEnum):
    """Instructions opcodes."""
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    register_a: int = 0
    register_b: int = 0
    register_c: int = 0
    program: tuple[int] = ()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    register_a: int = 0
    register_b: int = 0
    register_c: int = 0
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
    register_a = 0
    register_b = 0
    register_c = 0
    program = []
    for line in input_string.split("\n"):
        if re.match(_REGISTER_A_REGEXP, line):
            register_a = int(re.findall(_REGISTER_A_REGEXP, line)[0])
        elif re.match(_REGISTER_B_REGEXP, line):
            register_b = int(re.findall(_REGISTER_B_REGEXP, line)[0])
        elif re.match(_REGISTER_C_REGEXP, line):
            register_c = int(re.findall(_REGISTER_C_REGEXP, line)[0])
        elif re.match(_PROGRAM_REGEXP, line):
            program = tuple(
                [
                    int(x) for x in re.findall(_PROGRAM_REGEXP, line)[0].split(",")
                ]
            )

    return TaskInput(
        program=program,
        register_a=register_a,
        register_b=register_b,
        register_c=register_c,
    )


class Computer:
    """Computer."""

    def __init__(self, register_a: int, register_b: int, register_c: int, program: list[int]):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program
        self.output = []
        self.ip = 0

    def run(self):
        """Runs program."""
        self.ip = 0
        self.output = []
        while self.ip < len(self.program):
            instruction = Istructions(self.program[self.ip])
            operand = self.program[self.ip + 1]

            self.ip += 2
            if instruction == Istructions.ADV:
                combo_operand_value = self._get_value_for_combo_operand(
                    operand)
                self.register_a //= 2**combo_operand_value
            elif instruction == Istructions.BXL:
                self.register_b ^= operand
            elif instruction == Istructions.BST:
                combo_operand_value = self._get_value_for_combo_operand(
                    operand)
                self.register_b = combo_operand_value % 8
            elif instruction == Istructions.JNZ:
                if self.register_a:
                    self.ip = operand
            elif instruction == Istructions.BXC:
                self.register_b ^= self.register_c
            elif instruction == Istructions.OUT:
                combo_operand_value = self._get_value_for_combo_operand(
                    operand)
                self.output.append(combo_operand_value % 8)
            elif instruction == Istructions.BDV:
                combo_operand_value = self._get_value_for_combo_operand(
                    operand)
                self.register_b = self.register_a // 2**combo_operand_value
            elif instruction == Istructions.CDV:
                combo_operand_value = self._get_value_for_combo_operand(
                    operand)
                self.register_c = self.register_a // 2**combo_operand_value
            else:
                raise ValueError("Invalid instruction")

    def get_output(self) -> str:
        """Returns output."""
        return ",".join([str(x) for x in self.output])

    def _get_value_for_combo_operand(self, operand: int) -> int:
        if 0 <= operand < 4:
            return operand
        if operand == 4:
            return self.register_a
        if operand == 5:
            return self.register_b
        if operand == 6:
            return self.register_c

        raise ValueError("Invalid operand")


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    computer = Computer(
        register_a=task_input.register_a,
        register_b=task_input.register_b,
        register_c=task_input.register_c,
        program=task_input.program,
    )
    computer.run()

    return TaskSolution(
        register_a=computer.register_a,
        register_b=computer.register_b,
        register_c=computer.register_c,
        program_output=computer.get_output(),
    )


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution()

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


_INSTRUCTION_USING_COMBO = (
    Istructions.ADV,
    Istructions.BST,
    Istructions.OUT,
    Istructions.BDV,
    Istructions.CDV,
)


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


@dataclasses.dataclass(frozen=True)
class AregOut:
    """Combination input-output values."""
    a: int
    out: int


@dataclasses.dataclass(frozen=True)
class AregShiftOutCreg:
    """Combination input-output values."""
    a: int
    shift: int
    out: int
    c: int


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


def _get_value_for_combo_operand(
    operand: int,
    register_a: int = 0,
    register_b: int = 0,
    register_c: int = 0
) -> int:
    if 0 <= operand < 4:
        return operand
    if operand == 4:
        return register_a
    if operand == 5:
        return register_b
    if operand == 6:
        return register_c

    raise ValueError("Invalid operand")


def _run(
    program: tuple[int, ...],
    register_a: int = 0,
    register_b: int = 0,
    register_c: int = 0
) -> tuple[list[int], int, int, int]:
    """Runs program."""
    ip = 0
    output = []
    while ip < len(program):
        instruction = Istructions(program[ip])
        operand = program[ip + 1]
        if instruction in _INSTRUCTION_USING_COMBO:
            operand_value = _get_value_for_combo_operand(
                operand=operand,
                register_a=register_a,
                register_b=register_b,
                register_c=register_c
            )
        else:
            operand_value = operand

        ip += 2
        if instruction == Istructions.ADV:
            register_a //= 2**operand_value
        elif instruction == Istructions.BXL:
            register_b ^= operand_value
        elif instruction == Istructions.BST:
            register_b = operand_value % 8
        elif instruction == Istructions.JNZ:
            if register_a:
                ip = operand_value
        elif instruction == Istructions.BXC:
            register_b ^= register_c
        elif instruction == Istructions.OUT:
            output.append(operand_value % 8)
        elif instruction == Istructions.BDV:
            register_b = register_a // 2**operand_value
        elif instruction == Istructions.CDV:
            register_c = register_a // 2**operand_value
        else:
            raise ValueError("Invalid instruction")

    return output, register_a, register_b, register_c


class Computer:
    """Computer."""

    def __init__(
        self,
        program: tuple[int, ...],
        register_a: int = 0,
        register_b: int = 0,
        register_c: int = 0
    ):
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c
        self.program = program
        self.output = []
        self.register_a_bits = None

    def run(self):
        """Runs program."""
        self.output, self.register_a, self.register_b, self.register_c = _run(
            program=self.program,
            register_a=self.register_a,
            register_b=self.register_b,
            register_c=self.register_c
        )

    def get_output(self) -> str:
        """Returns output."""
        return ",".join([str(x) for x in self.output])

    def find_correct_register_a(self) -> int:
        """Find a value which leads to output equal program.

        The program looks like:
            0   b = a % 8
            1   b = b ^ 1
            2   c = a // 2**b
            3   b = b ^ 5
            4   b = b ^ c
            5   OUT b % 8
            6   a = a // 2**3
            7   JNZ 0
        """
        number_of_digits = len(self.program)
        digit_values = [0 for _ in range(number_of_digits)]
        prev_values = [0 for _ in range(number_of_digits)]
        digit_index = 0
        while digit_index < number_of_digits:
            prev_value = prev_values[digit_index]
            matched = False
            for a in range(digit_values[digit_index], 8):
                digit_values[digit_index] = a + 1
                register_a = prev_value * 8 + a
                output, _, _, _ = _run(
                    program=self.program,
                    register_a=register_a,
                )
                program_tail = list(self.program[-digit_index - 1:])
                if output == program_tail:
                    matched = True
                    digit_index += 1
                    if digit_index < number_of_digits:
                        prev_values[digit_index] = register_a
                    else:
                        return register_a
                    break
            if not matched:
                digit_values[digit_index] = 0
                prev_values[digit_index] = 0
                if digit_index == 0:
                    raise ValueError("No solution found")
                digit_index -= 1

        return 0


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
    computer = Computer(
        register_a=task_input.register_a,
        register_b=task_input.register_b,
        register_c=task_input.register_c,
        program=task_input.program,
    )
    register_a = computer.find_correct_register_a()
    computer = Computer(
        register_a=register_a,
        register_b=0,
        register_c=0,
        program=task_input.program,
    )
    computer.run()

    return TaskSolution(
        register_a=register_a,
        program_output=computer.get_output()
    )

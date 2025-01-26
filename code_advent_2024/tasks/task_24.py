"""""Task 24 solver."""
import dataclasses
import enum
import re
from code_advent_2024.tasks import task

_GATE_REGXP = r"(?P<input_1>\w+)\s+(?P<gate_type>AND|OR|XOR)\s+(?P<input_2>\w+)\s+->\s+(?P<output>\w+)"
_WIRE_INIT_STATE_REGXP = r"(?P<wire_name>\w+): (?P<init_value>\d)"


class GateType(enum.Enum):
    """Represents gate type."""
    AND = 0
    OR = 1
    XOR = 2


@dataclasses.dataclass(frozen=True)
class WireValue:
    """Represents wire value."""
    name: str = ""
    value: int = 0


@dataclasses.dataclass(frozen=True)
class Gate:
    """Represents gate type."""
    input_1: str = ""
    input_2: str = ""
    output: str = ""
    gate_type: GateType = None


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    init_wire_values: tuple[WireValue] = ()
    gates: tuple[Gate, ...] = ()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    z_wires_output: int


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
    init_wire_values = []
    gates = []
    is_in_init_section = True
    for line in input_string.split("\n"):
        if not line:
            is_in_init_section = False
            continue
        if is_in_init_section:
            match = re.search(_WIRE_INIT_STATE_REGXP, line).groupdict()
            init_wire_values.append(
                WireValue(name=match["wire_name"],
                          value=int(match["init_value"]))
            )
        else:
            match = re.search(_GATE_REGXP, line).groupdict()
            gates.append(
                Gate(
                    input_1=match["input_1"],
                    input_2=match["input_2"],
                    output=match["output"],
                    gate_type=GateType[match["gate_type"]]
                )
            )

    return TaskInput(
        init_wire_values=init_wire_values,
        gates=gates
    )


def _calc_gate_value(gate: Gate, wire_to_value: dict[str, int]) -> dict[str, int]:
    input_1_value = wire_to_value[gate.input_1]
    input_2_value = wire_to_value[gate.input_2]
    output_value = None
    if gate.gate_type == GateType.AND:
        output_value = input_1_value & input_2_value
    elif gate.gate_type == GateType.OR:
        output_value = input_1_value | input_2_value
    elif gate.gate_type == GateType.XOR:
        output_value = input_1_value ^ input_2_value
    wire_to_value[gate.output] = output_value

    return wire_to_value


def _calc_all_values(
    wires_to_calc: list[str],
    output_to_gate: dict[str, Gate],
    wire_to_value: dict[str, int]
) -> dict[str, int]:
    wires_to_process = []
    wires_to_process_queue = list(wires_to_calc)

    while wires_to_process_queue:
        wire_to_process = wires_to_process_queue.pop(0)
        wires_to_process.append(wire_to_process)
        if wire_to_process in output_to_gate:
            gate = output_to_gate[wire_to_process]
            wires_to_process_queue.append(gate.input_1)
            wires_to_process_queue.append(gate.input_2)
    wires_to_process.reverse()

    for wire in wires_to_process:
        if wire not in wire_to_value:
            gate = output_to_gate[wire]
            wire_to_value = _calc_gate_value(gate, wire_to_value)

    return wire_to_value


def _build_z_number(wire_to_value: dict[str, int]) -> int:
    z_number = 0
    z_wires = [
        wire_name
        for wire_name in wire_to_value
        if wire_name.startswith("z")
    ]
    z_wires.sort(reverse=True)
    for z_wire in z_wires:
        z_number = z_number * 2 + wire_to_value[z_wire]

    return z_number


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    output_to_gate = {}
    wire_to_value = {}
    for gate in task_input.gates:
        output_to_gate[gate.output] = gate
    for wire in task_input.init_wire_values:
        wire_to_value[wire.name] = wire.value
    z_wires = [
        wire_name
        for wire_name in output_to_gate
        if wire_name.startswith("z")
    ]

    wire_to_value = _calc_all_values(
        z_wires, output_to_gate, wire_to_value
    )
    z_wires_output = _build_z_number(wire_to_value)

    return TaskSolution(z_wires_output=z_wires_output)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    return TaskSolution(z_wires_output=0)

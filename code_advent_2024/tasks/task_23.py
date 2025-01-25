"""""Task 23 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class Connection:
    """Represents connection."""
    first_pc: str = ""
    second_pc: str = ""


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    connections: tuple[Connection] = ()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    number_of_three_interconnected_pcs: int = 0
    password: str = ""


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
    connections = []
    for line in input_string.split():
        pc_1, pc_2 = line.split("-")
        connections.append(Connection(pc_1, pc_2))

    return TaskInput(connections=connections)


def _build_connection_graph(connections: list[Connection]) -> dict[str, set[str]]:
    """Build connection graph.

    Args:
        connections: List of connections.

    Returns:
        Connection graph in form of a dict where key is a pc
          and value is a set of connected pcs.
    """
    connection_graph = {}
    for connection in connections:
        connection_graph.setdefault(
            connection.first_pc, set()).add(connection.second_pc)
        connection_graph.setdefault(
            connection.second_pc, set()).add(connection.first_pc)

    return connection_graph


def _calc_number_of_three_connecting_pcs(
    connection_graph: dict[str, set[str]]
) -> int:
    """Find three connecting pcs."""
    three_interconnected_pcs = set()
    started_with_t_pcs = [
        pc_name
        for pc_name in connection_graph
        if pc_name.startswith("t")
    ]
    for first_pc in started_with_t_pcs:
        for second_pc in connection_graph[first_pc]:
            common_connections = connection_graph[first_pc] & connection_graph[second_pc]
            for third_pc in common_connections:
                three_interconnected_pcs.add(
                    tuple(sorted([first_pc, second_pc, third_pc]))
                )

    return len(three_interconnected_pcs)


def _calc_password(
    connection_graph: dict[str, set[str]]
) -> str:
    pass


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    connection_graph = _build_connection_graph(task_input.connections)
    number_of_three_interconnected_pcs = _calc_number_of_three_connecting_pcs(
        connection_graph=connection_graph
    )

    return TaskSolution(number_of_three_interconnected_pcs=number_of_three_interconnected_pcs)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    connection_graph = _build_connection_graph(task_input.connections)
    password = _calc_password(connection_graph)
    return TaskSolution(password=password)

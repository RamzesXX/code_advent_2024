"""""Task 21 solver.
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Position in the map."""
    row: int = 0
    col: int = 0


_NUMBER_PAD_BUTTON_COORDINATES = {
    "7": Coordinates(0, 0),
    "8": Coordinates(0, 1),
    "9": Coordinates(0, 2),
    "4": Coordinates(1, 0),
    "5": Coordinates(1, 1),
    "6": Coordinates(1, 2),
    "1": Coordinates(2, 0),
    "2": Coordinates(2, 1),
    "3": Coordinates(2, 2),
    "0": Coordinates(3, 1),
    "A": Coordinates(3, 2),
}

_ARROW_PAD_BUTTON_COORDINATES = {
    "^": Coordinates(0, 1),
    "A": Coordinates(0, 2),
    "<": Coordinates(1, 0),
    "v": Coordinates(1, 1),
    ">": Coordinates(1, 2),
}


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    codes: tuple[str, ...] = ()


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    sum_of_complexities: int = 0


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
    codes = []
    for line in input_string.split("\n"):
        codes.append(line)

    return TaskInput(codes=tuple(codes))


def _calc_sequence_complexity(code: str, sequence: list[str]) -> int:
    return len(sequence) * int(code[:-1])


def _get_available_paths(
    from_postion: Coordinates,
    to_position: Coordinates,
    prohibited_position: Coordinates
) -> set[str]:
    available_paths = set()
    d_row = to_position.row - from_postion.row
    d_col = to_position.col - from_postion.col
    hor_arrow_char = ">" if d_col > 0 else "<"
    vert_arrow_char = "v" if d_row > 0 else "^"

    if d_row == 0 or d_col == 0:
        path = hor_arrow_char * abs(d_col) + vert_arrow_char * abs(d_row)
        available_paths.add(path)

    elif (
        (
            to_position.col == prohibited_position.col
            and from_postion.row == prohibited_position.row
        )
        or (
            to_position.row == prohibited_position.row
            and from_postion.col == prohibited_position.col
        )
    ):
        if from_postion.col == prohibited_position.col:
            path = hor_arrow_char * abs(d_col) + vert_arrow_char * abs(d_row)
            available_paths.add(path)
        else:
            path = vert_arrow_char * abs(d_row) + hor_arrow_char * abs(d_col)
            available_paths.add(path)
    else:
        path = hor_arrow_char * abs(d_col) + vert_arrow_char * abs(d_row)
        available_paths.add(path)
        path = vert_arrow_char * abs(d_row) + hor_arrow_char * abs(d_col)
        available_paths.add(path)

    return available_paths


def _get_only_shortest_paths(paths: set[str]) -> set[str]:
    sorted_paths = sorted(paths, key=len)
    shortest_path_len = len(sorted_paths[0])
    paths = set(filter(lambda path: len(path) == shortest_path_len, paths))

    return paths


def _build_shortest_path(
    code: str,
    pad_button_coordinates: dict[str, Coordinates],
    prohibited_position: Coordinates
) -> set[str]:
    prev_letter = "A"
    prev_position = pad_button_coordinates[prev_letter]
    paths = {""}
    for letter in code:
        new_position = pad_button_coordinates[letter]
        available_paths = _get_available_paths(
            prev_position,
            new_position,
            prohibited_position
        )
        paths = {
            path + available_path + "A"
            for path in paths
            for available_path in available_paths
        }
        prev_letter, prev_position = letter, new_position

    return _get_only_shortest_paths(paths)


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    sum_of_complexities = 0
    for code in task_input.codes:
        shortest_paths_arr = _build_shortest_path(
            code=code,
            pad_button_coordinates=_NUMBER_PAD_BUTTON_COORDINATES,
            prohibited_position=Coordinates(3, 0)
        )
        for _ in range(2):
            shortest_paths_arr_tmp = set()
            for shortest_path in shortest_paths_arr:
                shortest_paths = _build_shortest_path(
                    code=shortest_path,
                    pad_button_coordinates=_ARROW_PAD_BUTTON_COORDINATES,
                    prohibited_position=Coordinates(0, 0)
                )
                shortest_paths_arr_tmp.update(shortest_paths)
            shortest_paths_arr = _get_only_shortest_paths(
                shortest_paths_arr_tmp)

        shortest_paths = _get_only_shortest_paths(shortest_paths_arr)

        sum_of_complexities += _calc_sequence_complexity(
            code, shortest_paths.pop()
        )

    return TaskSolution(sum_of_complexities=sum_of_complexities)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    sum_of_complexities = 0
    for code in task_input.codes:
        shortest_paths_arr = _build_shortest_path(
            code=code,
            pad_button_coordinates=_NUMBER_PAD_BUTTON_COORDINATES,
            prohibited_position=Coordinates(3, 0)
        )
        for i in range(25):
            shortest_paths_arr_tmp = set()
            for shortest_path in shortest_paths_arr:
                shortest_paths = _build_shortest_path(
                    code=shortest_path,
                    pad_button_coordinates=_ARROW_PAD_BUTTON_COORDINATES,
                    prohibited_position=Coordinates(0, 0)
                )
                shortest_paths_arr_tmp.update(shortest_paths)
            shortest_paths_arr = _get_only_shortest_paths(
                shortest_paths_arr_tmp)

        shortest_paths = _get_only_shortest_paths(shortest_paths_arr)

        sum_of_complexities += _calc_sequence_complexity(
            code, shortest_paths.pop()
        )

    return TaskSolution(sum_of_complexities=sum_of_complexities)

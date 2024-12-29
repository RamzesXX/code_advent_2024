"""""Task 12 solver."""
import dataclasses
from code_advent_2024.tasks import task

_POSITIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    garden_map: list[list[str]]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    fence_cost: int = 0


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Represents coordinates on a map."""
    row: int
    col: int


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

    garden_map = []

    for line in input_string.split("\n"):
        garden_map.append([x for x in line])

    return TaskInput(garden_map=garden_map)


def _split_into_figures(
        garden_map: list[list[str]]
) -> dict[int, set[Coordinates]]:
    print("\nProgress:")
    width = len(garden_map[0])
    total_area = len(garden_map) * width

    next_figure_id = 0
    figure_coords: dict[int, set[Coordinates]] = {}
    coords_figure: dict[Coordinates, int] = {}
    for row_idx, row in enumerate(garden_map):
        for col_idx, cell in enumerate(row):
            cur_plot_coords = Coordinates(row=row_idx, col=col_idx)
            cur_plot_id = None
            # edge plots
            if (
                (row_idx == 0 or garden_map[row_idx - 1][col_idx] != cell)
                and (col_idx == 0 or garden_map[row_idx][col_idx - 1] != cell)
            ):
                figure_coords.setdefault(
                    next_figure_id, set()).add(cur_plot_coords)
                coords_figure[Coordinates(
                    row=row_idx, col=col_idx)] = next_figure_id
                next_figure_id += 1
                continue

            # plot with same id is above

            if (row_idx != 0 and garden_map[row_idx - 1][col_idx] == cell):
                adjacent_figure_coords = Coordinates(row_idx - 1, col_idx)
                adjacent_figure_id = coords_figure[adjacent_figure_coords]

                cur_plot_id = adjacent_figure_id
                figure_coords[cur_plot_id].add(cur_plot_coords)
                coords_figure[cur_plot_coords] = cur_plot_id

            # plot with same id is left
            if (col_idx != 0 and garden_map[row_idx][col_idx - 1] == cell):
                adjacent_figure_coords = Coordinates(row_idx, col_idx - 1)
                adjacent_figure_id = coords_figure[adjacent_figure_coords]

                if cur_plot_id is None:
                    cur_plot_id = adjacent_figure_id
                    coords_figure[cur_plot_coords] = cur_plot_id
                    figure_coords[cur_plot_id].add(cur_plot_coords)
                elif cur_plot_id != adjacent_figure_id:
                    from_id = max(cur_plot_id, adjacent_figure_id)
                    to_id = min(cur_plot_id, adjacent_figure_id)
                    for plot_coords in figure_coords[from_id]:
                        figure_coords[to_id].add(plot_coords)
                        coords_figure[plot_coords] = to_id
                    del figure_coords[from_id]

            processed_area = row_idx * width + col_idx
            task.show_progress(total=total_area, current=processed_area)
    print()

    return figure_coords


def _calc_perimeter_for_plot(plot_coords: Coordinates, figure_coords: set[Coordinates]) -> int:
    """Calcs a single plot's perimeter.

    For each square plot belonging to a figure we count number of sides not having a neighbour
    """
    perimeter = 0
    for position in _POSITIONS:
        neighbour_coords = Coordinates(
            row=plot_coords.row + position[0],
            col=plot_coords.col + position[1]
        )
        if neighbour_coords not in figure_coords:
            perimeter += 1

    return perimeter


def _calc_fence_cost_by_perimeter(figure_coords: set[Coordinates]) -> int:
    perimeter = sum(
        _calc_perimeter_for_plot(coords, figure_coords)
        for coords in figure_coords
    )
    area = len(figure_coords)

    return perimeter * area


def _calc_side_numbers_for_figure(figure_coords: set[Coordinates]) -> int:
    """Calcs a figure's sides number.

    For each row and column we count number of "external"(not havinf=g a neighbour) sides.
    if prev line had the same sides they are not taken into account as they just prolong
    existing sides.
    """
    sides = 0

    ordered_by_row_col_coords = sorted(
        figure_coords, key=lambda x: (x.row, x.col))
    prev_crossings = set()
    crossings = set()
    cur_row = ordered_by_row_col_coords[0].row
    for plot_coords in ordered_by_row_col_coords:
        if cur_row != plot_coords.row:
            cur_row = plot_coords.row
            prev_crossings = crossings
            crossings = set()
        left = Coordinates(row=plot_coords.row, col=plot_coords.col - 1)
        if left not in figure_coords:
            cur_crossing = (-1, plot_coords.col)
            crossings.add(cur_crossing)
            if cur_crossing not in prev_crossings:
                sides += 1
        right = Coordinates(row=plot_coords.row, col=plot_coords.col + 1)
        if right not in figure_coords:
            cur_crossing = (1, plot_coords.col)
            crossings.add(cur_crossing)
            if cur_crossing not in prev_crossings:
                sides += 1

    ordered_by_col_row_coords = sorted(
        figure_coords, key=lambda x: (x.col, x.row))
    prev_crossings = set()
    crossings = set()
    cur_col = ordered_by_col_row_coords[0].col
    for plot_coords in ordered_by_col_row_coords:
        if cur_col != plot_coords.col:
            cur_col = plot_coords.col
            prev_crossings = crossings
            crossings = set()
        up = Coordinates(row=plot_coords.row - 1, col=plot_coords.col)
        if up not in figure_coords:
            cur_crossing = (-1, plot_coords.row)
            crossings.add(cur_crossing)
            if cur_crossing not in prev_crossings:
                sides += 1
        down = Coordinates(row=plot_coords.row+1, col=plot_coords.col)
        if down not in figure_coords:
            cur_crossing = (1, plot_coords.row)
            crossings.add(cur_crossing)
            if cur_crossing not in prev_crossings:
                sides += 1

    return sides


def _calc_fence_cost_by_side_number(figure_coords: set[Coordinates]) -> int:
    sides = _calc_side_numbers_for_figure(figure_coords)
    area = len(figure_coords)

    return sides * area


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    figure_coords = _split_into_figures(task_input.garden_map)
    fence_cost = sum(
        _calc_fence_cost_by_perimeter(coords)
        for coords in figure_coords.values()
    )

    return TaskSolution(fence_cost=fence_cost)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    figure_coords = _split_into_figures(task_input.garden_map)
    fence_cost = sum(
        _calc_fence_cost_by_side_number(coords)
        for coords in figure_coords.values()
    )

    return TaskSolution(fence_cost=fence_cost)

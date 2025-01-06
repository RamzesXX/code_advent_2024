"""""Task 16 solver."""
import dataclasses
import enum
from code_advent_2024.tasks import task


_WALL_CHAR = "#"
_START_POSITION_CHAR = "S"
_END_POSITION_CHAR = "E"


@dataclasses.dataclass(frozen=True)
class Position:
    """Position in the map."""
    row: int = 0
    col: int = 0


@dataclasses.dataclass(frozen=True)
class PositionDeltas:
    """."""
    d_row: int = 0
    d_col: int = 0


class Direction(enum.Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


_DIRECTION_DELTAS = {
    Direction.NORTH: PositionDeltas(-1, 0),
    Direction.SOUTH: PositionDeltas(1, 0),
    Direction.WEST: PositionDeltas(0, -1),
    Direction.EAST: PositionDeltas(0, 1),
}


@dataclasses.dataclass(frozen=True)
class Reindeer:
    """."""
    position: Position
    direction: Direction


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    maze_map: dict[Position, str]
    start_position: Position
    end_position: Position
    reindeer: Reindeer


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    score: int = 0


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

    zoom_map = {}
    start_postion = None
    end_postion = None
    for row_idx,  line in enumerate(input_string.split("\n")):
        for col_idx, char in enumerate(line):
            if char == _WALL_CHAR:
                zoom_map[Position(row=row_idx, col=col_idx)] = _WALL_CHAR
            elif char == _START_POSITION_CHAR:
                start_postion = Position(row=row_idx, col=col_idx)
                reindeer = Reindeer(
                    position=start_postion,
                    direction=Direction.EAST
                )
            elif char == _END_POSITION_CHAR:
                end_postion = Position(row=row_idx, col=col_idx)

    return TaskInput(
        maze_map=zoom_map,
        start_position=start_postion,
        reindeer=reindeer,
        end_position=end_postion
    )


def _adjacent_positions(position: Position) -> tuple[Position, ...]:
    """Calculate GPS coordinate."""
    return {
        Position(
            row=position.row + direction_delta.d_row,
            col=position.col + direction_delta.d_col
        )
        for direction_delta in _DIRECTION_DELTAS
    }


class Traverer:
    """Maze traverser."""

    def __init__(self, maze_map: dict[Position, str], reindeer: Reindeer, end_position: Position):
        self.maze_map = maze_map
        self.reindeer = reindeer
        self.end_position = end_position
        self.visited_position = {
            reindeer.position: 0
        }

    def traverse(self):
        self.visited_position = {
            self.reindeer.position: 0
        }
        self._traverse(self.reindeer, 0)

    def get_score(self, position: Position) -> int | None:
        return self.visited_position.get(position, None)

    def _traverse(self,  reindeer: Reindeer, current_score: int):
        if reindeer.position == self.end_position:
            return
        if


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    maze_traverser = Traverer(
        maze_map=task_input.maze_map,
        reindeer=task_input.reindeer,
        end_position=task_input.end_position
    )
    maze_traverser.traverse()

    return TaskSolution(score=maze_traverser.get_score(task_input.end_position))


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    maze_traverser = Traverer(
        maze_map=task_input.maze_map,
        reindeer=task_input.reindeer,
        end_position=task_input.end_position
    )
    maze_traverser.traverse()

    return TaskSolution(score=maze_traverser.get_score(task_input.end_position))

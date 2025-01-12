"""""Task 16 solver."""
import dataclasses
import enum
from code_advent_2024.tasks import task


_WALL_CHAR = "#"
_START_POSITION_CHAR = "S"
_END_POSITION_CHAR = "E"
_VISITED_POSITION_CHAR = "O"

_STEP_COST = 1
_TURN_COST = 1000


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


class Direction(enum.IntEnum):
    """Directions."""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


_DIRECTION_DELTAS = {
    Direction.NORTH: PositionDeltas(-1, 0),
    Direction.SOUTH: PositionDeltas(1, 0),
    Direction.WEST: PositionDeltas(0, -1),
    Direction.EAST: PositionDeltas(0, 1),
}


@dataclasses.dataclass(frozen=True)
class DirectedPosition:
    """Reindeer position and direction."""
    position: Position
    direction: Direction


@dataclasses.dataclass(frozen=True)
class VisitingDetails:
    """."""
    score: int = None
    came_from: tuple[DirectedPosition, ...] = ()


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    maze_map: dict[Position, str]
    start_position: Position
    end_position: Position
    reindeer: DirectedPosition


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    score: int = 0
    best_path_tiles_number: int = 0


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

    maze_map = {}
    start_postion = None
    end_postion = None
    reindeer = None
    for row_idx,  line in enumerate(input_string.split("\n")):
        for col_idx, char in enumerate(line):
            if char == _WALL_CHAR:
                maze_map[Position(row=row_idx, col=col_idx)] = _WALL_CHAR
            elif char == _START_POSITION_CHAR:
                start_postion = Position(row=row_idx, col=col_idx)
                reindeer = DirectedPosition(
                    position=start_postion,
                    direction=Direction.EAST
                )
            elif char == _END_POSITION_CHAR:
                end_postion = Position(row=row_idx, col=col_idx)

    return TaskInput(
        maze_map=maze_map,
        start_position=start_postion,
        reindeer=reindeer,
        end_position=end_postion
    )


class MazeTraverser:
    """Maze traverser."""

    def __init__(
        self,
        maze_map: dict[Position, str],
        reindeer: DirectedPosition,
        end_position: Position
    ):
        self.maze_map = maze_map
        self.reindeer = reindeer
        self.end_position = end_position
        self.visited_positions = {}

    def traverse(self):
        """Traverse the maze."""
        positions_to_visit = [(self.reindeer, None, 0)]
        while positions_to_visit:
            reindeer, prev_position, current_score = positions_to_visit.pop(0)

            if not self._update_visiting_details(
                    reindeer,
                    prev_position,
                    current_score
            ):
                continue

            if reindeer.position == self.end_position:
                continue

            turned_left_reindeer = self._turn_reindeer(reindeer, -1)
            turned_right_reindeer = self._turn_reindeer(reindeer, +1)
            score_after_turning = current_score + _TURN_COST
            positions_to_visit.append(
                (turned_left_reindeer, reindeer, score_after_turning)
            )
            positions_to_visit.append(
                (turned_right_reindeer, reindeer, score_after_turning)
            )

            reindeer_after_move = self._move_reindeer(reindeer)
            score_after_moving = current_score + _STEP_COST

            if self.maze_map.get(reindeer_after_move.position, None) == _WALL_CHAR:
                continue

            positions_to_visit.append(
                (reindeer_after_move, reindeer, score_after_moving)
            )

    def get_score(self) -> int:
        """Gets position's score."""
        best_directed_positions = self._get_best_score_directed_positions(
            self.end_position)
        if not best_directed_positions:
            return -1

        visit_info = self.visited_positions.get(best_directed_positions[0])

        return visit_info.score

    def get_number_of_tiles_belonging_to_the_best_path(self) -> int:
        """Gets number of tiles belonging to the best path."""
        tiles = set()
        positions_to_process = self._get_best_score_directed_positions(
            self.end_position
        )
        while positions_to_process:
            cur_position = positions_to_process.pop(0)

            tiles.add(cur_position.position)
            visiting_details: VisitingDetails = self.visited_positions.get(
                cur_position
            )
            # print("\n\n")
            # print(self.visualize_maze({
            #     _VISITED_POSITION_CHAR: tiles
            # }))
            positions_to_process.extend(set(visiting_details.came_from))

        return len(tiles)

    def visualize_maze(self, elements: dict[str, set[Position]]) -> str:
        """Visualize maze.

        Args:
          elements: Character to position mapping.

        Returns:
          Maze picture string.
        """
        maze_tiles = self.maze_map.copy()

        for character, positions in elements.items():
            for position in positions:
                # check for overlapping
                maze_tiles[position] = character

        sorted_maze_tile_coords = sorted(
            maze_tiles,
            key=lambda position_: (position_.row, position_.col)
        )
        picture = []
        prev_position = Position(row=0, col=0)
        line = "000 "
        for cur_position in sorted_maze_tile_coords:
            dy = cur_position.row - prev_position.row
            if dy > 0:
                picture.append(line)
                picture.extend([""] * (dy - 1))
                line = f"{cur_position.row:03} "
                prev_position = Position(row=cur_position.row, col=0)
            dx = cur_position.col - prev_position.col
            line += "." * (dx - 1) + maze_tiles[cur_position]
            prev_position = cur_position
        picture.append(line)

        return "\n".join(picture)

    def _update_visiting_details(
        self,
        cur_position: DirectedPosition,
        prev_position: DirectedPosition,
        current_score: int
    ) -> bool:
        existing_visiting_details = self.visited_positions.get(
            cur_position, None)
        if (
            cur_position not in self.visited_positions
            or existing_visiting_details.score > current_score
        ):
            came_from = (prev_position,) if prev_position else ()
            visiting_details = VisitingDetails(
                score=current_score,
                came_from=came_from
            )
            self.visited_positions[cur_position] = visiting_details

            return True

        if existing_visiting_details.score == current_score:
            came_from = (
                *existing_visiting_details.came_from,
                prev_position
            )
            visiting_details = dataclasses.replace(
                existing_visiting_details,
                came_from=came_from
            )
            self.visited_positions[cur_position] = visiting_details

        return False

    def _turn_reindeer(
        self,
        reindeer: DirectedPosition,
        direction_delta: Direction
    ) -> DirectedPosition:
        new_direction = Direction(
            (reindeer.direction + direction_delta) % len(Direction)
        )
        return dataclasses.replace(reindeer, direction=new_direction)

    def _move_reindeer(
        self,
        reindeer: DirectedPosition
    ) -> DirectedPosition:
        direction_deltas = _DIRECTION_DELTAS[reindeer.direction]
        new_position = Position(
            row=reindeer.position.row + direction_deltas.d_row,
            col=reindeer.position.col + direction_deltas.d_col
        )

        return dataclasses.replace(reindeer, position=new_position)

    def _get_best_score_directed_positions(self, position: Position) -> list[DirectedPosition]:
        """Gets position's score."""
        best_directed_positions = []
        best_score = None
        for direction in Direction:
            directed_position = DirectedPosition(
                position=position,
                direction=direction
            )
            visit_info = self.visited_positions.get(directed_position, None)
            if not visit_info:
                continue
            if best_score is None or visit_info.score < best_score:
                best_score = visit_info.score
                best_directed_positions = [directed_position]
            elif visit_info.score == best_score:
                best_directed_positions.append(directed_position)

        return best_directed_positions


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    maze_traverser = MazeTraverser(
        maze_map=task_input.maze_map,
        reindeer=task_input.reindeer,
        end_position=task_input.end_position
    )
    maze_traverser.traverse()

    return TaskSolution(score=maze_traverser.get_score())


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    maze_traverser = MazeTraverser(
        maze_map=task_input.maze_map,
        reindeer=task_input.reindeer,
        end_position=task_input.end_position
    )
    maze_traverser.traverse()

    return TaskSolution(
        best_path_tiles_number=maze_traverser.get_number_of_tiles_belonging_to_the_best_path()
    )

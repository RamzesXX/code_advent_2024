"""""Task 6 solver."""
import dataclasses
from code_advent_2024.tasks import task

_DY_INDEX = 0
_DX_INDEX = 1

_DIRECTIONS = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)

_DIRECTIONS_CHARS = (
    "^",
    ">",
    "v",
    "<"
)

_OBSTACLE_CHAR = "#"


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """Represents coordinates on a map."""
    row: int
    col: int


@dataclasses.dataclass(frozen=True)
class TouchedCoordinates:
    """Represents coordinates on a map."""
    row: int
    col: int
    direction_index: int


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    room_map: list[list[str]]
    direction_index: int
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    patrolled_positions: int


class LaboratoryWalker:
    """Represents lab walker."""

    def __init__(self, task_input: TaskInput):
        self.map = task_input.room_map
        self.map_height = len(task_input.room_map)
        self.map_width = len(task_input.room_map[0])
        self.start_direction_index = task_input.direction_index
        self.start_position = Coordinates(task_input.y, task_input.x)
        self.cur_position = Coordinates(task_input.y, task_input.x)
        self.cur_direction_index = task_input.direction_index
        self.visited_positions: list[Coordinates] = []
        self.touched_obstacles: list[TouchedCoordinates] = []
        self.artifitial_obstacles: set[Coordinates] = set()
        self.beyond_map: bool = False
        self.in_loop: bool = False

    def reset(self, artifitial_obstacles: set[Coordinates]):
        """Start patrolling."""
        self.cur_position = dataclasses.replace(self.start_position)
        self.cur_direction_index = self.start_direction_index
        self.artifitial_obstacles = artifitial_obstacles
        self.visited_positions: list[Coordinates] = []
        self.touched_obstacles: list[TouchedCoordinates] = []
        self.beyond_map: bool = False
        self.in_loop: bool = False

    def is_there_obstacle(self, position: Coordinates) -> bool:
        """Check if there is an obstacle at the position."""
        return (
            self.map[position.row][position.col] == _OBSTACLE_CHAR
            or position in self.artifitial_obstacles
        )

    def do_step(self):
        """Do a step."""
        if self.beyond_map or self.in_loop:
            return
        self.visited_positions.append(self.cur_position)
        cur_derection = _DIRECTIONS[self.cur_direction_index]
        new_position = dataclasses.replace(
            self.cur_position,
            row=self.cur_position.row + cur_derection[_DY_INDEX],
            col=self.cur_position.col + cur_derection[_DX_INDEX]
        )

        if (
            new_position.row < 0 or new_position.row >= self.map_height
            or new_position.col < 0 or new_position.col >= self.map_width
        ):
            self.cur_position = new_position
            self.beyond_map = True
            return

        if self.is_there_obstacle(new_position):
            touched_coord = TouchedCoordinates(
                row=new_position.row,
                col=new_position.col,
                direction_index=self.cur_direction_index
            )

            if touched_coord in self.touched_obstacles:
                self.in_loop = True
                return

            self.touched_obstacles.append(touched_coord)
            self.cur_direction_index = (
                self.cur_direction_index + 1) % len(_DIRECTIONS)
        else:
            self.cur_position = new_position

        return


def get_input_from_file(file_name: str) -> TaskInput:
    """Read input data form a file.

    Args:
        file_name: Path to the file with input data.
    """
    with open(file_name, encoding="ascii") as f:
        file_content = f.read()

    return get_input_from_string(file_content)


def get_input_from_string(input_string: str) -> TaskInput:
    """Read input data from a string.

    Args:
        input_string: Input data as a string.
    """
    room_map = []

    for line in input_string.split("\n"):
        room_map.append([x for x in line])
    for y, row in enumerate(room_map):
        for x, char in enumerate(row):
            if char in _DIRECTIONS_CHARS:
                direction_index = _DIRECTIONS_CHARS.index(char)
                return TaskInput(room_map=room_map, x=x, y=y, direction_index=direction_index)


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    walker = LaboratoryWalker(task_input=task_input)
    while not walker.beyond_map and not walker.in_loop:
        walker.do_step()

    return TaskSolution(patrolled_positions=len(set(walker.visited_positions)))


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    walker = LaboratoryWalker(task_input=task_input)
    patrolled_positions = 0
    # TODO: We can check only points from a path instead of checking all points
    for row_index, row in enumerate(task_input.room_map):
        for col_index, char in enumerate(row):
            obstacle_coord = Coordinates(row=row_index, col=col_index)
            # Skip the existing obstacles and the start position
            if char == _OBSTACLE_CHAR or obstacle_coord == walker.start_position:
                continue

            walker.reset(artifitial_obstacles=set((obstacle_coord,)))
            while not walker.beyond_map and not walker.in_loop:
                walker.do_step()
            if walker.in_loop:
                patrolled_positions += 1

    return TaskSolution(patrolled_positions=patrolled_positions)

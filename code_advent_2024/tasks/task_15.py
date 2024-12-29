"""""Task 15 solver."""
import dataclasses
from code_advent_2024.tasks import task

_BOX_CHAR = "O"
_WALL_CHAR = "#"
_WIDE_BOX_CHAR_LEFT = "["
_WIDE_BOX_CHAR_RIGHT = "]"

_ROBOT_CHAR = "@"


@dataclasses.dataclass(frozen=True)
class CoordinateDeltas:
    """."""
    dx: int = 0
    dy: int = 0


_MOVES = {
    "^": CoordinateDeltas(0, -1),
    "v": CoordinateDeltas(0, 1),
    "<": CoordinateDeltas(-1, 0),
    ">": CoordinateDeltas(1, 0),
}


@dataclasses.dataclass(frozen=True)
class Coordinates:
    """."""
    x: int = 0
    y: int = 0

    def gps_coordinate(self):
        """Calculate GPS coordinate."""
        return self.y * 100 + self.x


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    room_map: dict[Coordinates, str]
    robot_position: Coordinates
    moves: list[CoordinateDeltas]


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    sum_of_box_coordinates: int = 0


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

    reading_map = True
    room_map = {}
    moves = []
    robot_position = None
    for y,  line in enumerate(input_string.split("\n")):
        if not line:
            reading_map = False
            continue

        if reading_map:
            for x, char in enumerate(line):
                if char in (_BOX_CHAR, _WALL_CHAR, _WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT):
                    room_map[Coordinates(x, y)] = char
                elif char == _ROBOT_CHAR:
                    robot_position = Coordinates(x, y)
        else:
            moves.extend(_MOVES[move] for move in line)

    return TaskInput(room_map=room_map, robot_position=robot_position, moves=moves)


def _move_robot_p1(position: Coordinates,
                   move: CoordinateDeltas,
                   room_map: dict[Coordinates, str],
                   ) -> tuple[Coordinates, dict[Coordinates, str]]:
    new_position = Coordinates(
        x=position.x + move.dx,
        y=position.y + move.dy
    )
    if room_map.get(new_position, None) == _WALL_CHAR:
        return position, room_map
    if room_map.get(new_position, None) == _BOX_CHAR:
        box_position = new_position
        room_map = _move_box_p1(box_position, move, room_map)
    if new_position not in room_map:
        return new_position, room_map

    return position, room_map


def _move_box_p1(position: Coordinates,
                 move: CoordinateDeltas,
                 room_map: dict[Coordinates, str]) -> dict[Coordinates, str]:
    new_position = Coordinates(
        x=position.x + move.dx,
        y=position.y + move.dy
    )
    if room_map.get(new_position, None) == _WALL_CHAR:
        return room_map

    if room_map.get(new_position, None) == _BOX_CHAR:
        room_map = _move_box_p1(new_position, move, room_map)

    if new_position not in room_map:
        del room_map[position]
        room_map[new_position] = _BOX_CHAR

    return room_map


def _move_robot_p2(position: Coordinates,
                   move: CoordinateDeltas,
                   room_map: dict[Coordinates, str],
                   ) -> tuple[Coordinates, dict[Coordinates, str]]:
    new_position = Coordinates(
        x=position.x + move.dx,
        y=position.y + move.dy
    )
    if room_map.get(new_position, None) == _WALL_CHAR:
        return position, room_map
    if room_map.get(new_position, None) in (_WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT):
        if move.dx == 1:
            box_position = new_position
        elif move.dx == -1:
            box_position = Coordinates(
                x=position.x + move.dx * 2,
                y=position.y + move.dy
            )
        elif room_map.get(new_position, None) == _WIDE_BOX_CHAR_RIGHT:
            box_position = Coordinates(
                x=position.x + move.dx - 1,
                y=position.y + move.dy
            )
        else:
            box_position = new_position
        if _can_move_box_p2(box_position, move, room_map):
            room_map = _move_box_p2(box_position, move, room_map)
    if new_position not in room_map:
        return new_position, room_map

    return position, room_map


def _get_boxes_to_move_p2(move, room_map, position_left, new_position_left, new_position_right):
    boxes_to_move = []
    if move.dx:
        boxes_to_move = [
            Coordinates(
                x=position_left.x + move.dx * 2,
                y=position_left.y + move.dy
            )
        ]
    else:
        if room_map.get(new_position_left, None) == _WIDE_BOX_CHAR_LEFT:
            boxes_to_move.append(new_position_left)
        else:
            if room_map.get(new_position_left, None) == _WIDE_BOX_CHAR_RIGHT:
                boxes_to_move.append(
                    Coordinates(
                        x=new_position_left.x - 1,
                        y=new_position_left.y
                    )
                )
            if room_map.get(new_position_right, None) == _WIDE_BOX_CHAR_LEFT:
                boxes_to_move.append(new_position_right)
    return boxes_to_move


def _can_move_box_p2(position: Coordinates,
                     move: CoordinateDeltas,
                     room_map: dict[Coordinates, str]
                     ) -> bool:
    position_left = position
    position_right = Coordinates(
        x=position.x + 1,
        y=position.y
    )
    new_position_left = Coordinates(
        x=position_left.x + move.dx,
        y=position_left.y + move.dy
    )
    new_position_right = Coordinates(
        x=position_right.x + move.dx,
        y=position_right.y + move.dy
    )
    if (
        room_map.get(new_position_left, None) == _WALL_CHAR
        or room_map.get(new_position_right, None) == _WALL_CHAR
    ):
        return False

    if (
        (move.dy and new_position_left not in room_map and new_position_right not in room_map)
        or (move.dx == -1 and new_position_left not in room_map)
        or (move.dx == 1 and new_position_right not in room_map)
    ):
        return True

    if (
        (move.dy and
            room_map.get(new_position_left, None) in (
                _WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT)
            or room_map.get(new_position_right, None) in (_WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT)
         )
        or (move.dx == -1 and room_map.get(new_position_left, None) == _WIDE_BOX_CHAR_RIGHT)
        or (move.dx == 1 and room_map.get(new_position_right, None) == _WIDE_BOX_CHAR_LEFT)
    ):
        boxes_to_move = _get_boxes_to_move_p2(
            move,
            room_map,
            position_left,
            new_position_left, new_position_right
        )

        for box_to_move in boxes_to_move:
            if not _can_move_box_p2(box_to_move, move, room_map):
                return False
        return True

    return room_map


def _move_box_p2(position: Coordinates,
                 move: CoordinateDeltas,
                 room_map: dict[Coordinates, str]
                 ) -> dict[Coordinates, str]:
    position_left = position
    position_right = Coordinates(
        x=position.x + 1,
        y=position.y
    )
    # TODO: take into acc left and right
    new_position_left = Coordinates(
        x=position_left.x + move.dx,
        y=position_left.y + move.dy
    )
    new_position_right = Coordinates(
        x=position_right.x + move.dx,
        y=position_right.y + move.dy
    )
    if (
        room_map.get(new_position_left, None) == _WALL_CHAR
        or room_map.get(new_position_right, None) == _WALL_CHAR
    ):
        return room_map

    if (
        (move.dy and
            (room_map.get(new_position_left, None) in (
                _WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT)
             or room_map.get(new_position_right, None) in (_WIDE_BOX_CHAR_LEFT, _WIDE_BOX_CHAR_RIGHT))
         )
        or (move.dx == -1 and room_map.get(new_position_left, None) == _WIDE_BOX_CHAR_RIGHT)
        or (move.dx == 1 and room_map.get(new_position_right, None) == _WIDE_BOX_CHAR_LEFT)
    ):
        boxes_to_move = _get_boxes_to_move_p2(
            move,
            room_map,
            position_left,
            new_position_left, new_position_right
        )

        for box_to_move in boxes_to_move:
            room_map = _move_box_p2(box_to_move, move, room_map)

    if (
        (not move.dx and new_position_left not in room_map and new_position_right not in room_map)
        or (move.dx == -1 and new_position_left not in room_map)
        or (move.dx == 1 and new_position_right not in room_map)
    ):
        if position_left in room_map:
            del room_map[position_left]
        if position_right in room_map:
            del room_map[position_right]
        room_map[new_position_left] = _WIDE_BOX_CHAR_LEFT
        room_map[new_position_right] = _WIDE_BOX_CHAR_RIGHT

    return room_map


def _visualize_robots_positions(position: Coordinates, room_map: dict[Coordinates, str]) -> str:
    flat_map = [(coordinates, char) for coordinates, char in room_map.items()]
    flat_map.append((position, _ROBOT_CHAR))

    sorted_flat_map = sorted(flat_map, key=lambda el_: (el_[0].y, el_[0].x))
    picture = []
    prev_coord = Coordinates(x=0, y=0)
    line = ""
    for cur_coord, char in sorted_flat_map:
        dy = cur_coord.y - prev_coord.y
        if dy > 0:
            picture.append(line)
            line = ""
            prev_coord = Coordinates(x=0, y=cur_coord.y)
        dx = cur_coord.x - prev_coord.x
        line += "." * (dx - 1) + char
        prev_coord = cur_coord
    picture.append(line)

    return "\n".join(picture)


def _transform_task_input(task_input: TaskInput) -> TaskInput:
    new_room_map = {}
    for coords, char in task_input.room_map.items():
        new_coords_left = Coordinates(
            x=coords.x * 2,
            y=coords.y
        )
        new_coords_right = Coordinates(
            x=coords.x * 2 + 1,
            y=coords.y
        )
        if char == _BOX_CHAR:
            new_room_map[new_coords_left] = _WIDE_BOX_CHAR_LEFT
            new_room_map[new_coords_right] = _WIDE_BOX_CHAR_RIGHT
        elif char == _WALL_CHAR:
            new_room_map[new_coords_left] = _WALL_CHAR
            new_room_map[new_coords_right] = _WALL_CHAR

    new_robot_position = Coordinates(
        x=task_input.robot_position.x*2,
        y=task_input.robot_position.y
    )

    return TaskInput(
        room_map=new_room_map,
        robot_position=new_robot_position,
        moves=task_input.moves
    )


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."

    robot_position = task_input.robot_position
    room_map = task_input.room_map

    for move in task_input.moves:
        robot_position, room_map = _move_robot_p1(
            robot_position, move, room_map
        )

    sum_of_box_coordinates = sum(
        coordinates.gps_coordinate()
        for coordinates, char in room_map.items()
        if char == _BOX_CHAR
    )

    return TaskSolution(sum_of_box_coordinates=sum_of_box_coordinates)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""
    task_input = _transform_task_input(task_input)

    robot_position = task_input.robot_position
    room_map = task_input.room_map

    for move in task_input.moves:
        robot_position, room_map = _move_robot_p2(
            robot_position,
            move, room_map
        )

    sum_of_box_coordinates = sum(
        coordinates.gps_coordinate()
        for coordinates, char in room_map.items()
        if char == _WIDE_BOX_CHAR_LEFT
    )

    return TaskSolution(sum_of_box_coordinates=sum_of_box_coordinates)

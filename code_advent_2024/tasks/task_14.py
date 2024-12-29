"""""Task 14 solver."""
import dataclasses
import re
from code_advent_2024.tasks import task

_ROOM_WIDTH = 101
_ROOM_HEIGHT = 103
_TIME_ELAPSED_SECONDS = 100

_EXTRACT_ROBOT_INFO_REGEXP = r"p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)"


@dataclasses.dataclass(frozen=True)
class Robot:
    """."""
    x: int
    y: int
    dx: int = 0
    dy: int = 0


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    """Represents task input."""
    robots: list[Robot]
    room_width: int = _ROOM_WIDTH
    room_height: int = _ROOM_HEIGHT
    time_elapsed_seconds: int = _TIME_ELAPSED_SECONDS


@dataclasses.dataclass(frozen=True, )
class TaskSolution(task.TaskSolution):
    """Represents task solution."""
    safety_factor: int = 0
    min_number_of_seconds: int = 0


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

    robots = []
    for line in input_string.split("\n"):
        ((x, y, dx, dy), ) = re.findall(_EXTRACT_ROBOT_INFO_REGEXP, line)
        robots.append(Robot(
            x=int(x),
            y=int(y),
            dx=int(dx),
            dy=int(dy),
        ))

    return TaskInput(robots=robots)


def _calc_robot_future_position(
        robot: Robot,
        room_width: int, room_height: int,
        time_elapsed_seconds: int
) -> Robot:
    x = robot.x + (robot.dx + room_width) * time_elapsed_seconds
    x %= room_width
    y = robot.y + (robot.dy + room_height) * time_elapsed_seconds
    y %= room_height

    return dataclasses.replace(robot, x=x, y=y)


def _determine_quadrance(robot: Robot, room_width: int, room_height: int) -> int:
    """."""
    room_center_x = room_width // 2
    room_center_y = room_height // 2
    if robot.x < room_center_x and robot.y < room_center_y:
        return 1
    elif robot.x > room_center_x and robot.y < room_center_y:
        return 2
    elif robot.x < room_center_x and robot.y > room_center_y:
        return 3
    elif robot.x > room_center_x and robot.y > room_center_y:
        return 4
    else:
        return 0


def _visualize_robots_positions(robots: list[Robot]) -> str:
    sorted_robots = sorted(robots, key=lambda robot: (robot.y, robot.x))
    picture = []
    prev_robot = Robot(x=0, y=0)
    line = ""
    for cur_robot in sorted_robots:
        dy = cur_robot.y - prev_robot.y
        if dy > 0:
            picture.append(line)
            picture.extend([""] * (dy - 1))
            line = ""
            prev_robot = Robot(x=0, y=cur_robot.y)
        dx = cur_robot.x - prev_robot.x
        line += " " * (dx - 1) + "*"
        prev_robot = cur_robot
    picture.append(line)

    return "\n".join(picture)


def _is_christmass_tree(robots: list[Robot]) -> bool:
    picture = _visualize_robots_positions(robots)

    return "*" * 20 in picture


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    new_robot_positions = [
        _calc_robot_future_position(
            robot=robot,
            room_width=task_input.room_width,
            room_height=task_input.room_height,
            time_elapsed_seconds=task_input.time_elapsed_seconds
        )
        for robot in task_input.robots
    ]
    robots_per_quadrances = {}
    for robot in new_robot_positions:
        quadrance = _determine_quadrance(
            robot, task_input.room_width, task_input.room_height)
        if quadrance:
            robots_per_quadrances[quadrance] = robots_per_quadrances.get(
                quadrance, 0) + 1

    safety_factor = 1
    for robots_in_quadrance in robots_per_quadrances.values():
        safety_factor *= robots_in_quadrance

    return TaskSolution(safety_factor=safety_factor)


def solve_part2(task_input: TaskInput) -> TaskSolution:
    """Solve the second part of the task."""

    number_of_seconds = 0
    robots = task_input.robots.copy()
    while True:
        if _is_christmass_tree(robots):
            break

        robots = [
            _calc_robot_future_position(
                robot=robot,
                room_width=task_input.room_width,
                room_height=task_input.room_height,
                time_elapsed_seconds=1
            )
            for robot in robots
        ]
        number_of_seconds += 1

    return TaskSolution(min_number_of_seconds=number_of_seconds)

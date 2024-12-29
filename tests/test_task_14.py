"""Task 14 test cases."""
import unittest
from code_advent_2024.tasks import task_14

_INPUT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip("\n")

_ROOM_WIDTH = 11
_ROOM_HEIGHT = 7
_TIME_ELAPSED_SECONDS = 100


class TaskTest(unittest.TestCase):
    """Test cases for task 14."""

    def setUp(self):
        super().setUp()
        self.task_input = task_14.TaskInput(
            robots=task_14.get_input_from_string(_INPUT).robots,
            room_width=_ROOM_WIDTH,
            room_height=_ROOM_HEIGHT,
            time_elapsed_seconds=_TIME_ELAPSED_SECONDS
        )

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_14.solve_part1(self.task_input)

        expected_value = task_14.TaskSolution(safety_factor=12)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

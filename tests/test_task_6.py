"""Task 1 test cases."""
import unittest
from code_advent_2024.tasks import task_6

_INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 1."""

    def setUp(self):
        super().setUp()
        self.task_input = task_6.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_6.solve_part1(self.task_input)

        expected_value = task_6.TaskSolution(patrolled_positions=41)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_6.solve_part2(self.task_input)

        expected_value = task_6.TaskSolution(patrolled_positions=6)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

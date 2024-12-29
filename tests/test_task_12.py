"""Task 12 test cases."""
import unittest
from code_advent_2024.tasks import task_12

_INPUT = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip("\n")

_INPUT_1 = """
AAAA
BBCD
BBCC
EEEC
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 11."""

    def setUp(self):
        super().setUp()
        self.task_input = task_12.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_12.solve_part1(self.task_input)

        expected_value = task_12.TaskSolution(fence_cost=1930)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_12.get_input_from_string(_INPUT_1)

        actual_value = task_12.solve_part1(self.task_input)

        expected_value = task_12.TaskSolution(fence_cost=140)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_12.solve_part2(self.task_input)

        expected_value = task_12.TaskSolution(fence_cost=1206)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2_1(self):
        """Tests solve_part2 method."""
        self.task_input = task_12.get_input_from_string(_INPUT_1)
        actual_value = task_12.solve_part2(self.task_input)

        expected_value = task_12.TaskSolution(fence_cost=80)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

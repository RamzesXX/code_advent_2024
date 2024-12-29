"""Task 7 test cases."""
import unittest
from code_advent_2024.tasks import task_7

_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 1."""

    def setUp(self):
        super().setUp()
        self.task_input = task_7.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_7.solve_part1(self.task_input)

        expected_value = task_7.TaskSolution(
            total_calibration_result=3749)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_7.solve_part2(self.task_input)

        expected_value = task_7.TaskSolution(
            total_calibration_result=11387)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

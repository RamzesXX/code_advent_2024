"""Task 11 test cases."""
import unittest
from code_advent_2024.tasks import task_11

_INPUT = """
0 1 10 99 999
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 11."""

    def setUp(self):
        super().setUp()
        self.task_input = task_11.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_11.solve_part1(self.task_input)

        expected_value = task_11.TaskSolution(number_of_stones=125681)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_11.TaskInput([125, 17])
        actual_value = task_11.solve_part1(self.task_input)

        expected_value = task_11.TaskSolution(number_of_stones=55312)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_11.solve_part2(self.task_input)

        expected_value = task_11.TaskSolution(number_of_stones=149161030616311)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

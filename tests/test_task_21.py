"""Task 21 test cases."""
import unittest
from code_advent_2024.tasks import task_21

_INPUT = """
029A
980A
179A
456A
379A
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 21."""

    def setUp(self):
        super().setUp()
        self.task_input = task_21.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_21.solve_part1(self.task_input)

        expected_value = task_21.TaskSolution(sum_of_complexities=126384)
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_21.solve_part2(self.task_input)

        expected_value = task_21.TaskSolution(sum_of_complexities=0)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

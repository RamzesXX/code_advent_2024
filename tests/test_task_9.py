"""Task 9 test cases."""
import unittest
from code_advent_2024.tasks import task_9

_INPUT = """
2333133121414131402
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 9."""

    def setUp(self):
        super().setUp()
        self.task_input = task_9.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_9.solve_part1(self.task_input)

        expected_value = task_9.TaskSolution(
            filesystem_checksum=1928)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_9.solve_part2(self.task_input)

        expected_value = task_9.TaskSolution(
            filesystem_checksum=3022)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 1 test cases."""
import unittest
from code_advent_2024.tasks import task_1

_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 1."""

    def setUp(self):
        super().setUp()
        self.task_input = task_1.TaskInput(
            left=[3, 4, 2, 1, 3, 3],
            right=[4, 3, 5, 3, 9, 3]
        )

    def test_get_input_from_string(self):
        """Tests if corect TaskInput is built from the string."""
        actual_value = task_1.get_input_from_string(_INPUT)

        expected_value = task_1.TaskInput(
            left=[3, 4, 2, 1, 3, 3],
            right=[4, 3, 5, 3, 9, 3]
        )
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_1.solve_part1(self.task_input)

        expected_value = task_1.TaskSolution(distance=11)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_1.solve_part2(self.task_input)

        expected_value = task_1.TaskSolution(similarity_score=31)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 2 test cases."""
import unittest
from code_advent_2024.tasks import task_2

_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 2."""

    def setUp(self):
        super().setUp()
        self.task_input = task_2.TaskInput(
            reports=[
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9]
            ]
        )

    def test_get_input_from_string(self):
        """Tests if corect TaskInput is built from the string."""
        actual_value = task_2.get_input_from_string(_INPUT)

        expected_value = task_2.TaskInput(
            reports=[
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9]
            ]
        )
        self.assertEqual(expected_value, actual_value)

    def test_solve1(self):
        """Tests solve_part1 method."""
        actual_value = task_2.solve_part1(self.task_input)

        expected_value = task_2.TaskSolution(safe_reports=2)
        self.assertEqual(expected_value, actual_value)

    def test_solve2(self):
        """Tests solve_part2 method."""
        actual_value = task_2.solve_part2(self.task_input)

        expected_value = task_2.TaskSolution(safe_reports=4)
        self.assertEqual(expected_value, actual_value)

    def test_solve2_1(self):
        """Tests solve_part2 method."""
        report_str = "24 25 28 31 28"
        report = [int(x) for x in report_str.split()]

        self.assertTrue(task_2._is_report_safe_p2(report))

    def test_solve2_2(self):
        """Tests solve_part2 method."""
        report_str = "1 2 6 4"
        report = [int(x) for x in report_str.split()]

        self.assertTrue(task_2._is_report_safe_p2(report))


if __name__ == "__main__":
    unittest.main()

"""Task 10 test cases."""
import unittest
from code_advent_2024.tasks import task_10

_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 10."""

    def setUp(self):
        super().setUp()
        self.task_input = task_10.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_10.solve_part1(self.task_input)

        expected_value = task_10.TaskSolution(
            sum_of_scores_of_all_trailheads=36)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_10.solve_part2(self.task_input)

        expected_value = task_10.TaskSolution(
            sum_of_scores_of_all_trailheads=81)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 8 test cases."""
import unittest
from code_advent_2024.tasks import task_8

_INPUT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 8."""

    def setUp(self):
        super().setUp()
        self.task_input = task_8.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_8.solve_part1(self.task_input)

        expected_value = task_8.TaskSolution(
            number_of_unique_antinode_locations=14)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_8.solve_part2(self.task_input)

        expected_value = task_8.TaskSolution(
            number_of_unique_antinode_locations=34)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

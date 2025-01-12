"""Task 16 test cases."""
import unittest
from code_advent_2024.tasks import task_16

_INPUT = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip("\n")

_INPUT_1 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip("\n")

_INPUT_2 = """
####
#.E#
#S.#
####
""".strip("\n")


_INPUT_3 = """
####
#SE#
####
""".strip("\n")

_INPUT_4 = """
#####
###E#
#...#
#.#.#
#...#
#S###
#####
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 16."""

    def setUp(self):
        super().setUp()
        self.task_input = task_16.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_16.solve_part1(self.task_input)

        expected_value = task_16.TaskSolution(score=7036)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_16.get_input_from_string(_INPUT_1)

        actual_value = task_16.solve_part1(self.task_input)

        expected_value = task_16.TaskSolution(score=11048)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_2(self):
        """Tests solve_part1 method."""
        self.task_input = task_16.get_input_from_string(_INPUT_2)

        actual_value = task_16.solve_part1(self.task_input)

        expected_value = task_16.TaskSolution(score=1002)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_3(self):
        """Tests solve_part1 method."""
        self.task_input = task_16.get_input_from_string(_INPUT_3)

        actual_value = task_16.solve_part1(self.task_input)

        expected_value = task_16.TaskSolution(score=1)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_16.solve_part2(self.task_input)

        expected_value = task_16.TaskSolution(best_path_tiles_number=45)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2_1(self):
        """Tests solve_part2 method."""
        self.task_input = task_16.get_input_from_string(_INPUT_1)

        actual_value = task_16.solve_part2(self.task_input)

        expected_value = task_16.TaskSolution(best_path_tiles_number=64)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2_2(self):
        """Tests solve_part2 method."""
        self.task_input = task_16.get_input_from_string(_INPUT_4)

        actual_value = task_16.solve_part2(self.task_input)

        expected_value = task_16.TaskSolution(best_path_tiles_number=10)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

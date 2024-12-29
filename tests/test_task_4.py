"""Task 1 test cases."""
import unittest
from code_advent_2024.tasks import task_4

_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 4."""

    def setUp(self):
        super().setUp()
        self.task_input = task_4.TaskInput(
            puzzle=[
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )

    def test_get_input_from_string(self):
        """Tests if corect TaskInput is built from the string."""
        actual_value = task_4.get_input_from_string(_INPUT)

        expected_value = task_4.TaskInput(
            puzzle=[
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_4.solve_part1(self.task_input)

        expected_value = task_4.TaskSolution(count=18)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_one_line(self):
        """Tests solve_part1 method."""
        self.task_input = task_4.TaskInput(
            puzzle=[
                "MMMSXXMASM",
            ]
        )
        actual_value = task_4.solve_part1(self.task_input)

        expected_value = task_4.TaskSolution(count=1)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_one_line_with_a_single_character(self):
        """Tests solve_part1 method."""
        self.task_input = task_4.TaskInput(
            puzzle=["X"]
        )
        actual_value = task_4.solve_part1(self.task_input)

        expected_value = task_4.TaskSolution(count=0)
        self.assertEqual(expected_value, actual_value)

    def test_solve1_word_in_all_directions(self):
        """Tests solve_part1 method."""
        self.task_input = task_4.TaskInput(
            puzzle=[
                "S..S..S",
                ".A.A.A.",
                "..MMM..",
                "SAMXMAS",
                "..MMM..",
                ".A.A.A.",
                "S..S..S",
            ]
        )
        actual_value = task_4._count_for_position(self.task_input, 3, 3)

        expected_value = 8
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_4.solve_part2(self.task_input)

        expected_value = task_4.TaskSolution(count=9)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

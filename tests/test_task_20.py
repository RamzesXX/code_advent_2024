"""Task 20 test cases."""
import unittest
import dataclasses

from code_advent_2024.tasks import task_20

_INPUT = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 20."""

    def setUp(self):
        super().setUp()
        self.task_input = task_20.get_input_from_string(_INPUT)
        self.task_input = dataclasses.replace(
            self.task_input, min_number_of_saved_picoseconds=12)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_20.solve_part1(self.task_input)

        expected_value = task_20.TaskSolution(
            number_of_cheats=8
        )
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_20.solve_part2(self.task_input)

        expected_value = task_20.TaskSolution(
            number_of_cheats=8
        )
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

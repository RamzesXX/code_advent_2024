"""Task 15 test cases."""
import unittest
from code_advent_2024.tasks import task_15

_INPUT = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip("\n")

_INPUT_1 = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""".strip("\n")

_INPUT_2 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 11."""

    def setUp(self):
        super().setUp()
        self.task_input = task_15.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_15.solve_part1(self.task_input)

        expected_value = task_15.TaskSolution(sum_of_box_coordinates=10092)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_15.get_input_from_string(_INPUT_1)

        actual_value = task_15.solve_part1(self.task_input)

        expected_value = task_15.TaskSolution(sum_of_box_coordinates=2028)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_15.solve_part2(self.task_input)

        expected_value = task_15.TaskSolution(sum_of_box_coordinates=9021)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_15.get_input_from_string(_INPUT_2)

        actual_value = task_15.solve_part2(self.task_input)

        expected_value = task_15.TaskSolution(sum_of_box_coordinates=618)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

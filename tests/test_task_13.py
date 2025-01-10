"""Task 13 test cases."""
import unittest
from code_advent_2024.tasks import task_13

_INPUT = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 13."""

    def setUp(self):
        super().setUp()
        self.task_input = task_13.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_13.solve_part1(self.task_input)

        expected_value = task_13.TaskSolution(number_of_tokens=480)
        self.assertEqual(expected_value, actual_value)

    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_13.solve_part2(self.task_input)

        expected_value = task_13.TaskSolution(number_of_tokens=875318608908)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 3 test cases."""
import unittest
from code_advent_2024.tasks import task_3

_INPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


class TaskTest(unittest.TestCase):
    """Test cases for task 1."""

    def test_get_input_from_string(self):
        """Tests if corect TaskInput is built from the string."""
        actual_value = task_3.get_input_from_string(_INPUT)

        expected_value = task_3.TaskInput(
            mul_string="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        self.assertEqual(expected_value, actual_value)

    def test_solve1(self):
        """Tests solve_part1 method."""
        task_input = task_3.TaskInput(
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )

        actual_value = task_3.solve_part1(task_input)

        expected_value = task_3.TaskSolution(sum_of_mul=161)
        self.assertEqual(expected_value, actual_value)

    def test_solve2(self):
        """Tests solve_part2 method."""
        task_input = task_3.TaskInput(
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )

        actual_value = task_3.solve_part2(task_input)

        expected_value = task_3.TaskSolution(sum_of_mul=48)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 22 test cases."""
import unittest
from parameterized import parameterized
from code_advent_2024.tasks import task_22

_INPUT = """
1
10
100
2024
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 17."""

    def setUp(self):
        super().setUp()
        self.task_input = task_22.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_22.solve_part1(self.task_input)

        expected_value = task_22.TaskSolution(
            sum_of_generated_secret_numbers=37327623)
        self.assertEqual(expected_value, actual_value)

    def test_calc_next_secret_number(self):
        """Tests solve_part1 method."""
        actual_value = task_22.calc_next_secret_number(123)

        expected_value = 15887950
        self.assertEqual(expected_value, actual_value)

    @parameterized.expand([
        (1, 8685429),
        (10, 4700978),
        (100, 15273692),
        (2024, 8667524)
    ])
    def test_get_secret_number_after_iterations(self, secret_number, expected_value):
        """Tests solve_part1 method."""
        actual_value = task_22.get_secret_number_after_iterations(
            secret_number,
            task_22._NUMBER_OF_ITERATIONS
        )

        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_22.solve_part2(self.task_input)

        expected_value = task_22.TaskSolution(
            sum_of_generated_secret_numbers=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

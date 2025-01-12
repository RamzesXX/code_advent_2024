"""Task 16 test cases."""
import unittest
from code_advent_2024.tasks import task_17

_INPUT = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip("\n")

_INPUT_1 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 17."""

    def setUp(self):
        super().setUp()
        self.task_input = task_17.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_17.solve_part1(self.task_input)

        expected_value = task_17.TaskSolution(
            program_output="4,6,3,5,6,3,5,2,1,0")
        self.assertEqual(expected_value, actual_value)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_17.get_input_from_string(_INPUT_1)

        actual_value = task_17.solve_part1(self.task_input)

        expected_value = task_17.TaskSolution(
            program_output="4,2,5,6,7,7,7,7,3,1,0")
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_17.solve_part2(self.task_input)

        expected_value = task_17.TaskSolution(program_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

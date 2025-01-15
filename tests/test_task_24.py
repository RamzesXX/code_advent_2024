"""Task 24 test cases."""
import unittest
from code_advent_2024.tasks import task_24

_INPUT = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 17."""

    def setUp(self):
        super().setUp()
        self.task_input = task_24.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_24.solve_part1(self.task_input)

        expected_value = task_24.TaskSolution(
            program_output="4,6,3,5,6,3,5,2,1,0")
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_24.solve_part2(self.task_input)

        expected_value = task_24.TaskSolution(program_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

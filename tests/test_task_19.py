"""Task 19 test cases."""
import unittest
from code_advent_2024.tasks import task_19

_INPUT = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 19."""

    def setUp(self):
        super().setUp()
        self.task_input = task_19.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_19.solve_part1(self.task_input)

        expected_value = task_19.TaskSolution(
            program_output="4,6,3,5,6,3,5,2,1,0")
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_19.solve_part2(self.task_input)

        expected_value = task_19.TaskSolution(program_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

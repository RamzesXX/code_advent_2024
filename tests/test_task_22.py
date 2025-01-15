"""Task 22 test cases."""
import unittest
from code_advent_2024.tasks import task_22

_INPUT = """
15887950
16495136
527345
704524
1553684
12683156
11100544
12249484
7753432
5908254
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
            program_output="4,6,3,5,6,3,5,2,1,0")
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_22.solve_part2(self.task_input)

        expected_value = task_22.TaskSolution(program_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

"""Task 18 test cases."""

import dataclasses
import unittest
from code_advent_2024.tasks import task_18

_INPUT = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 18."""

    def setUp(self):
        super().setUp()
        task_input = task_18.get_input_from_string(_INPUT)
        self.task_input = dataclasses.replace(
            task_input, end=task_18.Coordinates(6, 6)
        )

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        self.task_input = dataclasses.replace(
            self.task_input,
            coordinates=list(self.task_input.coordinates[:12])
        )

        actual_value = task_18.solve_part1(self.task_input)

        expected_value = task_18.TaskSolution(min_number_of_steps=22)
        self.assertEqual(expected_value, actual_value)

    @ unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_18.solve_part2(self.task_input)

        expected_value = task_18.TaskSolution(min_number_of_steps=0)
        self.assertEqual(expected_value, actual_value)

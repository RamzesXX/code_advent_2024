"""Task 23 test cases."""
import unittest
from code_advent_2024.tasks import task_23

_INPUT = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 17."""

    def setUp(self):
        super().setUp()
        self.task_input = task_23.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_23.solve_part1(self.task_input)

        expected_value = task_23.TaskSolution(
            program_output="4,6,3,5,6,3,5,2,1,0")
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_23.solve_part2(self.task_input)

        expected_value = task_23.TaskSolution(program_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

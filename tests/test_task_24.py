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

_INPUT_1 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 24."""

    def setUp(self):
        super().setUp()
        self.task_input = task_24.get_input_from_string(_INPUT)

    def test_solve_part1(self):
        """Tests solve_part1 method."""
        actual_value = task_24.solve_part1(self.task_input)

        expected_value = task_24.TaskSolution(z_wires_output=4)
        self.assertEqual(expected_value, actual_value)
        self.task_input = task_24.get_input_from_string(_INPUT)

    def test_solve_part1_1(self):
        """Tests solve_part1 method."""
        self.task_input = task_24.get_input_from_string(_INPUT_1)

        actual_value = task_24.solve_part1(self.task_input)

        expected_value = task_24.TaskSolution(z_wires_output=2024)
        self.assertEqual(expected_value, actual_value)

    @unittest.skip("Not implemented yet")
    def test_solve_part2(self):
        """Tests solve_part2 method."""
        actual_value = task_24.solve_part2(self.task_input)

        expected_value = task_24.TaskSolution(z_wires_output=None)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

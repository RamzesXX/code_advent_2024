"""Task 5 test cases."""
import unittest
from code_advent_2024.tasks import task_5

_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip("\n")


class TaskTest(unittest.TestCase):
    """Test cases for task 5."""

    def setUp(self):
        """Set up for test methods."""
        super().setUp()
        self.task_input = task_5.get_input_from_string(_INPUT)

    def test_is_update_correct(self):
        """Tests if update is correctly assesed."""
        actual_value = task_5.is_update_correct(
            self.task_input.updates[0],
            self.task_input.page_ordering_rules_values_after
        )
        self.assertTrue(actual_value)

    def test_correct_update_1(self):
        """Tests if update is correctly fixed."""

        actual_value = task_5.correct_update(
            [75, 97, 47, 61, 53],
            self.task_input.page_ordering_rules_values_after
        )

        expected_value = [97, 75, 47, 61, 53]
        self.assertEqual(actual_value, expected_value)

    def test_correct_update_2(self):
        """Tests if update is correctly fixed."""

        actual_value = task_5.correct_update(
            [61, 13, 29],
            self.task_input.page_ordering_rules_values_after
        )

        expected_value = [61, 29, 13]
        self.assertEqual(actual_value, expected_value)

    def test_correct_update_3(self):
        """Tests if update is correctly fixed."""

        actual_value = task_5.correct_update(
            [97, 13, 75, 29, 47],
            self.task_input.page_ordering_rules_values_after
        )

        expected_value = [97, 75, 47, 29, 13]
        self.assertEqual(actual_value, expected_value)

    def test_solve1(self):
        """Test case for solve_part1."""
        actual_value = task_5.solve_part1(self.task_input)

        expected_value = task_5.TaskSolution(sum_of_middle_page_numbers=143)
        self.assertEqual(expected_value, actual_value)

    def test_solve2(self):
        """Test case for solve_part2."""
        actual_value = task_5.solve_part2(self.task_input)

        expected_value = task_5.TaskSolution(sum_of_middle_page_numbers=123)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()

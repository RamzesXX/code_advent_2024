"""""Task 2 solver."""
import dataclasses
from code_advent_2024.tasks import task


@dataclasses.dataclass(frozen=True)
class TaskInput(task.TaskInput):
    "Represents task input."
    reports: list[list[int]]


@dataclasses.dataclass(frozen=True)
class TaskSolution(task.TaskSolution):
    "Represents task solution."
    safe_reports: int


def get_input_from_file(file_name: str) -> TaskInput:
    """Read input data form a file.

    Args:
        file_name: Path to the file with input data.
    """
    with open(file_name, encoding="ascii") as f:
        file_content = f.read()

    return get_input_from_string(file_content.strip("/n"))


def get_input_from_string(input_string: str) -> TaskInput:
    """Read input data form a string.

    Args:
        input_string: Input data as a string.
    """
    reports = []
    for line in input_string.split("\n"):
        reports.append([int(x_) for x_ in line.split()])
    return TaskInput(reports=reports)


def _is_report_safe_p1(report: list[int]) -> bool:
    if len(report) < 2:
        return False

    diffs = [(report[index] - report[index - 1])
             for index in range(1, len(report))]
    if (
        all((4 > diff > 0) for diff in diffs)
        or all((-4 < diff < 0) for diff in diffs)
    ):
        return True

    return False


def _is_report_safe_p2(report: list[int]) -> bool:
    if _is_report_safe_p1(report):
        return True

    for i in range(len(report)):
        if _is_report_safe_p1(report[:i] + report[i+1:]):
            return True

    return False


def _is_report_safe_p2_(report: list[int]) -> bool:
    if len(report) < 2:
        return False

    #   descending
    #  1 8 9
    skipped = False
    prev_prev = report[1] + 1
    prev = report[0]
    i = 1
    while i < len(report):
        cur = report[i]
        if -4 < (cur - prev) < 0:
            prev_prev = prev
        elif -4 < (cur - prev_prev) < 0 and not skipped:
            skipped = True
        else:
            break

        prev = cur
        i += 1

    if i == len(report) or (i == len(report) - 1 and not skipped):
        return True

    #  ascending
    #  1 8 9
    skipped = False
    prev_prev = report[1] - 1
    prev = report[0]
    i = 1
    while i < len(report):
        cur = report[i]
        if 4 > (cur - prev) > 0:
            prev_prev = prev
        elif 4 > (cur - prev_prev) > 0 and not skipped:
            skipped = True
        else:
            break

        prev = cur
        i += 1

    if i == len(report) or (i == len(report) - 1 and not skipped):
        return True

    return False


def solve_part1(task_input: TaskInput) -> TaskSolution:
    "Solve the first part of the task."
    safe_reports = [
        report
        for report in task_input.reports
        if _is_report_safe_p1(report)
    ]

    return TaskSolution(safe_reports=len(safe_reports))


def solve_part2(task_input: TaskInput) -> TaskSolution:
    "Solve the second part of the task."
    safe_reports = [
        report
        for report in task_input.reports
        if _is_report_safe_p2(report)
    ]

    return TaskSolution(safe_reports=len(safe_reports))

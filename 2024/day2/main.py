import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from util.io import readfile

INPUT_FILE = "input.txt"


def is_report_safe(report: list[int]) -> bool:
    is_increasing = None

    for i in range(1, len(report)):
        prev_level = report[i - 1]
        level = report[i]

        if is_increasing is None:
            is_increasing = prev_level < level

        if (
            (is_increasing and prev_level > level)
            or (not is_increasing and prev_level < level)
            or (abs(prev_level - level) < 1)
            or (abs(prev_level - level) > 3)
        ):
            return False

    return True


def part1(reports: list[list[int]]) -> tuple[int, list[list[int]]]:
    total_safe_reports = 0
    unsafe_reports = []

    for report in reports:
        if is_report_safe(report):
            total_safe_reports += 1
        else:
            unsafe_reports.append(report)

    return (total_safe_reports, unsafe_reports)


def part2(reports: list[list[int]]) -> None:
    total_safe_reports = 0

    for report in reports:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if is_report_safe(new_report):
                total_safe_reports += 1
                break

    return total_safe_reports


if __name__ == "__main__":
    data = readfile(INPUT_FILE)
    parsed_data = [[int(num) for num in line.split(" ")] for line in data]
    (safe_count, unsafe_reports) = part1(parsed_data)

    added_safe_reports = part2(unsafe_reports)

    print(safe_count + added_safe_reports)

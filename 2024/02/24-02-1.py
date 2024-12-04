
import sys


def is_safe(report):
    if report not in (sorted(report), sorted(report, reverse=True)):
        return False
    
    for index, level in enumerate(report):
        next_level_index = index + 1

        if next_level_index == len(report):
            return True

        next_level = report[next_level_index]

        if not (1 <= abs(level - next_level) <= 3):
            return False


def solve(input_text: str) -> str:
    reports = input_text.splitlines()
    reports = [report.split() for report in reports]
    reports = [[int(level) for level in report] for report in reports]

    safe_reports = 0

    for report in reports:
        if is_safe(report):
            safe_reports += 1

    return str(safe_reports)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)

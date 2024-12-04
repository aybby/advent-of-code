import itertools
import sys


TOLERANCE = 1


def get_reports(raw: str) -> list[int]:
    reports = raw.splitlines()
    reports = [report.split() for report in reports]
    reports = [[int(level) for level in report] for report in reports]

    return reports


def is_safe(report):
    ascending = report[0] < report[1]
    errors = 0

    for level_one, level_two in itertools.pairwise(report):
        difference = level_one - level_two

        if not 1 <= abs(difference) <= 3:
            errors += 1
            continue
        
        if difference > 0 and ascending or difference < 0 and not ascending:
            ascending = not ascending
            errors += 1
            continue

    return errors <= TOLERANCE


def solve(input_text: str) -> str:
    reports = get_reports(input_text)
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

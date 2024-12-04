import re
import sys


def solve(input_text: str) -> str:
    total = 0
    for match in re.finditer('mul\\(([0-9]{1,3}),([0-9]{1,3})\\)', input_text):
        total += int(match.group(1)) * int(match.group(2))
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)
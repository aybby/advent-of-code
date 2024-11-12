import sys


def solve(input_text: str) -> str:
    sum = 0

    for line in input_text.splitlines():
        line_numbers = [int(n) for n in line.split("\t") if n]

        line_min = min(line_numbers)
        line_max = max(line_numbers)

        difference = line_max - line_min
        sum += difference

    return str(sum)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)

import itertools
import logging
import sys


CROSSES = ('MSAMS', 'SMASM', 'MMASS', 'SSAMM')


def matches(y: int, x: int) -> bool:
    if y >= height - 2 or x >= height - 2:
        return False

    cross = ''.join([
        puzzle[y][x],
        puzzle[y][x+2],
        puzzle[y+1][x+1],
        puzzle[y+2][x],
        puzzle[y+2][x+2]
    ])

    if cross not in CROSSES:
        return False

    logging.info(f'Match found at ({x}, {y})!')
    return True


def solve(input_text: str) -> str:
    global puzzle
    global height
    global width

    puzzle = [list(line) for line in input_text.splitlines()]
    height, width = len(puzzle), len(puzzle[0])

    count = 0

    for y, x in itertools.product(range(height), range(width)):
        if matches(y, x):
            count += 1

    return count


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)
import itertools
import logging
import sys


DIRECTIONS = list(itertools.product(range(-1, 2), range(-1, 2)))
TARGET = 'XMAS'


def matches(y: int, x: int, direction: list) -> bool:
    logging.info(f'    Testing ({x}, {y}) + {direction}')
    
    for character in TARGET:
        if not (0 <= x < width) or not (0 <= y < height):
            logging.info('    Left boundaries.')
            return False
        if puzzle[y][x] != character:
            logging.info(f'    No match at ({x}, {y}).')
            return False
        
        y += direction[0]
        x += direction[1]

    logging.info('    Match found!')
    return True


def get_xmas_count(y: int, x: int) -> int:
    logging.info(f'Getting count at ({x}, {y}).')
    count = 0

    for direction in DIRECTIONS:
        if matches(y, x, direction):
            count += 1

    return count


def solve(input_text: str) -> str:
    global puzzle
    global height
    global width

    puzzle = [list(line) for line in input_text.splitlines()]
    height, width = len(puzzle), len(puzzle[0])

    count = 0

    for y, x in itertools.product(range(height), range(width)):
        count += get_xmas_count(y, x)

    return count


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)
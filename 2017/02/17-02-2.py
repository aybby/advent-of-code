import itertools
import sys


def parse_numbers(line: str) -> list[int]:
    numbers = line.split('\t')
    numbers = [int(n) for n in numbers]
    numbers.sort(reverse=True)
    
    return numbers


def find_factor(numbers: list[int]) -> tuple[int, int]:
    for number_one, number_two in itertools.combinations(numbers, 2):
        result = number_one / number_two
        
        if result % 1 == 0:
            return result



def solve(input_text: str) -> str:
    sum = 0

    for line in input_text.splitlines():
        numbers = parse_numbers(line)
        factor = find_factor(numbers)
        sum += factor

    return str(sum)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)

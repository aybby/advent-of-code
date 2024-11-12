import sys


def solve(input_text: str) -> str:
    input_length = len(input_text)
    increment = input_length // 2

    sum = 0

    for index, character in enumerate(input_text):
        next_index = (index + increment) % input_length
        
        if input_text[next_index] == character:
            sum += int(character)

    return str(sum)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)
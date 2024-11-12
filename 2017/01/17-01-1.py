import sys


def solve(input_text: str) -> str:
    sum = 0

    for index, character in enumerate(input_text):
        next_index = (index + 1) % len(input_text)
        
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
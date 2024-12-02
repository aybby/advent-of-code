import sys
 

def get_lists(input_text: str) -> tuple[list, list]:
    rows = input_text.splitlines()
    rows = [row.split() for row in rows]
    columns = list(zip(*rows))

    columns = [[int(n) for n in row] for row in columns]
    columns = [sorted(column) for column in columns]

    return columns


def solve(input_text: str) -> str:
    left_list, right_list = get_lists(input_text)

    total_distance = 0

    for left_n, right_n in zip(left_list, right_list):
        distance = abs(left_n - right_n)
        total_distance += distance
    
    return str(total_distance)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)

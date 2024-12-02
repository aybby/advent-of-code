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

    total_similarity = 0

    for n in left_list:
        similarity = right_list.count(n) * n
        total_similarity += similarity
    
    return str(total_similarity)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SyntaxError(f"Usage: python3 {__file__} <input_filepath>")
    
    with open(sys.argv[1]) as input_file:
        input_text = input_file.read()

    solution = solve(input_text)
    print(solution)

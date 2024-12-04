import re
import sys


def solve(input_text: str) -> str:
    input_text = input_text.replace('\n', '')
    input_text = re.sub(r"don't\(\).*?do\(\)", '', input_text)
    print(input_text)
    
    # I *should* be able to do this with another RE, but regex is fucking stupid and none of this works. If
    # $don't\(\).*
    # DOESN'T MATCH DON'T()[any char(s)] AT THE END OF A STRING
    # THEN WHAT THE FUCK *DOES* IT DO REGEX?
    # This isn't jokingly hating RE, this is legitimately an unfun problem for me. Why does it not follow its literal meaning?
    # $ = end of string
    # don't() = literal
    # .* any characters
    # What a stupid technology.
    input_text = input_text.split("don't()")[0]

    print(input_text)

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
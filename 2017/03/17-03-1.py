import logging
import math


def get_spiral(input_number: int) -> tuple:
    spiral_number = 0
    while True:
        spiral_maximum = (2 * spiral_number + 1) ** 2

        logging.info(f'Spiral #{spiral_number} max: {spiral_maximum}')

        if spiral_maximum >= input_number:
            logging.info(f'Spiral found, returning {spiral_number}, {spiral_maximum}.')
            return spiral_number, spiral_maximum
    
        spiral_number += 1


def get_middles(spiral_number: int, spiral_maximum: int) -> list:
    last_middle = spiral_maximum - spiral_number
    quarter_around_distance = math.sqrt(spiral_maximum) - 1
    middles = [last_middle - i * quarter_around_distance for i in range(4)]
    logging.info(f'Middles: {middles}')
    return middles


def find_middle_distance(input_number: int, middles: list) -> int:
    middle_distances = [abs(input_number - middle) for middle in middles]
    logging.info(f'Middles distances: {middle_distances}')
    return min(middle_distances)


def find_distance(input_number: int) -> int:
    spiral_number, spiral_maximum = get_spiral(input_number)
    middles = get_middles(spiral_number, spiral_maximum)
    middle_distance = find_middle_distance(input_number, middles)
    distance = spiral_number + middle_distance 
    return distance


def main():
    logging.basicConfig(level=logging.INFO)
    input_number = int(input('Input number: '))
    distance = find_distance(input_number)
    print('Distance:', distance)


if __name__ == '__main__':
    main()
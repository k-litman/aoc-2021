from typing import List, Tuple

from part_a import read_input


def parse_input(input_list: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal, aim, depth = 0, 0, 0
    for direction, value in input_list:
        if direction == 'forward':
            horizontal += value
            depth += aim * value
        elif direction == 'up':
            aim -= value
        else:
            aim += value

    return horizontal, depth


def main() -> None:
    input_list = read_input('input')
    horizontal, depth = parse_input(input_list)
    print(horizontal * depth)


if __name__ == '__main__':
    main()

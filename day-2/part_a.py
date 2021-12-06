from typing import List, Tuple


def parse_input(input_list: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal, depth = 0, 0
    for direction, value in input_list:
        if direction == 'forward':
            horizontal += value
        elif direction == 'up':
            depth -= value
        else:
            depth += value
    return horizontal, depth


def read_input(filename: str) -> List[Tuple[str, int]]:
    input_list = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            direction, value = line.split(' ')
            value = int(value)
            input_list.append((direction, value))
    return input_list


def main() -> None:
    input_list = read_input('input')
    horizontal, depth = parse_input(input_list)
    print(horizontal * depth)


if __name__ == '__main__':
    main()

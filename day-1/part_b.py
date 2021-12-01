from typing import List

from part_a import get_increases_count


def get_windows(numbers: List[int]) -> List[int]:
    windows = []
    for i in range(len(numbers) - 2):
        windows.append(sum(numbers[i:i+3]))
    return windows


def main() -> None:
    with open('input', 'r') as f:
        windows = get_windows([int(line) for line in f.readlines()])

    print(get_increases_count(windows))


if __name__ == '__main__':
    main()

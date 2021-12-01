from typing import List


def get_increases_count(numbers: List[int]) -> int:
    prev = None
    res = 0
    for curr in numbers:
        if prev is not None and prev < curr:
            res += 1
        prev = curr
    return res


def main() -> None:
    with open('input', 'r') as f:
        print(get_increases_count([int(line) for line in f.readlines()]))


if __name__ == '__main__':
    main()

import re

MAGIC_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def process_input(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def find_muls(input: str):
    return [match.groups() for match in re.finditer(MAGIC_PATTERN, input)]


if __name__ == "__main__":
    input = process_input("input.txt")
    pairs = [(int(a), int(b)) for a, b in find_muls(input)]
    products = [a * b for a, b in pairs]
    print(sum(products))

def process_file(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(map(int, line.strip().split(" "))) for line in lines]


def compute_diffs(report: list[int]):
    return [num - report[last_index] for last_index, num in enumerate(report[1:])]


def check_diffs(diff: list[int]):
    if diff[0] < 0:
        diff = [-1 * val for val in diff]

    return all(0 < val < 4 for val in diff)


if __name__ == "__main__":
    reports = process_file("input.txt")
    diffs = [compute_diffs(report) for report in reports]
    valids = [check_diffs(diff) for diff in diffs]
    print(valids.count(True))

def process_file(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(map(int, line.strip().split(" "))) for line in lines]


def compute_diffs(report: list[int]):
    return [num - report[last_index] for last_index, num in enumerate(report[1:])]


def check_diffs(diff: list[int]):
    if diff[0] <= 0 or diff[1] <= 0:
        diff = [-1 * val for val in diff]

    dampened = False
    for i, val in enumerate(diff):
        if 0 < val < 4:
            continue
        elif dampened == False:
            dampened = True
            if 0 < val + diff[i - 1] < 4:
                continue
            elif i + 1 < len(diff) and 0 < val + diff[i + 1] < 4:
                continue
            else:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    reports = process_file("input.txt")
    diffs = [compute_diffs(report) for report in reports]
    valids = [check_diffs(diff) for diff in diffs]
    print(valids.count(True))

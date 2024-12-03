def process_file(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [list(map(int, line.strip().split(" "))) for line in lines]


def compute_diffs(report: list[int]):
    return [num - report[last_index] for last_index, num in enumerate(report[1:])]


def check_diffs(diff: list[int], dampener: int = 0):
    if diff[0] < 0:
        diff = [-1 * val for val in diff]

    return all(0 < val < 4 for val in diff)


def get_best(report):
    if check_diffs(compute_diffs(report)):
        return report
    else:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if check_diffs(compute_diffs(new_report)):
                return new_report
        return report  # it's gonna fail but we need to return something


if __name__ == "__main__":
    reports = process_file("basic_input.txt")
    diffs = [compute_diffs(report) for report in reports]
    valids = [check_diffs(diff) for diff in diffs]
    print(valids.count(True))

    best_valids = [check_diffs(compute_diffs(get_best(report))) for report in reports]
    print(best_valids.count(True))

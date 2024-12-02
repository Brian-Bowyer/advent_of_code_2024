from collections import Counter


def process_file(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        list1, list2 = [], []
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            split_line = lines[i].split(" ")
            list1.append(int(split_line[0]))
            list2.append(int(split_line[-1]))

        return list1, list2


def main1():
    l1, l2 = process_file("input.txt")
    l1_sorted = sorted(l1)
    l2_sorted = sorted(l2)
    distances = []
    for pair in zip(l1_sorted, l2_sorted):
        distance = abs(pair[0] - pair[1])
        distances.append(distance)
    print(sum(distances))


def calculate_similarity(left: list[int], right: list[int]):
    right_counter = Counter(right)
    similarity = 0
    for item in left:
        similarity += right_counter[item] * item
    return similarity


if __name__ == "__main__":
    main1()

def part1():
    print("In how many assignment pairs does one range fully contain the other?")
    contained = 0

    with open("./res/day4.txt", "r") as f:
        for line in f.readlines():
            item1: set
            item2: set
            item1, item2 = line.strip().split(',')
            item1 = set(
                [i for i in range(int(item1.split("-")[0]), int(item1.split("-")[1]) + 1)])
            item2 = set(
                [i for i in range(int(item2.split("-")[0]), int(item2.split("-")[1]) + 1)])

            if item1.issubset(item2) or item2.issubset(item1):
                contained += 1

    print(contained)


def part2():
    print("In how many assignment pairs do the ranges overlap?")
    overlap = 0

    with open("./res/day4.txt", "r") as f:
        for line in f.readlines():
            item1: set
            item2: set
            item1, item2 = line.strip().split(',')
            item1 = set(
                [i for i in range(int(item1.split("-")[0]), int(item1.split("-")[1]) + 1)])
            item2 = set(
                [i for i in range(int(item2.split("-")[0]), int(item2.split("-")[1]) + 1)])

            if item1.intersection(item2):
                overlap += 1

    print(overlap)


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/4")
    part1()
    part2()

import re


def part1():
    print("How many characters need to be processed before the first start-of-packet marker is detected?")
    with open("./res/day6.txt", "r") as f:
        line = f.readline()
        index = 4
        while True:
            chars = line[index-4:index]
            # check duplicates
            chars_to_set = set(chars)
            if len(chars_to_set) == len(chars):
                # no duplicates
                print(index)
                return

            # case duplicates
            index += 1


def part2():
    print("How many characters need to be processed before the first start-of-message marker is detected?")
    with open("./res/day6.txt", "r") as f:
        line = f.readline()
        index = 14
        while True:
            chars = line[index-14:index]
            # check duplicates
            chars_to_set = set(chars)
            if len(chars_to_set) == len(chars):
                # no duplicates
                print(index)
                return

            # case duplicates
            index += 1


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/6")
    part1()
    part2()

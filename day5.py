import re


def part1():
    print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
    crates = dict()

    with open("./res/day5.txt", "r") as f:
        for line in f.readlines():
            crates_re = re.compile(
                r'(.{3})\s{1}')
            crates_match = crates_re.findall(line)

            for idx, i in enumerate(crates_match, start=1):
                if idx not in crates:
                    crates[idx] = list()
                if i != '   ':
                    crates[idx].insert(0, i)

            command_re = re.compile(
                r'^move ([0-9]*) from ([0-9]*) to ([0-9]*)\n')
            command_match = command_re.match(line)

            if command_match:
                crates_to_move = command_match.group(1)
                crates_from = command_match.group(2)
                crates_to = command_match.group(3)

                for i in range(int(crates_to_move)):
                    crate = crates[int(crates_from)].pop()
                    crates[int(crates_to)].append(crate)

        result = ""
        for c in crates.values():
            if c:
                result += c[-1]

        print(result.replace("[", "").replace("]", ""))


def part2():
    print("After the rearrangement procedure completes, what crate ends up on top of each stack?")
    crates = dict()

    with open("./res/day5.txt", "r") as f:
        for line in f.readlines():
            crates_re = re.compile(
                r'(.{3})\s{1}')
            crates_match = crates_re.findall(line)

            for idx, i in enumerate(crates_match, start=1):
                if idx not in crates:
                    crates[idx] = list()
                if i != '   ':
                    crates[idx].insert(0, i)

            command_re = re.compile(
                r'^move ([0-9]*) from ([0-9]*) to ([0-9]*)\n')
            command_match = command_re.match(line)

            if command_match:
                crates_to_move = command_match.group(1)
                crates_from = command_match.group(2)
                crates_to = command_match.group(3)

                crates_list = list()
                for i in range(int(crates_to_move)):
                    crates_list.insert(0, crates[int(crates_from)].pop())

                crates[int(crates_to)].extend(crates_list)

        result = ""
        for c in crates.values():
            if c:
                result += c[-1]

        print(result.replace("[", "").replace("]", ""))


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/5")
    part1()
    part2()

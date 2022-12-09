def part1():
    print("How many total Calories is that Elf carrying?")
    res = 0
    current = 0

    with open("./res/day1.txt", "r") as f:
        for line in f.readlines():
            if line == "\n":
                if current > res:
                    res = current
                current = 0
            else:
                current = current + int(line.strip())

    print(f"{res} Calories")


def part2():
    print("How many total Calories are top three Elfs carrying?")
    res = []
    current = 0

    with open("./res/day1.txt", "r") as f:
        for line in f.readlines():
            if line == "\n":
                res.append(current)
                current = 0
            else:
                current = current + int(line.strip())

    sorted_res = sorted(res, reverse=True)
    print("{0} Calories".format(sorted_res[0]+sorted_res[1]+sorted_res[2]))


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/1")
    part1()
    part2()

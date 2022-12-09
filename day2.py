def part1():
    print("What would your total score be if everything goes exactly according to your strategy guide?")
    res = 0

    values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    with open("./res/day2.txt", "r") as f:
        for line in f.readlines():
            m1, m2 = line.strip().split(" ")

            if m1 == "A":
                if m2 == "X":
                    res = res + values[m2] + 3
                elif m2 == "Y":
                    res = res + values[m2] + 6
                else:
                    res = res + values[m2] + 0

            if m1 == "B":
                if m2 == "X":
                    res = res + values[m2] + 0
                elif m2 == "Y":
                    res = res + values[m2] + 3
                else:
                    res = res + values[m2] + 6

            if m1 == "C":
                if m2 == "X":
                    res = res + values[m2] + 6
                elif m2 == "Y":
                    res = res + values[m2] + 0
                else:
                    res = res + values[m2] + 3
    print(res)


def part2():
    print("What would your total score be if everything goes exactly according to your strategy 2 guide?")
    res = 0

    values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    with open("./res/day2.txt", "r") as f:
        for line in f.readlines():
            m1, m2 = line.strip().split(" ")

            if m2 == "X":
                if m1 == "A":
                    res = res + values["Z"]
                elif m1 == "B":
                    res = res + values["X"]
                else:
                    res = res + values["Y"]

            if m2 == "Y":
                if m1 == "A":
                    res = res + values["X"] + 3
                elif m1 == "B":
                    res = res + values["Y"] + 3
                else:
                    res = res + values["Z"] + 3

            if m2 == "Z":
                if m1 == "A":
                    res = res + values["Y"] + 6
                elif m1 == "B":
                    res = res + values["Z"] + 6
                else:
                    res = res + values["X"] + 6
    print(res)


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/2")
    part1()
    part2()

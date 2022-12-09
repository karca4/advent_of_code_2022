def part1():
    print("What is the sum of the priorities of those item types?")
    priority = 0

    with open("./res/day3.txt", "r") as f:
        for line in f.readlines():
            item = line.strip()
            item_len = len(item)
            item1 = set(item[:item_len//2])
            item2 = set(item[item_len//2:])

            intersection = item1.intersection(item2)
            if intersection:
                c = intersection.pop()
                if c.islower():
                    priority = priority + ord(c)-96
                else:
                    priority = priority + 26 + ord(c)-64
            else:
                print(
                    f"No character in common in substrings {item1} - {item2}")

    print(priority)


def part2():
    print("What is the sum of the priorities of those item types?")
    priority = 0

    with open("./res/day3.txt", "r") as f:
        count = 1
        lines = []
        for line in f:
            lines.append(set(line.strip()))
            if count % 3 == 0:
                intersection = set.intersection(*lines)
                if intersection:
                    c = intersection.pop()
                    if c.islower():
                        priority = priority + ord(c)-96
                    else:
                        priority = priority + 26 + ord(c)-64
                else:
                    print(
                        f"No character in common in substrings {[x for x in lines]}")

                lines = []
            count += 1

    print(priority)


if __name__ == "__main__":
    print("https://adventofcode.com/2022/day/3")
    part1()
    part2()

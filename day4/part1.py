def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        [range1, range2] = line.strip().split(",")
        [a1, b1] = [int(i) for i in (range1.split("-"))]
        [a2, b2] = [int(i) for i in (range2.split("-"))]

        # Check condition for complete overlap
        if (a1 <= a2 and b1 >= b2) or (a2 <= a1 and b2 >= b1):
            total += 1

    print(total)


if __name__ == "__main__":
    main()

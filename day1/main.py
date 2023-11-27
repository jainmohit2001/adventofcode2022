def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    # Maximum calorie encountered so far
    max_cal = 0

    # Calories for the current elf
    cal = 0

    for line in lines:
        # If empty line
        if line == "\n":
            max_cal = max(max_cal, cal)
            cal = 0
            continue

        cal += int(line)

    print(max_cal)


if __name__ == "__main__":
    main()

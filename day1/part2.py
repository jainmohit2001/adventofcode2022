def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    # Top three maximum calories encountered so far
    max_cal = [0, 0, 0]

    # Calories for the current elf
    cal = 0

    for line in lines:
        # If empty line
        if line == "\n":
            if cal >= max_cal[0]:
                max_cal[2] = max_cal[1]
                max_cal[1] = max_cal[0]
                max_cal[0] = cal
            elif cal >= max_cal[1]:
                max_cal[2] = max_cal[1]
                max_cal[1] = cal
            elif cal >= max_cal[2]:
                max_cal[2] = cal
            cal = 0
            continue

        cal += int(line)

    print(max_cal[0] + max_cal[1] + max_cal[2])


if __name__ == "__main__":
    main()

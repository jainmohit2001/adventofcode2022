ORD_a = ord("a") - 1
ORD_A = ord("A") - 1


def main():
    # Read input

    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    priorities = 0

    for i in range(0, len(lines), 3):
        # Counters for each type for three consecutive lines
        counters = [
            [0 for i in range(53)],
            [0 for i in range(53)],
            [0 for i in range(53)],
        ]

        # For the next 3 lines
        for row in range(3):
            for char in lines[i + row].strip():
                # Find the idx and increment the counter
                if char >= "a" and char <= "z":
                    idx = ord(char) - ORD_a
                else:
                    idx = ord(char) - ORD_A + 26
                counters[row][idx] += 1

        # Check the column which as the whole row > 0
        for col in range(53):
            if counters[0][col] > 0 and counters[1][col] > 0 and counters[2][col] > 0:
                priorities += col
                break

    print(priorities)


if __name__ == "__main__":
    main()

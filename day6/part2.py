def process_signal(signal: str):
    for i in range(0, len(signal) - 14):
        chars = {}
        duplicate = False

        for j in range(0, 14):
            if signal[i + j] in chars:
                duplicate = True
                break
            chars[signal[i + j]] = True

        if not duplicate:
            print(i + j + 1)
            return


def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    for line in lines:
        process_signal(line.strip())


if __name__ == "__main__":
    main()

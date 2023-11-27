def main():
    # Read file
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    points = 0

    for line in lines:
        [opponent, mine] = line.strip().split(" ")

        if mine == "X":
            # Loose
            if opponent == "A":
                points += 3  # Opponent has rock, I need scissors
            elif opponent == "B":
                points += 1  # Opponent has paper, I need rock
            elif opponent == "C":
                points += 2  # Opponent has scissors, I need paper
        elif mine == "Y":
            # Draw
            points += 3

            if opponent == "A":
                points += 1  # Opponent has rock, I need rock
            elif opponent == "B":
                points += 2  # Opponent has paper, I need paper
            elif opponent == "C":
                points += 3  # Opponent has scissors, I need scissors
        elif mine == "Z":
            # Win
            points += 6

            if opponent == "A":
                points += 2  # Opponent has rock, I need paper
            elif opponent == "B":
                points += 3  # Opponent has paper, I need scissors
            elif opponent == "C":
                points += 1  # Opponent has scissors, I need rock

    print(points)


if __name__ == "__main__":
    main()

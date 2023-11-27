def main():
    # Read file
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    points = 0

    for line in lines:
        [opponent, mine] = line.strip().split(" ")

        # Add points for the shape selected
        if mine == "X":
            points += 1  # Rock - 1
        elif mine == "Y":
            points += 2  # Paper - 2
        elif mine == "Z":
            points += 3  # Scissors - 3

        # Win cases
        # Opponent has rock and mine is paper
        # or Opponent has paper and mine is scissors
        # or Opponent has scissors and mine is rock.
        if (
            (opponent == "A" and mine == "Y")
            or (opponent == "B" and mine == "Z")
            or (opponent == "C" and mine == "X")
        ):
            points += 6

        # Draw cases
        elif (
            (opponent == "A" and mine == "X")
            or (opponent == "B" and mine == "Y")
            or (opponent == "C" and mine == "Z")
        ):
            points += 3

    print(points)


if __name__ == "__main__":
    main()

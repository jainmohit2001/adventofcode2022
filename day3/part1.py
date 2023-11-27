ORD_a = ord("a") - 1
ORD_A = ord("A") - 1


def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    priority = 0

    for line in lines:
        hashmap = {}

        length = len(line)

        # Traverse the left half and populate the hash map
        for i in range(int(length / 2)):
            if line[i] in hashmap:
                hashmap[line[i]] += 1
            else:
                hashmap[line[i]] = 1

        # Traverse the right half and find the matching element
        for i in range(int(length / 2), length):
            if line[i] in hashmap:
                if line[i] >= "a" and line[i] <= "z":
                    p = ord(line[i]) - ORD_a
                else:
                    p = ord(line[i]) - ORD_A + 26

                # print(line[i], p)
                priority += p
                break

    print(priority)


if __name__ == "__main__":
    main()

from utils import Node, print_tree, parse_input

TOTAL_SIZE = 0


def traverse_tree(node: Node) -> int:
    global TOTAL_SIZE

    if node.is_dir is False:
        return

    if node.size <= 100000:
        print(node.name, node.size)
        TOTAL_SIZE += node.size

    for child in node.children:
        if child.is_dir is True:
            traverse_tree(child)


def main():
    global TOTAL_SIZE
    # Read file
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    root = parse_input(lines)
    # print_tree(root)

    TOTAL_SIZE = 0
    traverse_tree(root)
    print(TOTAL_SIZE)


if __name__ == "__main__":
    main()

from utils import Node, parse_input, print_tree

TOTAL_DISK_SPACE_AVAILABLE = 70000000
REQUIRED_UNUSED_SPACE = 30000000
DIR_SIZE_NEEDED = None
CUR_DIR_SIZE = None


def traverse_tree(node: Node):
    global DIR_SIZE_NEEDED, CUR_DIR_SIZE

    if node.is_dir is False:
        return

    # The DIR Satisfies our needs
    if node.size >= DIR_SIZE_NEEDED:
        if (node.size - DIR_SIZE_NEEDED) < (CUR_DIR_SIZE - DIR_SIZE_NEEDED):
            CUR_DIR_SIZE = node.size
    else:
        return

    for child in node.children:
        if child.is_dir is True and child.size >= DIR_SIZE_NEEDED:
            traverse_tree(child)


def main():
    global DIR_SIZE_NEEDED, CUR_DIR_SIZE
    # Read file
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    root = parse_input(lines)
    # print_tree(root)
    CUR_DIR_SIZE = root.size
    DIR_SIZE_NEEDED = REQUIRED_UNUSED_SPACE - (TOTAL_DISK_SPACE_AVAILABLE - root.size)

    print(f"Total space occupied {root.size}")
    print(f"Minimum space need to run {DIR_SIZE_NEEDED}")

    traverse_tree(root)
    print(CUR_DIR_SIZE)


if __name__ == "__main__":
    main()

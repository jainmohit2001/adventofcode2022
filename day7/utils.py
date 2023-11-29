from typing import List


class Node:
    def __init__(self, is_dir: bool, name: str, size: int, parent=None):
        self.is_dir = is_dir
        self.name = name
        self.size = size
        self.children: List["Node"] = []
        self.parent = None

    def add_child(self, node: "Node"):
        node.parent = self

        # Add the size of the node to all the parents
        curNode = self
        while curNode is not None:
            curNode.size += node.size
            curNode = curNode.parent

        self.children.append(node)

    def get_child(self, name):
        if self.is_dir is False:
            raise ValueError("Operation not allowed for File node")

        for node in self.children:
            if node.name == name:
                return node

        raise ValueError(f"No child found with name {name} in dir {self.name}")


def print_tree(node: Node, indent: str = ""):
    if node.is_dir is False:
        print(f"{indent}- {node.name} (file, size={node.size})")
        return

    print(f"{indent}- {node.name} (dir, size={node.size})")

    for child in node.children:
        print_tree(child, indent + "  ")


def parse_input(lines: List[str]) -> Node:
    root = Node(True, "/", 0)  # The root dir
    cwd = root  # The current working dir

    for i in range(len(lines)):
        line = lines[i].strip()

        # If a command is found
        if line[0] == "$":
            line_split = line.split(" ")
            command = line_split[1]

            # Change directory command
            if command == "cd":
                arg = line_split[2]
                if arg == "..":
                    cwd = cwd.parent
                elif arg == "/":
                    cwd = root
                else:
                    cwd = cwd.get_child(arg)
            continue

        # A dir is found in the cwd
        if line[0] == "d":
            name = line.split(" ")[1]
            new_dir = Node(True, name, 0, cwd)
            cwd.add_child(new_dir)
        # A file is found in the cwd
        else:
            [size, name] = line.split(" ")
            new_file = Node(False, name, int(size), cwd)
            cwd.add_child(new_file)

    return root

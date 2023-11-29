from typing import TypeVar

from utils import CrateParser, ProcedureParser, Stack

T = TypeVar("T")

SPACE = " "
OPEN_BRACKETS = "["
CLOSED_BRACKETS = "]"


def main():
    # Read input
    with open("input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    # The stack inputs
    inputs = []

    # The starting pos in the file where the move statements start
    move_start_pos = 0
    for idx, line in enumerate(lines):
        if line == "\n":
            move_start_pos = idx + 1
            break

    # Parse each stack input line
    for i in range(move_start_pos - 2):
        parser = CrateParser(lines[i])
        inputs.append(parser.parse())

    # print(inputs)

    stacks = [Stack[str]() for i in range(len(inputs[0]))]

    # Start from bottom of the input stack and keep adding crates
    row = len(inputs) - 1
    while row >= 0:
        for idx, crate in enumerate(inputs[row]):
            if crate is not None:
                stacks[idx].push(crate)
        row -= 1

    # for stack in stacks:
    #     print(stack._arr)

    # Parse procedures
    procedures = [
        ProcedureParser(lines[i]).parse() for i in range(move_start_pos, len(lines))
    ]

    # Perform procedures
    for proc in procedures:
        # print(proc.quantity, proc.source, proc.destination)
        for _ in range(proc.quantity):
            crate = stacks[proc.source - 1].pop()
            stacks[proc.destination - 1].push(crate)

    top_list = ""

    for i, stack in enumerate(stacks):
        top_list += stack.peek()

    print(top_list)


if __name__ == "__main__":
    main()

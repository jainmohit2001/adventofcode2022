from typing import Any, Union, TypeVar, Generic, List

T = TypeVar("T")

SPACE = " "
OPEN_BRACKETS = "["
CLOSED_BRACKETS = "]"


class Stack(Generic[T]):
    _arr: List[T]

    def __init__(self):
        self._arr = []

    def push(self, item: T) -> None:
        self._arr.append(item)

    def pop(self) -> T:
        return self._arr.pop()

    def size(self) -> int:
        return len(self._arr)

    def peek(self) -> T:
        return self._arr[-1]


class CrateParser:
    line: str
    pos: int

    def __init__(self, line: str):
        self.line = line
        self.pos = 0

    def parse(self) -> list:
        # List of crates in the given line
        crate_list = []

        while (self.pos < len(self.line)) and self.__current_token() != "\n":
            crate = self.__parse_crate()
            crate_list.append(crate)
            if self.__current_token() == "\n":
                break
            self.__consume_token(SPACE)

        return crate_list

    def __parse_crate(self) -> Union[str, None]:
        # An empty crate represents three spaces in the line
        if self.__current_token() == SPACE:
            for _ in range(3):
                self.__consume_token(token=SPACE)
            return None

        # Example: [P], [Q]
        self.__consume_token(token=OPEN_BRACKETS)
        crate = self.__consume_token()
        self.__consume_token(token=CLOSED_BRACKETS)
        return crate

    def __consume_token(self, token=None) -> str:
        # Cross check if the current char is the given token
        char = self.__current_token()
        if token is not None and char != token:
            raise ValueError(
                f"Invalid char {self.line[self.pos]} found at {self.pos}. Expected {token}"
            )

        self.pos += 1
        return char

    def __current_token(self) -> str:
        return self.line[self.pos]


class Procedure:
    quantity: int
    source: int
    destination: int

    def __init__(self, quantity: int, source: int, destination: int) -> None:
        self.quantity = quantity
        self.source = source
        self.destination = destination


class ProcedureParser:
    line: str
    pos: int

    def __init__(self, line: str) -> None:
        self.line = line
        self.pos = 0

    def parse(self) -> Procedure:
        self.__consume_token(token="m")
        self.__consume_token(token="o")
        self.__consume_token(token="v")
        self.__consume_token(token="e")

        self.__consume_token(token=SPACE)
        quantity = self.__parseInt()

        self.__consume_token(token="f")
        self.__consume_token(token="r")
        self.__consume_token(token="o")
        self.__consume_token(token="m")

        self.__consume_token(token=SPACE)
        source = self.__parseInt()

        self.__consume_token(token="t")
        self.__consume_token(token="o")

        self.__consume_token(token=SPACE)
        destination = self.__parseInt()

        return Procedure(quantity, source, destination)

    def __parseInt(self) -> int:
        start_pos = self.pos

        while self.pos < len(self.line):
            char = self.__consume_token()
            if char == SPACE or char == "\n":
                break

        return int(self.line[start_pos : self.pos])

    def __consume_token(self, token=None) -> str:
        # Cross check if the current char is the given token
        char = self.__current_token()
        if token is not None and char != token:
            raise ValueError(
                f"Invalid char {self.line[self.pos]} found at {self.pos}. Expected {token}"
            )

        self.pos += 1
        return char

    def __current_token(self) -> str:
        return self.line[self.pos]

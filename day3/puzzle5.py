from dataclasses import dataclass
from enum import Enum, auto


class State(Enum):
    DOT = auto()
    NUMBER = auto()
    SYMBOL = auto()


@dataclass
class NumberRegistration:
    begin_char_pos: int
    end_char_pos: int
    value: int


def puzzle5():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()
    symbol_registry = set()
    number_registry = []
    new_number_registry = []
    part_numbers = []

    state = State.DOT
    is_part_number = False
    current_number = ""

    for line_no, line in enumerate(input_data):
        print(line)
        for char_pos, char in enumerate(line):
            if char == '.':
                if state == State.NUMBER:
                    if is_part_number or (line_no - 1, char_pos) in symbol_registry:
                        print(f"Part Number: {current_number}")
                        part_numbers.append(int(current_number))
                    else:
                        print(
                            f"Registered: {current_number} for {char_pos - len(current_number)}-{char_pos - 1} on {line_no}")
                        new_number_registry.append(
                            NumberRegistration(char_pos - len(current_number), char_pos - 1, int(current_number)))
                    current_number = ""
                    is_part_number = False
                state = State.DOT
            elif '0' <= char <= '9':
                if state == State.SYMBOL:
                    is_part_number = True
                elif state == State.DOT:
                    if (line_no - 1, char_pos - 1) in symbol_registry:
                        is_part_number = True
                if (line_no - 1, char_pos) in symbol_registry:
                    is_part_number = True
                current_number += char
                state = State.NUMBER
            else:
                if state == State.NUMBER:
                    print(f"Part Number: {current_number}")
                    part_numbers.append(int(current_number))
                    current_number = ""
                    is_part_number = False
                for n in number_registry:
                    if (n.begin_char_pos - 1) <= char_pos <= (n.end_char_pos + 1):
                        print(f"Found {n.value} on previous line")
                        part_numbers.append(n.value)
                        n.value = 0
                symbol_registry.add((line_no, char_pos))
                print(f"Added {char} to registry at ({line_no}, {char_pos})")
                state = State.SYMBOL
        if state == State.NUMBER:
            if state == State.NUMBER:
                if is_part_number:
                    part_numbers.append(int(current_number))
                else:
                    char_pos = len(line) - 1
                    print(f"Registered: {current_number}")
                    new_number_registry.append(
                        NumberRegistration(char_pos - len(current_number), char_pos - 1, int(current_number)))
                current_number = ""
                is_part_number = False
            state = State.DOT
        number_registry = new_number_registry[:]
        new_number_registry = []
    print(sum(part_numbers))


if __name__ == "__main__":
    puzzle5()

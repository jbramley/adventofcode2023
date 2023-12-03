from collections import defaultdict
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


def puzzle6():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()
    gear_registry = set()
    number_registry = []
    new_number_registry = []
    gear_list = defaultdict(list)

    state = State.DOT
    current_number = ""
    current_gears = []

    for line_no, line in enumerate(input_data):
        print(line)
        for char_pos, char in enumerate(line):
            if char == '*':
                if state == State.NUMBER:
                    print(f"Part Number: {current_number}")
                    gear_list[(line_no, char_pos)].append(int(current_number))
                    for g in current_gears:
                        gear_list[g].append(int(current_number))
                    new_number_registry.append(
                        NumberRegistration(char_pos - len(current_number), char_pos - 1, int(current_number)))
                    current_number = ""
                    current_gears = []
                for n in number_registry:
                    if (n.begin_char_pos - 1) <= char_pos <= (n.end_char_pos + 1):
                        print(f"Found {n.value} on previous line")
                        gear_list[(line_no, char_pos)].append(n.value)
                gear_registry.add((line_no, char_pos))
                print(f"Added {char} to registry at ({line_no}, {char_pos})")
                state = State.SYMBOL
            elif '0' <= char <= '9':
                if state == State.SYMBOL:
                    current_gears.append((line_no, char_pos - 1))
                elif state == State.DOT:
                    if (line_no - 1, char_pos - 1) in gear_registry:
                        current_gears.append((line_no - 1, char_pos - 1))
                if (line_no - 1, char_pos) in gear_registry:
                    current_gears.append((line_no - 1, char_pos))
                current_number += char
                state = State.NUMBER
            else:
                if state == State.NUMBER:
                    if (line_no - 1, char_pos) in gear_registry:
                        current_gears.append((line_no - 1, char_pos))
                    for g in current_gears:
                        gear_list[g].append(int(current_number))
                    print(
                        f"Registered: {current_number} for {char_pos - len(current_number)}-{char_pos - 1} on {line_no}")
                    new_number_registry.append(
                        NumberRegistration(char_pos - len(current_number), char_pos - 1, int(current_number)))
                    current_number = ""
                    current_gears = []
                state = State.DOT
        if state == State.NUMBER:
            for g in current_gears:
                gear_list[g].append(int(current_number))
            char_pos = len(line) - 1
            print(f"Registered: {current_number}")
            new_number_registry.append(
                NumberRegistration(char_pos - len(current_number), char_pos - 1, int(current_number)))
            current_number = ""
            current_gears = []
            state = State.DOT
        number_registry = new_number_registry[:]
        new_number_registry = []
    print(sum(g[0] * g[1] for g in gear_list.values() if len(g) == 2))


if __name__ == "__main__":
    puzzle6()

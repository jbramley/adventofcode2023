import math


def puzzle11():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    time = int(''.join(t for t in input_data[0].split(" ")[1:] if t))
    distance = int(''.join(d for d in input_data[1].split(" ")[1:] if d))

    answer_1 = (-time - math.sqrt((time**2)-(4*distance)))/-2
    answer_2 = (-time + math.sqrt((time**2)-(4*distance)))/-2
    ways_to_win = math.floor(answer_1) - math.ceil(answer_2) + 1
    print(ways_to_win)


if __name__ == '__main__':
    puzzle11()
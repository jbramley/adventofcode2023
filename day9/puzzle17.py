import itertools
import pprint


def puzzle17():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    total = 0
    for line in input_data:
        seq = [int(x) for x in line.split(" ")]
        diff_stack = []
        diffs = [x1-x0 for x0, x1 in itertools.pairwise(seq)]
        while any(diffs):
            diff_stack.append(diffs)
            diffs = [x1 - x0 for x0, x1 in itertools.pairwise(diffs)]
        addee = 0
        while diff_stack:
            d = diff_stack.pop()
            addee += d[-1]
        total += seq[-1] + addee
    print(total)


if __name__ == '__main__':
    puzzle17()

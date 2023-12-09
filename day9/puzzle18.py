import itertools
import pprint


def puzzle18():
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
        sub = 0
        while diff_stack:
            d = diff_stack.pop()
            sub = d[0] - sub
        total += seq[0] - sub
    print(total)


if __name__ == '__main__':
    puzzle18()

import functools
from collections import Counter

card_ranks = "23456789TJQKA"

hand_rank = [
    (1, 1, 1, 1, 1),
    (2, 1, 1, 1),
    (2, 2, 1,),
    (3, 1, 1,),
    (3, 2),
    (4, 1),
    (5,),
]


def puzzle13():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    hands = {}
    for line in input_data:
        hand, bid = line.split(" ")
        c = Counter(hand)
        hands[hand_rank.index(tuple(i[1] for i in c.most_common())), tuple(card_ranks.index(c) for c in hand)] = bid

    winnings = 0
    for i, k in enumerate(sorted(hands.keys())):
        winnings += (i + 1) * int(hands[k])

    print(winnings)


if __name__ == "__main__":
    puzzle13()

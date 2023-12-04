def puzzle8():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    number_cards = [1]*len(input_data)
    for i, line in enumerate(input_data):
        _, numbers = line.split(":")
        winning_numbers, our_numbers = numbers.split("|")
        winning_numbers = set(w for w in winning_numbers.strip().split())
        our_numbers = [1 for n in our_numbers.strip().split() if n in winning_numbers]
        for j in range(len(our_numbers)):
            new_card_i = i + j + 1
            if new_card_i < len(input_data):
                number_cards[i + j + 1] += number_cards[i]
    print(sum(number_cards))


if __name__ == "__main__":
    puzzle8()

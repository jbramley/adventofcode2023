def puzzle7():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    total_points = 0
    for line in input_data:
        _, numbers = line.split(":")
        winning_numbers, our_numbers = numbers.split("|")
        winning_numbers = set(w for w in winning_numbers.strip().split())
        our_numbers = [1 for n in our_numbers.strip().split() if n in winning_numbers]
        if not our_numbers:
            continue
        total_points += 2 ** (len(our_numbers) - 1)
    print(total_points)


if __name__ == "__main__":
    puzzle7()

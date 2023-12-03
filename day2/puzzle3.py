MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def puzzle3():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.readlines()

    good_games = 0
    for line in input_data:
        game_id, pulls = line.split(":")
        possible = True
        for pull in pulls.split(";"):
            ball_counts = pull.split(",")
            for b_c in ball_counts:
                c, b = b_c.strip().split(" ")
                if int(c) > MAX_CUBES[b.strip()]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            continue
        g, i = game_id.split(" ")
        good_games += int(i)
    print(good_games)


if __name__ == "__main__":
    puzzle3()

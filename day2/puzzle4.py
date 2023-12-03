def puzzle4():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.readlines()

    power_sum = 0
    for line in input_data:
        min_balls = {"red": 0, "green": 0, "blue": 0}
        game, pulls = line.split(":")
        for p in pulls.split(";"):
            balls = p.split(",")
            for b_c in balls:
                c, b = b_c.strip().split(" ")
                b = b.strip()
                c = int(c)
                min_balls[b] = max(min_balls[b], c)
        power_sum += (min_balls["red"] * min_balls["blue"] * min_balls["green"])
    print(power_sum)


if __name__ == "__main__":
    puzzle4()
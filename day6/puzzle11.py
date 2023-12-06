def puzzle11():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    times = [int(t) for t in input_data[0].split(" ")[1:] if t]
    distances = [int(d) for d in input_data[1].split(" ")[1:] if d]

    races = zip(times, distances)
    ways_to_win = 1
    for t, d in races:
        race_ways_to_win = 0
        for i in range(t):
            if i * (t - i) > d:
                race_ways_to_win += 1
        ways_to_win *= race_ways_to_win

    print(ways_to_win)


if __name__ == '__main__':
    puzzle11()
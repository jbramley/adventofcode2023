import itertools
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class SeedInformation:
    seed: int
    soil: int | None = None
    fertilizer: int | None = None
    water: int | None = None
    light: int | None = None
    temperature: int | None = None
    humidity: int | None = None
    location: int | None = None


@dataclass
class PlantingMap:
    destination_start: int
    source_start: int
    range_len: int


def map_seed(seed, maps, source_type, map_type):
    for m in maps[map_type]:
        if m.source_start <= getattr(seed, source_type) <= (m.source_start + m.range_len - 1):
            setattr(seed, map_type, m.destination_start + (getattr(seed, source_type) - m.source_start))
            break
    else:
        setattr(seed, map_type, getattr(seed, source_type))


def puzzle9():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    seeds_line = input_data[0]
    seeds = [SeedInformation(seed=int(s)) for s in seeds_line[len("seeds: "):].split(" ")]

    maps: dict[str, list[PlantingMap]] = defaultdict(list)
    current_map = None
    for i, line in enumerate(input_data[1:]):
        match line:
            case "seed-to-soil map:":
                current_map = "soil"
            case "soil-to-fertilizer map:":
                current_map = "fertilizer"
            case "fertilizer-to-water map:":
                current_map = "water"
            case "water-to-light map:":
                current_map = "light"
            case "light-to-temperature map:":
                current_map = "temperature"
            case "temperature-to-humidity map:":
                current_map = "humidity"
            case "humidity-to-location map:":
                current_map = "location"
            case "":
                continue
            case _:
                if line[0].isdigit():
                    maps[current_map].append(PlantingMap(*[int(n) for n in line.split(" ")]))
    for seed in seeds:
        for source, dest in itertools.pairwise(["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]):
            map_seed(seed, maps, source, dest)

    print(sorted(seeds, key=lambda k: k.location))
    

if __name__ == "__main__":
    puzzle9()
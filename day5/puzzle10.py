import itertools
import pprint
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
    destination_end: int
    source_start: int
    source_end: int
    id: str | None = None
    location: int | None = None


def map_seed(seed, maps, source_type, map_type):
    for m in maps[map_type]:
        if m.source_start <= getattr(seed, source_type) <= (m.source_start + m.range_len - 1):
            setattr(seed, map_type, m.destination_start + (getattr(seed, source_type) - m.source_start))
            break
    else:
        setattr(seed, map_type, getattr(seed, source_type))


def overlaps(s0, e0, s1, e1):
    return e0 >= s1 and s0 <= e1


def split_overlaps(s0, e0, s1, e1) -> tuple[tuple[int, int] | None, tuple[int, int], tuple[int, int] | None]:
    return (s0, s1 - 1) if s0 < s1 else None, (max(s0, s1), max(e0, e1)), (e1 + 1, e0) if e0 > e1 else None


def puzzle9():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    mapping_stack = [("seed", int(r[0]), int(r[0]) + int(r[1]) - 1, f"seed_{r[0]}") for r in
                     list(itertools.pairwise(input_data[0][len("seeds: "):].split(" ")))[::2]]

    almanac_maps: dict[str, list[PlantingMap]] = defaultdict(list)
    processed_maps: dict[str, list[PlantingMap]] = defaultdict(list)
    next_map = {"seed": "soil", "soil": "fertilizer", "fertilizer": "water", "water": "light", "light": "temperature",
                "temperature": "humidity", "humidity": "location"}
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
                    dest_start, source_start, range_len = (int(n) for n in line.split(" "))
                    almanac_maps[current_map].append(
                        PlantingMap(dest_start, dest_start + range_len - 1, source_start, source_start + range_len - 1,
                                    f"{current_map}_{len(almanac_maps[current_map])}"))

    lowest_location = None
    while mapping_stack:
        m = mapping_stack.pop()
        lookup_map = next_map[m[0]]
        for p_m in processed_maps[lookup_map]:
            if overlaps(m[1], m[2], p_m.source_start, p_m.source_end):
                before, overlap, after = split_overlaps(m[1], m[2], p_m.source_start, p_m.source_end)
                if before:
                    mapping_stack.append((m[0], before[0], before[1], m[3] + f"[{m[0]}_{before[0]}_{before[1]}]"))
                if after:
                    mapping_stack.append((m[0], after[0], after[1], m[3] + f"[{m[0]}_{after[0]}_{after[1]}]"))

                processed_maps[lookup_map].append(
                    PlantingMap(overlap[0] - p_m.source_start + p_m.destination_start,
                                overlap[1] - p_m.source_start + p_m.destination_start,
                                overlap[0],
                                overlap[1]))
                m = None
                break
        if m is None:
            continue
        for p_m in almanac_maps[lookup_map]:
            if overlaps(m[1], m[2], p_m.source_start, p_m.source_end):
                before, overlap, after = split_overlaps(m[1], m[2], p_m.source_start, p_m.source_end)
                if before:
                    mapping_stack.append((m[0], before[0], before[1], m[3] + f"[{m[0]}_{before[0]}_{before[1]}]"))
                if after:
                    mapping_stack.append((m[0], after[0], after[1], m[3] + f"[{m[0]}_{after[0]}_{after[1]}]"))
                if lookup_map == "location":
                    location = overlap[0] - p_m.source_start + p_m.destination_start
                    if lowest_location is None or location < lowest_location:
                        print(f"New lowest location: {location} from {m[3]}")
                        lowest_location = location
                    processed_maps[lookup_map].append(
                        PlantingMap(overlap[0] - p_m.source_start + p_m.destination_start,
                                    overlap[1] - p_m.source_start + p_m.destination_start,
                                    overlap[0], overlap[1], location=location))
                else:
                    mapping_stack.append(
                        (lookup_map, overlap[0] - p_m.source_start + p_m.destination_start,
                         overlap[1] - p_m.source_start + p_m.destination_start, f"{m[3]}[{overlap[0]}_{overlap[1]}]-{p_m.id}"))
                break
        else:
            if lookup_map == "location":
                location = m[1]
                if lowest_location is None or location < lowest_location:
                    print(f"New lowest location: {location} from {m[3]}")
                    lowest_location = location
                processed_maps[lookup_map].append(PlantingMap(m[1], m[2], m[1], m[2]))
            else:
                mapping_stack.append((lookup_map, m[1], m[2], f"{m[3]}[{m[1]}_{m[2]}-{lookup_map}_missing"))
    print(lowest_location)


if __name__ == "__main__":
    puzzle9()

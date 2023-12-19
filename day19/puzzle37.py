from dataclasses import dataclass
from enum import Enum


class SimpleRule(Enum):
    ACCEPT = 'A'
    REJECT = 'R'


@dataclass
class CompRule:
    attr: str
    op: str
    val: int
    result: str | SimpleRule


Rule = CompRule | SimpleRule | str


OP_TO_FN = {
    ">": "__gt__",
    "<": "__lt__",
}

def puzzle37():
    with open("input", "r", encoding="utf") as fp:
        input_data = fp.read()

    rule_data, part_data = [d.splitlines() for d in input_data.split("\n\n")]
    rulebook = {}
    for rule in rule_data:
        name = rule[:rule.index('{')]
        rules = rule[rule.index('{') + 1:-1].split(",")
        rule_list = []
        for r in rules:
            if ':' in r:
                comp, result = r.split(":")
                if result in 'AR':
                    result = SimpleRule(result)
                c = CompRule(comp[0], OP_TO_FN[comp[1]], int(comp[2:]), result)
                rule_list.append(c)
            else:
                if r in 'AR':
                    r = SimpleRule(r)
                rule_list.append(r)
        rulebook[name] = rule_list

    total = 0

    for part_line in part_data:
        part = dict((a,int(v)) for a,v in [av.split("=") for av in part_line[1:-1].split(",")])
        page = "in"
        final_result = None
        while True:
            for r in rulebook[page]:
                result = None
                match r:
                    case CompRule(attr, op, val, res):
                        if getattr(part[attr], op)(val):
                            result = res
                    case _:
                        result = r
                if isinstance(result, SimpleRule):
                    final_result = result
                    break
                if isinstance(result, str):
                    page = result
                    break
            if final_result is not None:
                if final_result == SimpleRule.ACCEPT:
                    total += sum(part.values())
                break

    print(total)


if __name__ == '__main__':
    puzzle37()

from __future__ import annotations

import pprint
from dataclasses import dataclass


@dataclass
class RuleComp:
    attr: str
    op: str
    val: int

    def __invert__(self):
        return RuleComp(self.attr, "<>"[self.op == "<"] + "=", self.val)


@dataclass
class RuleRange:
    x0: int = 1
    x1: int = 4000
    m0: int = 1
    m1: int = 4000
    a0: int = 1
    a1: int = 4000
    s0: int = 1
    s1: int = 4000

    def update(self, comp: RuleComp):
        if len(comp.op) == 1:
            if comp.op[0] == "<":
                v = getattr(self, comp.attr + "1")
                setattr(self, comp.attr + "1", min(v, comp.val - 1))
            else:
                v = getattr(self, comp.attr + "0")
                setattr(self, comp.attr + "0", max(v, comp.val + 1))
        else:
            if comp.op[0] == "<":
                v = getattr(self, comp.attr + "1")
                setattr(self, comp.attr + "1", min(v, comp.val))
            else:
                v = getattr(self, comp.attr + "0")
                setattr(self, comp.attr + "0", max(v, comp.val))

    def combinations(self):
        return (self.x1 + 1 - self.x0) * (self.m1 + 1 - self.m0) * (self.a1 + 1 - self.a0) * (self.s1 + 1 - self.s0)


ALWAYS = RuleComp("x", ">", -1)


@dataclass
class RuleNode:
    parent: RuleNode | None
    comp: RuleComp | None
    children: tuple[RuleNode | bool, RuleNode | bool]


def build_rule_tree(page, rulebook, rule_no=0) -> RuleNode:
    r = rulebook[page][rule_no]
    if ":" in r:
        comp = RuleComp(r[0], r[1], int(r[2:r.index(":")]))
        result = r[r.index(":") + 1:]
        if result == 'A':
            child_0 = True
        elif result == 'R':
            child_0 = False
        else:
            child_0 = build_rule_tree(result, rulebook)
        if rule_no < len(rulebook[page]) - 1:
            child_1 = build_rule_tree(page, rulebook, rule_no + 1)
        else:
            child_1 = ~child_0
        node = RuleNode(None, comp=comp, children=(child_0, child_1))
        if isinstance(child_0, RuleNode):
            child_0.parent = node
        if isinstance(child_1, RuleNode):
            child_1.parent = node
        return node
    else:
        if r == "A":
            return RuleNode(parent=None, comp=ALWAYS, children=(True, True))
        elif r == "R":
            return RuleNode(parent=None, comp=ALWAYS, children=(False, False))
        else:
            child = build_rule_tree(r, rulebook)
            node = RuleNode(None, comp=ALWAYS, children=(child, False))
            child.parent = node
            return node


def get_accepted_paths(node) -> list[RuleRange] | None:
    if node.comp == ALWAYS:
        if isinstance(node.children[0], bool):
            if node.children[0]:
                return [RuleRange()]
            else:
                return None
        else:
            return get_accepted_paths(node.children[0])
    else:
        paths = []
        for i, c in enumerate(node.children):
            if i == 1:
                comp = ~node.comp
            else:
                comp = node.comp
            if c is True:
                r = RuleRange()
                r.update(comp)
                paths.append(r)
            elif c is False:
                continue
            else:
                child_paths = get_accepted_paths(c)
                if child_paths is not None:
                    for p in child_paths:
                        p.update(comp)
                        paths.append(p)

        return paths


def puzzle38():
    with open("input", "r", encoding="utf") as fp:
        input_data = fp.read()

    rule_data, part_data = [d.splitlines() for d in input_data.split("\n\n")]
    rulebook = {}
    for rule_line in rule_data:
        name = rule_line[:rule_line.index('{')]
        rules = rule_line[rule_line.index('{') + 1:-1].split(",")
        rulebook[name] = rules

    rule_tree = build_rule_tree("in", rulebook)
    accepted_paths = get_accepted_paths(rule_tree)

    pprint.pprint(accepted_paths)
    for r in accepted_paths:
        print(f"{r} -> {r.combinations()}")
    print(sum(r.combinations() for r in accepted_paths))
    # 167_409_079_868_000
    # 256_000_000_000_000
    # 189_284_490_000
    # 196_638_594_000


if __name__ == '__main__':
    puzzle38()

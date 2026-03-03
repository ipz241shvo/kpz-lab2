from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Virus:
    weight: float
    age: int
    name: str
    kind: str
    children: List["Virus"] = field(default_factory=list)

    # Prototype: deep clone (clone itself + all children recursively)
    def clone(self) -> "Virus":
        cloned_children = [child.clone() for child in self.children]
        return Virus(
            weight=self.weight,
            age=self.age,
            name=self.name,
            kind=self.kind,
            children=cloned_children
        )

    def add_child(self, child: "Virus") -> None:
        self.children.append(child)

    def print_tree(self, indent: int = 0) -> None:
        pad = "  " * indent
        print(f"{pad}- {self.name} ({self.kind}), age={self.age}, weight={self.weight}, id={id(self)}")
        for child in self.children:
            child.print_tree(indent + 1)


if __name__ == "__main__":
    # ==============================
    # 1-2) Create "family" (3 generations)
    # ==============================
    grandparent = Virus(weight=1.2, age=10, name="Alpha", kind="RNA")

    parent1 = Virus(weight=0.9, age=6, name="Beta", kind="RNA")
    parent2 = Virus(weight=1.0, age=7, name="Gamma", kind="DNA")

    child1 = Virus(weight=0.4, age=2, name="Delta", kind="RNA")
    child2 = Virus(weight=0.5, age=1, name="Epsilon", kind="RNA")
    child3 = Virus(weight=0.6, age=3, name="Zeta", kind="DNA")

    # Build tree:
    parent1.add_child(child1)
    parent1.add_child(child2)
    parent2.add_child(child3)

    grandparent.add_child(parent1)
    grandparent.add_child(parent2)

    print("=== ORIGINAL FAMILY ===")
    grandparent.print_tree()

    # ==============================
    # 3-5) Prototype: deep clone
    # ==============================
    clone_family = grandparent.clone()

    print("\n=== CLONED FAMILY ===")
    clone_family.print_tree()

    # Show independence: change clone, original not affected
    clone_family.name = "Alpha_CLONE"
    clone_family.children[0].name = "Beta_CLONE"
    clone_family.children[0].children[0].name = "Delta_CLONE"

    print("\n=== AFTER CHANGING CLONE (ORIGINAL MUST STAY SAME) ===")
    print("\nORIGINAL:")
    grandparent.print_tree()

    print("\nCLONE:")
    clone_family.print_tree()
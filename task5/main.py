from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Protocol
from abc import ABC, abstractmethod


# ==========================
# Product
# ==========================

@dataclass
class Character:
    role: str                      # "Hero" / "Enemy"
    name: str = "Unknown"
    height_cm: int = 170
    body_type: str = "Average"
    hair_color: str = "Brown"
    eye_color: str = "Brown"
    outfit: str = "Simple clothes"
    inventory: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)

    # специфічне: добрі/злі справи
    good_deeds: List[str] = field(default_factory=list)
    evil_deeds: List[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            f"Role: {self.role}",
            f"Name: {self.name}",
            f"Height: {self.height_cm} cm",
            f"Body: {self.body_type}",
            f"Hair: {self.hair_color}",
            f"Eyes: {self.eye_color}",
            f"Outfit: {self.outfit}",
            f"Inventory: {', '.join(self.inventory) if self.inventory else '-'}",
            f"Skills: {', '.join(self.skills) if self.skills else '-'}",
        ]
        if self.good_deeds:
            lines.append(f"Good deeds: {', '.join(self.good_deeds)}")
        if self.evil_deeds:
            lines.append(f"Evil deeds: {', '.join(self.evil_deeds)}")
        return "\n".join(lines)


# ==========================
# Builder Interface
# ==========================

class ICharacterBuilder(ABC):
    @abstractmethod
    def reset(self) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_name(self, name: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_height(self, cm: int) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_body_type(self, body_type: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_hair_color(self, color: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_eye_color(self, color: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def set_outfit(self, outfit: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def add_item(self, item: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def add_skill(self, skill: str) -> "ICharacterBuilder": ...

    @abstractmethod
    def build(self) -> Character: ...


# ==========================
# HeroBuilder
# ==========================

class HeroBuilder(ICharacterBuilder):
    def __init__(self):
        self._character = Character(role="Hero")

    def reset(self) -> "HeroBuilder":
        self._character = Character(role="Hero")
        return self

    # fluent interface: return self
    def set_name(self, name: str) -> "HeroBuilder":
        self._character.name = name
        return self

    def set_height(self, cm: int) -> "HeroBuilder":
        self._character.height_cm = cm
        return self

    def set_body_type(self, body_type: str) -> "HeroBuilder":
        self._character.body_type = body_type
        return self

    def set_hair_color(self, color: str) -> "HeroBuilder":
        self._character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> "HeroBuilder":
        self._character.eye_color = color
        return self

    def set_outfit(self, outfit: str) -> "HeroBuilder":
        self._character.outfit = outfit
        return self

    def add_item(self, item: str) -> "HeroBuilder":
        self._character.inventory.append(item)
        return self

    def add_skill(self, skill: str) -> "HeroBuilder":
        self._character.skills.append(skill)
        return self

    # спеціальне "добро"
    def add_good_deed(self, deed: str) -> "HeroBuilder":
        self._character.good_deeds.append(deed)
        return self

    def build(self) -> Character:
        result = self._character
        self.reset()
        return result


# ==========================
# EnemyBuilder (same interface)
# ==========================

class EnemyBuilder(ICharacterBuilder):
    def __init__(self):
        self._character = Character(role="Enemy")

    def reset(self) -> "EnemyBuilder":
        self._character = Character(role="Enemy")
        return self

    def set_name(self, name: str) -> "EnemyBuilder":
        self._character.name = name
        return self

    def set_height(self, cm: int) -> "EnemyBuilder":
        self._character.height_cm = cm
        return self

    def set_body_type(self, body_type: str) -> "EnemyBuilder":
        self._character.body_type = body_type
        return self

    def set_hair_color(self, color: str) -> "EnemyBuilder":
        self._character.hair_color = color
        return self

    def set_eye_color(self, color: str) -> "EnemyBuilder":
        self._character.eye_color = color
        return self

    def set_outfit(self, outfit: str) -> "EnemyBuilder":
        self._character.outfit = outfit
        return self

    def add_item(self, item: str) -> "EnemyBuilder":
        self._character.inventory.append(item)
        return self

    def add_skill(self, skill: str) -> "EnemyBuilder":
        self._character.skills.append(skill)
        return self

    # спеціальне "зло"
    def add_evil_deed(self, deed: str) -> "EnemyBuilder":
        self._character.evil_deeds.append(deed)
        return self

    def build(self) -> Character:
        result = self._character
        self.reset()
        return result


# ==========================
# Director
# ==========================

class CharacterDirector:
    def __init__(self, builder: ICharacterBuilder):
        self._builder = builder

    def set_builder(self, builder: ICharacterBuilder) -> None:
        self._builder = builder

    def create_dream_hero(self) -> Character:
        # Використовуємо fluent interface
        # (тут можна фантазію будь-яку)
        b = self._builder.reset()
        # якщо передали EnemyBuilder — все одно збудує, але роль буде Enemy
        return (b.set_name("Astra")
                .set_height(176)
                .set_body_type("Athletic")
                .set_hair_color("Silver")
                .set_eye_color("Blue")
                .set_outfit("Light armor + cloak")
                .add_skill("Sword mastery")
                .add_skill("Healing")
                .add_item("Sword of Dawn")
                .add_item("Health potion")
                .build())

    def create_arch_enemy(self) -> Character:
        b = self._builder.reset()
        return (b.set_name("Noctar")
                .set_height(190)
                .set_body_type("Massive")
                .set_hair_color("Black")
                .set_eye_color("Red")
                .set_outfit("Dark plate armor")
                .add_skill("Necromancy")
                .add_skill("Fear aura")
                .add_item("Cursed blade")
                .add_item("Shadow amulet")
                .build())


# ==========================
# Main (демонстрація)
# ==========================

if __name__ == "__main__":

    hero_builder = HeroBuilder()
    enemy_builder = EnemyBuilder()

    director = CharacterDirector(hero_builder)

    # Герой мрії через директора
    hero = director.create_dream_hero()

    # Додаткові "добрі справи" (спец. методи для HeroBuilder)
    # Це не обов'язково робити через директора — можна після.
    hero_builder.reset().set_name(hero.name)  # просто показ fluent-ланцюжок на HeroBuilder
    # (вище рядок не змінює hero; це демонстрація builder-ланцюжка)

    # Ворог через директора (перемикаємо білдер)
    director.set_builder(enemy_builder)
    enemy = director.create_arch_enemy()

    # Додамо злі справи (спец. метод EnemyBuilder)
    enemy_builder.reset().set_name(enemy.name)  # демонстрація fluent

    print("=== HERO ===")
    print(hero.summary())

    print("\n=== ENEMY ===")
    print(enemy.summary())

    # Додаткова перевірка fluent interface без директора:
    custom_enemy = (EnemyBuilder()
                    .set_name("Ruin")
                    .set_height(205)
                    .set_body_type("Giant")
                    .set_hair_color("White")
                    .set_eye_color("Green")
                    .set_outfit("Rags of the Abyss")
                    .add_skill("Poison")
                    .add_item("Toxic dagger")
                    .add_evil_deed("Burned the ancient library")
                    .add_evil_deed("Cursed a whole village")
                    .build())

    print("\n=== CUSTOM ENEMY (FLUENT) ===")
    print(custom_enemy.summary())
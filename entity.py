from typing import Tuple

"A generic object to represent a generic entity such as players, enemies, items,etc"
class Entity:
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self,dx: int, dy: int):
        self.x += dx
        self.y += dy

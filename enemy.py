import pygame
from typing import Iterable

from .entity import Entity
from .constants import DISPLAY_SIZE


class Enemy(Entity):
    def __init__(self, image: pygame.Surface, coords: Iterable[float], speed: int, damage: float):
        super().__init__(image, coords, speed)
        self.damage = damage

    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()

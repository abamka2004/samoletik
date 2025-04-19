from .entity import Entity
from .constants import DISPLAY_SIZE


class Enemy(Entity):
    def __init__(self, image, coords, speed, damage: int | float):
        super().__init__(image, coords, speed, damage)
        self.damage = damage

    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()

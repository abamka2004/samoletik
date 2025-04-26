from typing import Iterable

import pygame


class Entity:
    def __init__(self, image: pygame.Surface, coords: Iterable[float], speed: float):
        self.image = image.copy()
        self.rect = self.image.get_frect(center=coords)
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)
        self.alive = True

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def kill(self) -> None:
        self.alive = False

    def move(self, x: int, y: int) -> None:
        self.rect.move_ip(x, y)

    def collide_entity(self, other) -> bool:
        return pygame.sprite.collide_mask(self, other)

from typing import Any, Iterable
import pygame

from .entity import Entity
from .constants import SHOOT_EVENT, DISPLAY_SIZE


class Player(Entity):
    def __init__(self, animation: Iterable[pygame.Surface], coords: tuple[float, int], speed: float, health: int=100):
        super().__init__(animation[0], coords, speed)
        self.health = health

        self.animation = animation
        self.last_update = pygame.time.get_ticks()
        self.current_frame = 0
        self.frame_rate = 80
    
    def get_damage(self, value: int) -> None:
        self.health -= value
    
        if self.health <= 0:
            self.kill()
            self.health = 0
    
    def update(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        left = pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]
        right = pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]

        if left != right:
            if left:
                self.move(-self.speed, 0)
            else:
                self.move(self.speed, 0)
    
        just_pressed_keys = pygame.key.get_just_pressed()
        if just_pressed_keys[pygame.K_SPACE]:
            pygame.event.post(pygame.Event(SHOOT_EVENT))
        
        #animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.current_frame += 1
            if self.current_frame == len(self.animation):
                self.animation.reverse()
                self.current_frame = 0

            self.image = self.animation[self.current_frame]
            self.last_update = now


    def move(self, x: float, y: float):
        super().move(x, y)

        if self.rect.right < 0:
            self.rect.centerx = DISPLAY_SIZE[0]
        
        if self.rect.left > DISPLAY_SIZE[0]:
            self.rect.centerx = 0
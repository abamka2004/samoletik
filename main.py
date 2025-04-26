import pygame

from random import randint

from src.constants import MAX_FPS, DISPLAY_SIZE
from src.constants import SHOOT_EVENT, SPAWN_EVENT
from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy


def game(display: pygame.Surface, clock: pygame.time.Clock) -> None:
    coords = DISPLAY_SIZE[0] /2, DISPLAY_SIZE[1] -50
    player_image = pygame.Surface((50, 50))
    player_image.fill('blue')
    player = Player(player_image, coords, 6, 100)

    bullet_image = pygame.Surface([20, 20])
    bullet_image.fill('green')
    bullets = list()

    enemy_image = pygame.Surface([50, 50])
    enemy_image.fill('red')
    enemies = list()

    difficulty = 0
    pygame.time.set_timer(SPAWN_EVENT, 3000, 1)


    while True:
        difficulty += clock.get_time()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                b = Bullet(bullet_image, player.rect.midtop, 10)
                bullets.append(b)
            elif event.type == SPAWN_EVENT:
                millis = round(2000 - difficulty / 70) 
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)

                coords = [randint(50, DISPLAY_SIZE[0] - 50), -enemy_image.height]
                speed = 5 + difficulty / 35_000
                damage = round(10 + difficulty / 7000)
                e = Enemy(enemy_image, coords, speed, damage)
                enemies.append(e)

        # update
        player.update()

        for b in bullets.copy():
            b.update()
            if not b.alive:
                bullets.remove(b)

        for e in enemies.copy():
            e.update()
            if not e.alive:
                enemies.remove(e)

        # render
        display.fill((0,0,0))

        player.render(display)

        for b in bullets:
            b.render(display)

        for e in enemies:
            e.render(display)
 
        pygame.display.update()
        clock.tick(MAX_FPS)

def main() -> None:
    pygame.init()

    display = pygame.display.set_mode(DISPLAY_SIZE, flags=pygame.RESIZABLE | pygame.SCALED ,vsync=True)
    pygame.display.set_caption('Shooter')

    clock = pygame.time.Clock()

    while True:
        game(display, clock)

if __name__ == '__main__':
    main()

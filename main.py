import pygame

from random import randint

from src.constants import (
    MAX_FPS, DISPLAY_SIZE, HEALTH_BAR_WIDTH, PLAYER_SPEED, PLAYER_HEALTH, ENEMY_SPEED, ENEMY_DAMAGE, BULLET_SPEED)
from src.constants import SHOOT_EVENT, SPAWN_EVENT
from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy
from src.utils import load_image, get_path


def game(display: pygame.Surface, clock: pygame.time.Clock) -> None:
    asteroid_image = load_image('assets', 'images', 'asteroid.png', size=[164, 164])
    background_image = load_image('assets', 'images', 'background.png', size=DISPLAY_SIZE)
    player_image = load_image('assets', 'images', 'player.png', size=[96, 96])
    shot_image = load_image('assets', 'images', 'shot.png', size=[64, 64])

    coords = DISPLAY_SIZE[0] /2, DISPLAY_SIZE[1] -50
    player = Player(player_image, coords, PLAYER_SPEED, PLAYER_HEALTH)

    bullets = list()
    enemies = list()

    difficulty = 0
    pygame.time.set_timer(SPAWN_EVENT, 3000, 1)

    while player.health > 0:
        difficulty += clock.get_time()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                b = Bullet(shot_image, player.rect.midtop, BULLET_SPEED)
                bullets.append(b)
            elif event.type == SPAWN_EVENT:
                millis = max(750, round(2000 - difficulty / 70))
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)

                coords = [randint(50, DISPLAY_SIZE[0] - 50), -asteroid_image.height]
                speed = ENEMY_SPEED + difficulty / 35_000
                damage = round(ENEMY_DAMAGE + difficulty / 7000)
                e = Enemy(asteroid_image, coords, speed, damage)
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

        for b in bullets:
            for e in enemies:
                if b.collide_entity(e):
                    b.kill()
                    e.kill()

        for e in enemies:
            if e.collide_entity(player):
                player.get_damage(e.damage)
                e.kill()
        print(bullets)
        print(enemies)

        # render
        display.fill('black')
        display.blit(background_image, (0, 0))

        player.render(display)

        for b in bullets:
            b.render(display)

        for e in enemies:
            e.render(display)

        pygame.draw.rect(display, (100, 0, 0), [10, 10, HEALTH_BAR_WIDTH, 30])
        width = int(player.health / PLAYER_HEALTH * HEALTH_BAR_WIDTH)
        pygame.draw.rect(display, (255, 0, 0), [10, 10, width, 30])

        pygame.display.update()
        clock.tick(MAX_FPS)


def show_lose(display: pygame.Surface, clock: pygame.Clock) -> ...:
    running = True

    font = pygame.Font(get_path('assets', 'fonts', 'pixel.ttf'), 64)
    text = font.render('You lose!', True, (255, 50, 50))
    display.blit(text, text.get_rect(center=[DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2]))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False


def main() -> None:
    pygame.init()

    display = pygame.display.set_mode(DISPLAY_SIZE, flags=pygame.RESIZABLE | pygame.SCALED ,vsync=True)
    pygame.display.set_caption('Shooter')

    clock = pygame.time.Clock()

    while True:
        game(display, clock)
        show_lose(display, clock)


if __name__ == '__main__':
    main()

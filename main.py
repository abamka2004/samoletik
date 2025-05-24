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
    player_image1 = load_image('assets', 'images', 'player1.png', size=[96, 96])
    player_image2 = load_image('assets', 'images', 'player2.png', size=[96, 96])
    player_image3 = load_image('assets', 'images', 'player3.png', size=[96, 96])
    player_image4 = load_image('assets', 'images', 'player4.png', size=[96, 96])

    player_animation = [player_image, player_image1, player_image2, player_image3, player_image4]

    shot_image = load_image('assets', 'images', 'shot.png', size=[64, 64])

    shot_sound = pygame.Sound(get_path('assets', 'sounds', 'shot.wav'))
    death_sound = pygame.Sound(get_path('assets', 'sounds', 'death.wav'))
    explosion_sound = pygame.Sound(get_path('assets', 'sounds', 'explosion.wav')) 

    coords = DISPLAY_SIZE[0] /2, DISPLAY_SIZE[1] -70
    player = Player(player_animation, coords, PLAYER_SPEED, PLAYER_HEALTH)

    bullets = list()
    enemies = list()

    font = pygame.Font(get_path('assets', 'fonts', 'pixel.ttf'), 24)

    score = 0
    difficulty = 0
    pygame.time.set_timer(SPAWN_EVENT, 1800, 1)

    while player.health > 0:
        difficulty += clock.get_time()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                shot_sound.play()
                b = Bullet(shot_image, player.rect.midtop, BULLET_SPEED)
                bullets.append(b)
            elif event.type == SPAWN_EVENT:
                millis = max(750, round(2000 - difficulty / 70))
                pygame.time.set_timer(SPAWN_EVENT, millis, 1)

                new_asteroid_image = pygame.transform.rotozoom(asteroid_image, randint(0, 360), 1 + randint(-20, 80) / 100)
                coords = [randint(50, DISPLAY_SIZE[0] - 50), -new_asteroid_image.height]
                speed = ENEMY_SPEED + difficulty / 35_000
                damage = round(ENEMY_DAMAGE + difficulty / 7000)

                e = Enemy(new_asteroid_image, coords, speed, damage)
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
                    explosion_sound.play()
                    b.kill()
                    e.kill()
                    score += 1

        for e in enemies:
            if e.collide_entity(player):
                death_sound.play()
                player.get_damage(e.damage)
                e.kill()

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

        image_score = font.render(str(score), True, 'white')
        rect_score = image_score.get_rect(midtop=[player.rect.centerx, player.rect.bottom - 20])
        display.blit(image_score, rect_score)

        pygame.display.update()
        clock.tick(MAX_FPS)


def show_lose(display: pygame.Surface, clock: pygame.Clock) -> None:
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
    
    pygame.mixer.music.load(get_path('assets', 'music', 'background-1.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()

    while True:
        game(display, clock)
        show_lose(display, clock)


if __name__ == '__main__':
    main()

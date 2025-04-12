import pygame

from src.constants import MAX_FPS, DISPLAY_SIZE
from src.constants import SHOOT_EVENT
from src.player import Player


def game(display: pygame.Surface, clock: pygame.time.Clock) -> None:
    coords = DISPLAY_SIZE[0] /2, DISPLAY_SIZE[1] -50
    image = pygame.Surface((50, 50))
    image.fill((255, 0, 0))
    player = Player(image, coords, 4, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                print('1')


        player.update()


        display.fill((0,0,0))

        player.render(display)

        display.blit(display)
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

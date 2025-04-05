import pygame
from src.constants import MAX_FPS, DISPLAY_SIZE


def game(display: pygame.Surface, clock: pygame.time.Clock) -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        display.blit()
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

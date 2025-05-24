import pygame

# переменные для окна
MAX_FPS = 60
DISPLAY_SIZE = 800, 600

# события
SHOOT_EVENT = pygame.event.custom_type()
SPAWN_EVENT = pygame.event.custom_type()
ENEMY_SHOOT_EVENT = pygame.event.custom_type()

# переменные игрока
HEALTH_BAR_WIDTH = 150
PLAYER_HEALTH = 100
PLAYER_SPEED = 7.5

# переменные врага
ENEMY_DAMAGE = 10
ENEMY_SPEED = 5

SHOOT_ENEMY_DAMAGE = 15
SHOOT_ENEMY_SPEED = 1
SHOOT_ENEMY_INTERVAL = 0.75 # в секундах

# переменные для пули
BULLET_SPEED = 10

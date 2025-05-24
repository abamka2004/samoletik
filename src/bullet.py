from .constants import DISPLAY_SIZE
from .entity import Entity

class Bullet(Entity):
    def update(self):
        self.move(0, -self.speed)
        if self.rect.bottom <= 0:
            self.kill()


class EnemyBullet(Bullet):
    def update(self):
        self.move(0, self.speed)
        if self.rect.top >= DISPLAY_SIZE[1]:
            self.kill()

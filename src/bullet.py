from .entity import Entity

class Bullet(Entity):
    def update(self):
        self.move(0, -self.speed)
        if self.rect.bottom <= 0:
            self.kill()

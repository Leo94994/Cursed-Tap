from pygame.sprite import Sprite
import pygame as pg


class Portal(Sprite):
    def __init__(self, x, y, size, color):
        super(Portal, self).__init__()
        self.x = x
        self.y = y
        self.size = size
        self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)
        self.color = color
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


portal_in = Portal(1000, 640, 70, (110, 241, 255, 90))
portal_out = Portal(20, 20, 70, (255, 161, 65, 90))


portals = pg.sprite.Group()
portals.add(portal_in)
portals.add(portal_out)



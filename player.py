import pygame as pg
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.player_image = pg.image.load('img/player.png')
        self.rect = self.player_image.get_rect()
        self.speed = 1.11
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def draw(self):
        self.screen.blit(self.player_image, self.rect)

    def update(self):
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

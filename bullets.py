import pygame as pg
from pygame.sprite import Sprite
import attack


class Bullet(Sprite):
    def __init__(self, x, y, screen, attack, w=10, h=10):
        super(Bullet, self).__init__()
        self.screen_rect = screen.get_rect()
        self.w = w
        self.h = h
        self.color = (10, 200, 30)
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.speed_x = 0.3
        self.speed_y = 1.2
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.gap = 60
        self.attack = attack  # 'rain', 'calamitas'
        self.radius = 100
        self.temp = 1

    def update(self, screen):
        if self.attack == 'rain':
            attack.update_bullet_rain(self)
        if self.attack == 'calamitas_l' or self.attack == 'calamitas_r':
            attack.update_calamitas_attack(self)
        if self.attack == 'circle_l' or self.attack == 'circle_r':
            attack.update_bullet_circle_lr(self)
        if self.attack == 'circle_u' or self.attack == 'circle_d':
            attack.update_bullet_circle_diagonal(self)
        if self.attack == 'cage_u' or self.attack == 'cage_d' or self.attack == 'cage_l' or self.attack == 'cage_r':
            attack.update_cage_attack(self)
        # if self.attack == 'manyrods_y' or self.attack == 'manyrods_x':
        #     attack.update_manyrods_attack(self)

        self.rect.x = self.x
        self.rect.y = self.y

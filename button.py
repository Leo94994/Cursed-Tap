import pygame as pg
import consts
from consts import SFX_BUTTON_CLICK, RED_BTN_CLR, GREEN_BTN_CLR, update_sfx_volume


class Button:
    def __init__(self, x, y, w, h, text=('text', 20, (0, 0, 255)),
                 bgcolor=(120, 120, 120), lncolor=(255, 255, 255),
                 outline_width=2, border_radius=10):
        self.active = True
        self.pressed = False
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text[0]
        self.font_size = text[1]
        self.font_color = text[2]
        self.bgcolor = bgcolor
        self.default_bgcolor = self.bgcolor
        self.lncolor = lncolor
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.outline_width = outline_width
        self.border_radius = border_radius
        self.font = pg.font.Font(None, self.font_size)
        self.font_surf = self.font.render(self.text, True, self.font_color)
        self.font_rect = self.font_surf.get_rect()

    def draw(self, screen):
        pg.draw.rect(screen, self.bgcolor, self.rect, border_radius=10)
        pg.draw.rect(screen, self.lncolor, self.rect, self.outline_width, self.border_radius)
        screen.blit(self.font.render(self.text, True, self.font_color),
                    (self.x + self.w / 2 - self.font_rect.centerx,
                     self.y + self.h / 2 - self.font_rect.centery))

    def click(self):
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos) and pg.mouse.get_pressed()[0] and self.active:
            SFX_BUTTON_CLICK.play()
            return True
        else:
            return False

    def overlap(self):
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.active:
            self.bgcolor = (self.default_bgcolor[0] + 30 if self.bgcolor[0] <= 245 else self.bgcolor[0],
                            self.default_bgcolor[1] + 30 if self.bgcolor[1] <= 245 else self.bgcolor[1],
                            self.default_bgcolor[2] + 30 if self.bgcolor[2] <= 245 else self.bgcolor[2])
        else:
            self.bgcolor = self.default_bgcolor

    # Дальше функции для экземпляров

    def btn_all_sound_pressed(self, btn):
        consts.Music_volume = 0
        consts.sfx_volume = 0
        pg.mixer.music.stop()
        btn.pressed = True
        btn.default_bgcolor = RED_BTN_CLR
        btn.text = 'Off'
        update_sfx_volume()

    @staticmethod
    def btn_all_sound_unpressed(btn):
        consts.sfx_volume = consts.DEFAULT_SFX_VOLUME
        consts.Music_volume = consts.DEFAULT_MUSIC_VOLUME
        btn.pressed = False
        btn.default_bgcolor = GREEN_BTN_CLR
        btn.text = 'On'
        update_sfx_volume()

    @staticmethod
    def BTN_COLLISION_pressed(btn):
        consts.COLLISION = False
        btn.pressed = True
        btn.text = 'Collision: False'

    @staticmethod
    def BTN_COLLISION_unpressed(btn):
        consts.COLLISION = True
        btn.pressed = False
        btn.text = 'Collision: True'

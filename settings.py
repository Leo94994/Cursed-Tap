import pygame as pg
from consts import WIDTH, HEIGHT, GREEN_BTN_CLR, Music_volume
from button import Button
from slider import Slider


class Settings:
    def __init__(self):
        self.show_settings = False
        self.settings_rect_indent = 10
        self.settings_rect_color = (0, 0, 0)
        self.settings_rect_line_width = 3
        self.settings_rect = pg.Rect(self.settings_rect_indent, self.settings_rect_indent,
                                     WIDTH - self.settings_rect_indent * 2, HEIGHT - self.settings_rect_indent * 2)

        self.settings_rect_win_1 = pg.Rect(self.settings_rect_indent * 2, self.settings_rect_indent * 2,
                                           WIDTH / 2 - self.settings_rect_indent * 2,
                                           HEIGHT / 2 - self.settings_rect_indent * 2)
        self.settings_rect_win_2 = pg.Rect(self.settings_rect_indent + WIDTH / 2, self.settings_rect_indent * 2,
                                           WIDTH / 2 - self.settings_rect_indent * 3,
                                           HEIGHT / 2 - self.settings_rect_indent * 2)
        self.settings_rect_win_3 = pg.Rect(self.settings_rect_indent * 2, self.settings_rect_indent + HEIGHT / 2,
                                           WIDTH / 2 - self.settings_rect_indent * 2,
                                           HEIGHT / 2 - self.settings_rect_indent * 3)
        self.settings_rect_win_4 = pg.Rect(self.settings_rect_indent + WIDTH / 2,
                                           self.settings_rect_indent + HEIGHT / 2,
                                           WIDTH / 2 - self.settings_rect_indent * 2 - self.settings_rect_indent,
                                           HEIGHT / 2 - self.settings_rect_indent * 3)

        self.settings_font_color = (255, 255, 255)
        self.settings_font_size = 35
        self.settings_win1_title_font = pg.font.Font(None, self.settings_font_size)
        self.settings_win1_title_text = self.settings_win1_title_font.render('Музыка и звуки', True,
                                                                             self.settings_font_color)
        self.settings_win1_title_rect = self.settings_win1_title_text.get_rect()

    def open(self, mm):
        mm.main_menu_image = pg.transform.scale(pg.image.load('img/Без имени-1.jpg'), (WIDTH, HEIGHT))
        self.show_settings = True


    def update(self, screen):
        pg.draw.rect(screen, self.settings_rect_color, self.settings_rect,
                     self.settings_rect_line_width, border_radius=10)
        pg.draw.rect(screen, self.settings_rect_color, self.settings_rect_win_1,
                     self.settings_rect_line_width, border_radius=10)
        pg.draw.rect(screen, self.settings_rect_color, self.settings_rect_win_2,
                     self.settings_rect_line_width, border_radius=10)
        pg.draw.rect(screen, self.settings_rect_color, self.settings_rect_win_3,
                     self.settings_rect_line_width, border_radius=10)
        pg.draw.rect(screen, self.settings_rect_color, self.settings_rect_win_4,
                     self.settings_rect_line_width, border_radius=10)
        screen.blit(self.settings_win1_title_text, (self.settings_rect_win_1.centerx -
                                                    self.settings_win1_title_rect.centerx,
                                                    self.settings_rect_win_1.y + 10))
        btn_all_sound.draw(screen)
        btn_all_sound.overlap()
        btn_collision.draw(screen)
        btn_collision.overlap()
        sldr_music.draw(screen)
        sldr_music.update()


def load():
    try:
        with open('settings.txt', 'r') as settings_file:
            lines = settings_file.readlines()
            for line in lines:
                if 'btn_all_sound.pressed:' in line:
                    btn_all_sound.pressed = bool(True if 'True' in line else False)
                elif 'sldr_music:' in line:
                    sldr_music.val = float(line.replace('sldr_music: ', ''))
            if btn_all_sound.pressed:
                btn_all_sound.btn_all_sound_pressed(btn_all_sound)
            else:
                btn_all_sound.btn_all_sound_unpressed(btn_all_sound)
    except FileNotFoundError:
        with open('settings.txt', 'a') as settings_file:
            settings_file.write(f'btn_all_sound.pressed: {btn_all_sound.pressed}\n')
            settings_file.write(f'sldr_music: {sldr_music.val}')


def save():
    with open('settings.txt', 'w') as settings_file:
        settings_file.write(f'btn_all_sound.pressed: {str(btn_all_sound.pressed)}\n')
        settings_file.write(f'sldr_music: {str(sldr_music.val)}')


btn_all_sound = Button(490, 30, 40, 40, ('On', 25, 'black'), GREEN_BTN_CLR)
btn_collision = Button(100, 500, 150, 70, ('collision: True', 30, (255, 255, 255)))
sldr_music = Slider(35, 100, 300, 20, 50)

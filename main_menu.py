import pygame as pg

import consts
import controls
from consts import (WIDTH, HEIGHT, FPS, BG_COLOR, TIME_ATK_CIRCLE_LR, TIME_ATK_CAGE,
                    TIME_ATK_CALAMITAS, TIME_ATK_BULLET_RAIN, ATK_CAGE, ATK_CIRCLE_LR, ATK_BULLET_RAIN, ATK_CALAMITAS,
                    RED_BTN_CLR, GREEN_BTN_CLR, SFX_PLAY, SFX_BUTTON_CLICK)
from button import Button
import stats
import settings
from settings import Settings, btn_all_sound, btn_collision

stats.start()
pg.mixer.music.load('OST/main menu.mp3')


class MainMenu:
    def __init__(self):
        self.main_menu_font_size = 70
        self.main_menu_font = pg.font.Font(None, self.main_menu_font_size)
        self.main_menu_font_color = (140, 10, 20)
        self.main_menu_text = self.main_menu_font.render('Нажми любую клавишу чтобы начать!', True,
                                                         self.main_menu_font_color)
        self.main_menu_image = pg.transform.scale(pg.image.load('img/main_menu_image.jpg'), (WIDTH, HEIGHT))
        self.main_menu = True

    def open_main_menu(self, screen):
        pg.mixer.music.load('OST/main menu.mp3')
        pg.mixer.music.play(-1)
        pg.mixer_music.set_volume(consts.Music_volume)
        btn_settings = Button(1020, 10, 50, 50, ('O', 25, 'red'), (108, 79, 79))
        sttngs = Settings()
        settings.load()
        self.main_menu = True
        while self.main_menu:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    controls.exit_game()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if btn_settings.click():
                        sttngs.open(self)
                    elif btn_all_sound.click():
                        if not btn_all_sound.pressed:
                            btn_all_sound.btn_all_sound_pressed(btn_all_sound)
                        else:
                            btn_all_sound.btn_all_sound_unpressed(btn_all_sound)
                    elif btn_collision.click():
                        if not btn_collision.pressed:
                            btn_collision.BTN_COLLISION_pressed(btn_collision)
                        else:
                            btn_collision.BTN_COLLISION_unpressed(btn_collision)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        SFX_BUTTON_CLICK.play()
                        if sttngs.show_settings:
                            sttngs.show_settings = False
                            settings.save()
                            self.main_menu_image = pg.transform.scale(pg.image.load('img/main_menu_image.jpg'),
                                                                      (WIDTH, HEIGHT))
                        else:
                            controls.exit_game()
                    else:
                        if not sttngs.show_settings:
                            SFX_PLAY.play()
                            self.main_menu = False

            screen.blit(self.main_menu_image, (0, 0))

            if not sttngs.show_settings:
                screen.blit(self.main_menu_text, (WIDTH / 2 - self.main_menu_text.get_rect().centerx, HEIGHT / 2 + 100))
                btn_settings.draw(screen)
                btn_settings.overlap()
            else:
                sttngs.update(screen)
            pg.display.flip()


if __name__ == '__main__':
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    mm = MainMenu()
    mm.open_main_menu(screen)

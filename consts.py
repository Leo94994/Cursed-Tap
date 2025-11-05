import pygame as pg



pg.init()

JOIN_TO_MAIN_MENU = True
COLLISION = True
DEBUG_MODE = True
WIDTH = 1080
HEIGHT = 720
FPS = 240
BG_COLOR = (0, 0, 0)

DEFAULT_MUSIC_VOLUME = 0.1
DEFAULT_SFX_VOLUME = 0.2
sfx_volume = DEFAULT_SFX_VOLUME
Music_volume = DEFAULT_MUSIC_VOLUME

SFX_DEATH = pg.mixer.Sound('SFX/death.mp3')
SFX_PLAY = pg.mixer.Sound('SFX/play.mp3')
SFX_TOMENU = pg.mixer.Sound('SFX/tomenu.mp3')
SFX_BUTTON_CLICK = pg.mixer.Sound('SFX/button click.mp3')
SFX_SLIDER = pg.mixer.Sound('SFX/slider.mp3')


def update_sfx_volume():
    SFX_DEATH.set_volume(sfx_volume)
    SFX_PLAY.set_volume(sfx_volume)
    SFX_TOMENU.set_volume(sfx_volume)
    SFX_BUTTON_CLICK.set_volume(sfx_volume)
    SFX_SLIDER.set_volume(sfx_volume)


RED_BTN_CLR = (200, 30, 20)
GREEN_BTN_CLR = (20, 200, 30)

# tap_bg_anim = [pg.image.load('animations/tap_bg/anim_0.jpg'),
#                pg.image.load('animations/tap_bg/anim_1.jpg'),
#                pg.image.load('animations/tap_bg/anim_2.jpg')]

ATK_BULLET_RAIN = pg.USEREVENT + 1
ATK_CALAMITAS = pg.USEREVENT + 2
ATK_CIRCLE_LR = pg.USEREVENT + 4
ATK_CIRCLE_DIAGONAL = pg.USEREVENT + 6
ATK_CAGE = pg.USEREVENT + 5
ATK_MANYRODS = pg.USEREVENT + 7

TIME_ATK_BULLET_RAIN = 1
# 1
TIME_ATK_CALAMITAS = 6500
# 6_500
TIME_ATK_CAGE = 19_000
# 19_000
TIME_ATK_CIRCLE_LR = 27_000
# 27_000
TIME_ATK_CIRCLE_DIAGONAL = 30_500
# 30_500
TIME_ATK_MANYRODS = 1
# 34_000

update_sfx_volume()

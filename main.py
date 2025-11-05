import attack
import consts


def run():
    import controls
    from bullets import Bullet
    import pygame as pg
    from player import Player
    from pygame.sprite import Group
    from consts import (WIDTH, HEIGHT, FPS, BG_COLOR, TIME_ATK_CIRCLE_LR, TIME_ATK_CAGE,
                        TIME_ATK_CALAMITAS, TIME_ATK_BULLET_RAIN, ATK_CAGE, ATK_CIRCLE_LR, ATK_BULLET_RAIN,
                        ATK_CALAMITAS, DEBUG_MODE, COLLISION, ATK_CIRCLE_DIAGONAL, TIME_ATK_CIRCLE_DIAGONAL,
                        ATK_MANYRODS, TIME_ATK_MANYRODS,)
    from main_menu import MainMenu
    import stats
    import time
    import debug

    clock = pg.time.Clock()
    pg.init()
    screen_image = pg.transform.scale(pg.image.load('img/душ.jpg'), (WIDTH, HEIGHT))
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Cursed Tap is here.')

    player = Player(screen)
    bullet = Bullet(0, 0, screen, 'rain')
    bullets = Group()
    mm = MainMenu()

    if consts.JOIN_TO_MAIN_MENU:
        mm.open_main_menu(screen)

    from consts import Music_volume
    consts.update_sfx_volume()
    pg.mixer.music.load('OST/Iron Oxide.mp3')
    pg.mixer.music.set_volume(Music_volume)
    pg.mixer.music.play()

    # АТАКИ
    pg.time.set_timer(ATK_BULLET_RAIN, TIME_ATK_BULLET_RAIN, 1)
    pg.time.set_timer(ATK_CALAMITAS, TIME_ATK_CALAMITAS, 2)
    pg.time.set_timer(ATK_CAGE, TIME_ATK_CAGE, 1)
    pg.time.set_timer(ATK_CIRCLE_LR, TIME_ATK_CIRCLE_LR, 1)
    pg.time.set_timer(ATK_CIRCLE_DIAGONAL, TIME_ATK_CIRCLE_DIAGONAL, 1)
    # # pg.time.set_timer(pg.USEREVENT + 6666, 20100)  # FORCE KILL PLAYER

    pg.time.set_timer(ATK_MANYRODS, TIME_ATK_MANYRODS, 1)
    pg.mixer_music.set_pos(0)

    run_game = True
    start_time = time.time()
    while run_game:
        game_time = time.time() - start_time
        screen.fill(BG_COLOR)
        # screen.blit(screen_image, (0, 0))
        controls.update(screen, player, bullet, bullets, game_time)
        if DEBUG_MODE:
            debug.debug(screen, bullets)
            debug.debug(screen, f'ticks: {pg.time.get_ticks()}', y=25)
            debug.debug(screen, f'attempt: {stats.attempts_session}', y=50)
            debug.debug(screen, f'all attempts: {int(stats.attempts_all)}', y=75)
            debug.debug(screen, f'COLLISION: {consts.COLLISION}', y=100)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    run()

# _______________MAIN_MENU___________________________________
# !!!! Исправить баг с загрузкой позиции головки слайдера из файла настроек !!!!
# Настройки
# Кнопка выключения звуков - сделать так, чтобы музыка не начиналась с начала
# Сделать кнопку настроек по умолчанию
# Сделать кнопку выхода из настроек
# Сделать кнопку на клавиатуре захода в настройки из игры
# Сделать кнопку паузы на клаве
# Сделать так чтобы можно было начинать игру мышкой
# Выводить статистику где-нибудь(в гл меню)
# режим практики
# Пофиксить все что связяно с перетаскиванием окна
# SFX Выхода из игры, SFX слайдера
# атака лабиринт
# шипы по краям
# Из большого куба разлетаются маленькие

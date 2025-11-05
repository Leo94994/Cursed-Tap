import pygame as pg
import main
import sys

import consts
from consts import (WIDTH, HEIGHT, FPS, BG_COLOR, TIME_ATK_CIRCLE_LR, TIME_ATK_CAGE,
                    TIME_ATK_CALAMITAS, TIME_ATK_BULLET_RAIN, ATK_CAGE, ATK_CIRCLE_LR, ATK_BULLET_RAIN, ATK_CALAMITAS,
                    DEBUG_MODE, SFX_TOMENU, SFX_DEATH, COLLISION, ATK_CIRCLE_DIAGONAL, TIME_ATK_CIRCLE_DIAGONAL,
                    ATK_MANYRODS, TIME_ATK_MANYRODS)
import attack
import stats
import settings


def exit_game():
    stats.on_exit()
    settings.save()
    sys.exit()


def events(player, bullet, screen, bullets,  game_time):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                stats.attempts_session += 1
                main.join_to_main_menu = True
                SFX_TOMENU.play()
                main.run()
            elif event.key == pg.K_a or event.key == pg.K_LEFT:  # ВЛЕВО
                player.move_left = True
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:  # ВПРАВО
                player.move_right = True
            elif event.key == pg.K_w or event.key == pg.K_UP:  # ВВЕРХ
                player.move_up = True
            elif event.key == pg.K_s or event.key == pg.K_DOWN:  # ВНИЗ
                player.move_down = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_LEFT:  # ВЛЕВО
                player.move_left = False
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:  # ВПРАВО
                player.move_right = False
            elif event.key == pg.K_w or event.key == pg.K_UP:  # ВВЕРХ
                player.move_up = False
            elif event.key == pg.K_s or event.key == pg.K_DOWN:  # ВНИЗ
                player.move_down = False

        elif event.type == ATK_BULLET_RAIN:                   # RAIN
            attack.create_bullet_rain(screen, bullet, bullets)
        elif event.type == ATK_CALAMITAS:                     # CALAMITAS
            attack.create_calamitas_attack(screen, bullets)
        elif event.type == ATK_CIRCLE_LR:                        # CIRCLE_LR
            pg.time.set_timer((pg.USEREVENT + 101), 200, 8)
        elif event.type == ATK_CIRCLE_DIAGONAL:                  # CIRCLE_DIAGONAL
            pg.time.set_timer((pg.USEREVENT + 103), 150, 8)
        elif event.type == ATK_CAGE:                                 # CAGE
            pg.time.set_timer(pg.USEREVENT + 102, 1000, 4)
        elif event.type == ATK_MANYRODS:                            # MANYRODS
            pg.time.set_timer(pg.USEREVENT + 104, 1, 50)

        elif event.type == pg.USEREVENT + 101:
            if game_time >= TIME_ATK_CIRCLE_LR / 1000:
                attack.create_bullet_circle_lr(screen, bullets)
        elif event.type == pg.USEREVENT + 103:
            if game_time >= TIME_ATK_CIRCLE_DIAGONAL / 1000:
                attack.create_bullet_circle_diagonal(screen, bullets)
        elif event.type == pg.USEREVENT + 102:
            if game_time >= TIME_ATK_CAGE / 1000:
                attack.create_cage_attack(screen, bullets)
        elif event.type == pg.USEREVENT + 104:
            if game_time >= TIME_ATK_MANYRODS / 1000:
                # attack.create_manyrods_attack(screen, bullets)
                pass
        elif event.type == pg.USEREVENT + 6666:  # FORCE KILL PLAYER
            collide(bullets)


def collide(bullets):
    SFX_DEATH.play()
    stats.attempts_session += 1
    pg.mixer.music.stop()
    # pg.time.delay(500)
    bullets.empty()
    main.join_to_main_menu = False
    main.run()


def update(screen, player, bullet, bullets,  game_time):
    events(player, bullet, screen, bullets,  game_time)
    bullets.update(screen)
    bullets.draw(screen)
    player.update()
    player.draw()

    # КОЛЛИЗИЯ
    if pg.sprite.spritecollideany(player, bullets) and consts.COLLISION:
        collide(bullets)



import pygame as pg

pg.init()
font = pg.font.Font(None, 25)


def debug(screen, info, x=10, y=0):
    surf = font.render(str(info), True, 'red')
    screen.blit(surf, (x, y))


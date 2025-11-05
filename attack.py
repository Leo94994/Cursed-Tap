import random

import pygame as pg

import portal
from consts import WIDTH, HEIGHT
from bullets import Bullet
from random import randint
from math import sin, cos
import time
from portal import portal_in, portal_out, portals


def create_bullet_rain(screen, bullet, bullets):
    for y in range(-1500 + randint(0, 10), 0, 70):
        for x in range(100 + randint(-10, 10), 2200, 70):
            bullet = Bullet(x, y, screen, 'rain')
            bullet.speed_x = 0.6
            bullet.speed_y = 1.2
            bullets.add(bullet)


def update_bullet_rain(bullet):
    if bullet.attack == 'rain':
        if bullet.y < HEIGHT:
            bullet.y += bullet.speed_y
            bullet.x -= bullet.speed_x
        else:
            bullet.kill()


def create_calamitas_attack(screen, bullets):
    count_of_billets = 70
    for _ in range(count_of_billets):
        bullet = Bullet(randint(0, WIDTH) - 1100, randint(0, HEIGHT), screen, 'calamitas_l')
        bullet.speed_x = 1.2
        bullets.add(bullet)
    for _ in range(count_of_billets):
        bullet = Bullet(randint(0, WIDTH) + 1100, randint(0, HEIGHT), screen, 'calamitas_r')
        bullet.speed_x = 1.2
        bullets.add(bullet)


def update_calamitas_attack(bullet):
    if bullet.attack == 'calamitas_l' and not bullet.x > WIDTH + 1100:
        bullet.x += bullet.speed_x
        if not bullet.speed_x <= 0.7:
            bullet.speed_x -= 0.0005
        if bullet.x > WIDTH / 3 * 2:
            bullet.speed_x += 0.005
    elif bullet.attack == 'calamitas_r' and not bullet.x < -1100:
        bullet.x -= bullet.speed_x
        if not bullet.speed_x <= 0.7:
            bullet.speed_x -= 0.0005
        if bullet.x < WIDTH / 3:
            bullet.speed_x += 0.005
    else:
        bullet.kill()


def create_bullet_circle_lr(screen, bullets):
    def create_ex(bullet):
        bullet.speed_x = q
        bullet.speed_y = q
        bullet.gap = 50
        bullet.radius = 10
        bullets.add(bullet)
    for q in range(1, 45):  # 45 Это идеальное число, не трогай!
        create_ex(bullet=Bullet(0, 0, screen, 'circle_l'))
        create_ex(bullet=Bullet(0, 0, screen, 'circle_r'))


def update_bullet_circle_lr(bullet):
    # print(bullet.x, bullet.y)
    if bullet.attack == 'circle_l':
        bullet.x = bullet.radius * cos(bullet.speed_x)
        bullet.y = bullet.radius * sin(bullet.speed_y) + HEIGHT / 2
    elif bullet.attack == 'circle_r':
        bullet.x = bullet.radius * cos(bullet.speed_x) + WIDTH
        bullet.y = bullet.radius * sin(bullet.speed_y) + HEIGHT / 2
    bullet.speed_x += 0.001
    bullet.speed_y += 0.001
    bullet.radius += 1

    if bullet.x > WIDTH+bullet.gap or bullet.x < -bullet.gap or bullet.y > HEIGHT+bullet.gap or bullet.y < -bullet.gap:
        bullet.kill()

def create_bullet_circle_diagonal(screen, bullets):
    def create_ex(bullet):
        bullet.speed_x = q
        bullet.speed_y = q
        bullet.gap = 200
        bullet.radius = 10
        bullets.add(bullet)
    for q in range(1, 45):  # 45 Это идеальное число, не трогай!
        create_ex(bullet=Bullet(0, 0, screen, 'circle_u'))
        create_ex(bullet=Bullet(0, 0, screen, 'circle_d'))


def update_bullet_circle_diagonal(bullet):
    # print(bullet.x, bullet.y)
    if bullet.attack == 'circle_u':
        bullet.x = bullet.radius * cos(bullet.speed_x)
        bullet.y = bullet.radius * sin(bullet.speed_y)
    elif bullet.attack == 'circle_d':
        bullet.x = bullet.radius * cos(bullet.speed_x) + WIDTH
        bullet.y = bullet.radius * sin(bullet.speed_y) + HEIGHT
    bullet.speed_x += 0.001
    bullet.speed_y += 0.001
    bullet.radius += 1.4

    if bullet.x > WIDTH+bullet.gap or bullet.x < -bullet.gap or bullet.y > HEIGHT+bullet.gap or bullet.y < -bullet.gap:
        bullet.kill()


def create_cage_attack(screen, bullets):
    def set_args(bullet):
        bullet.speed_x = 1
        bullet.speed_y = 0.75
        bullets.add(bullet)
    offset = randint(0, 50)
    gap = 50
    count_on_width = round(WIDTH / 2 / gap)
    count_on_height = round(HEIGHT / 2 / gap)
    leghth = 100
    for i in range(count_on_width):
        bullet = Bullet(i*gap+offset, -leghth, screen, 'cage_u', w=2, h=leghth)
        set_args(bullet)
    for i in range(count_on_width):
        bullet = Bullet(i * gap + count_on_width*gap + offset, HEIGHT, screen, 'cage_d', w=2, h=leghth)
        set_args(bullet)
    for i in range(count_on_height):
        bullet = Bullet(-leghth, i * gap + offset, screen, 'cage_l', w=leghth, h=2)
        set_args(bullet)
    for i in range(count_on_height+1):
        bullet = Bullet(WIDTH, i * gap + count_on_height*gap + offset, screen, 'cage_r', w=leghth, h=2)
        set_args(bullet)


def update_cage_attack(bullet):
    if bullet.attack == 'cage_l' and bullet.x < WIDTH:
        bullet.x += bullet.speed_x
    elif bullet.attack == 'cage_r' and bullet.rect.right > 0:
        bullet.x -= bullet.speed_x
    elif bullet.attack == 'cage_u' and bullet.y < HEIGHT:
        bullet.y += bullet.speed_y
    elif bullet.attack == 'cage_d' and bullet.rect.bottom > 0:
        bullet.y -= bullet.speed_y
    else:
        bullet.kill()


# def create_manyrods_attack(screen, bullets):
#
#     def set_args_ud(bullet):
#         bullet.y = -bullet.h
#         bullet.speed_y = 0.5
#         bullets.add(bullet)
#         possible_x_coords = [0]
#         x_coords = []
#         coord_x = 0
#         temp = 0
#         while coord_x <= WIDTH:
#             coord_x += bullet.w
#             possible_x_coords.append(coord_x)
#             temp += 1
#         x_coords.append(random.choice(possible_x_coords))
#         bullet.x = x_coords[temp]
#
#
#     # def set_args_x(bullet):
#     #     bullet.x = -bullet.w
#     #     bullet.speed_x = 0.5
#     #     bullets.add(bullet)
#
#
#     # set_args_x(bullet=Bullet(0, 0, screen, 'manyrods_x', w=800, h=5))
#     set_args_ud(bullet=Bullet(0, 0, screen, 'manyrods_y', h=800, w=5))
#
#
# def update_manyrods_attack(bullet):
#     if bullet.attack == 'manyrods_y' and bullet.y < HEIGHT + 10:
#         bullet.y += bullet.speed_y
#         bullet.speed_y *= 1.01
#     elif bullet.attack == 'manyrods_x' and bullet.x < WIDTH + 10:
#         bullet.x += bullet.speed_x
#         bullet.speed_x *= 1.01
#     else:
#         bullet.kill()

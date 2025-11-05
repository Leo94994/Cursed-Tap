import pygame as pg

session = True

attempts_session = 0
attempts_all = 0
time_in_game = 0


def start():
    global attempts_all
    global time_in_game
    try:
        with open('stats.txt', 'r') as stats_file:
            lines = stats_file.readlines()
            for line in lines:
                if 'attempts_all:' in line:
                    attempts_all = int(''.join(x for x in line if x.isdigit()))
                elif 'time_in_game (ms):' in line:
                    time_in_game = int(''.join(x for x in line if x.isdigit()))
    except FileNotFoundError:
        with open('stats.txt', 'a') as stats_file:
            stats_file.writelines(f'attempts_all: 0\n')
            stats_file.write(f'time_in_game: 0\n')


def calculate_h_m_s_ms(time) -> str:
    h = time // 1000 // 60 // 60
    m = time // 1000 // 60 % 60
    s = time // 1000 % 60
    ms = time % 1000
    return f'{h}:{m}:{s}.{ms}'


def on_exit():
    new_attempt_all = attempts_all + attempts_session
    new_time_in_game = time_in_game + pg.time.get_ticks()
    with open('stats.txt', 'w') as stats_file:
        stats_file.write(f'attempts_all: {new_attempt_all}\n')
        stats_file.write(f'time_in_game (ms): {new_time_in_game}\n')
        stats_file.write(f'time_in_game (h:m:s.ms): {calculate_h_m_s_ms(new_time_in_game)}')


# print(time_in_game)
# print(attempts_all)


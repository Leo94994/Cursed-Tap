import pygame as pg
from consts import WIDTH, HEIGHT
import sys

rows = ['_____________Выдумщики_____________',
        'Гейм-дизайнер              Leo94994',
        'Продюсер                   Leo94994',
        'Сценарист                  Leo94994 / LoLDeath',
        'Генератор идей             Leo94994 / Love_your_ma / LoLDead',
        '________________Рабы_______________',
        'Программист                Leo94994',
        'Тестировщик                Leo94994 / Love_your_ma / LoLDeath',
        'Математики                  Leo94994 / Tankist_IMD1008',
        '_____________Музыканты_____________',
        'Вокалист                   Leo94994',
        'Звукорежессер              Leo94994',
        '_______________Художники____________',
        'Художник спрайтов          Leo94994 / LoLDeath',
        'Художник задних фонов      Leo94994',
        'Художник главного меню     LoLDeath',
        'Аниматор                   Leo94994']


class Credits:
    def __init__(self):
        self.font_size = 32
        self.font = pg.font.Font(None, self.font_size)
        self.font_color = (127, 255, 212)
        self.text = self.font.render('Гейм-дизайнер              Leo94994', False, self.font_color)
        self.rect = self.text.get_rect()
        self.credits = True
        self.speed = 0.03
        self.y = 0

    def draw_text(self, y):
        for row in range(len(rows)):
            self.text = self.font.render(rows[row], False, self.font_color)
            screen.blit(self.text, (WIDTH / 2 - self.rect.w / 2, 100 * row + y + 720))

    def update(self):
        cr.draw_text(self.y)
        self.y -= cr.speed


pg.init()
screen_image = pg.transform.scale(pg.image.load('img/Tube.png'), (WIDTH, HEIGHT))
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Cursed Tap is here.')
bg_color = (0, 0, 10)

cr = Credits()

pg.mixer.music.load('OST/credits song.mp3')
pg.mixer.music.play()
pg.mixer_music.set_volume(0.1)
credits = True

while credits:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    screen.fill(bg_color)
    cr.update()
    pg.display.flip()

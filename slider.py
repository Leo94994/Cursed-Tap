import pygame as pg
from consts import WIDTH, HEIGHT, SFX_SLIDER
import controls


class Slider:
    def __init__(self, x, y, w, h, init_val):
        self.counter = True
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mw = self.w / 15
        self.init_val = self.x + self.w / 100 * init_val - self.mw / 2
        self.val = init_val
        self.static_rect_color = (0, 0, 0)
        self.moving_rect_color = (255, 0, 0)
        self.static_rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.moving_rect = pg.Rect(self.init_val, self.y, self.mw, self.h)
        self.counter_x = self.x + self.w + 10
        self.counter_y = self.y
        self.font = pg.font.Font(None, 30)
        self.font_color = (255, 0, 0)
        self.font_bgcolor = (0, 0, 0)
        self.counter_text = self.font.render(str(int(self.val)), True, self.font_color, self.font_bgcolor)
        self.counter_rect = self.counter_text.get_rect()

    def draw(self, screen):
        pg.draw.rect(screen, self.static_rect_color, self.static_rect)
        pg.draw.rect(screen, self.moving_rect_color, self.moving_rect)
        if self.counter:
            self.counter_text = self.font.render(str(int(self.val)), True, self.font_color, self.font_bgcolor)
            screen.blit(self.counter_text, (self.counter_x, self.counter_y))

    def update(self):
        temp = 0
        mouse_pos = pg.mouse.get_pos()
        mouse_btn = pg.mouse.get_pressed()[0]
        if self.static_rect.collidepoint(mouse_pos):
            if mouse_btn:
                self.moving_rect.centerx = mouse_pos[0]
                self.val = (mouse_pos[0] - self.x) / self.w * 100
                if self.val > 99:
                    self.val = 100
                elif self.val < 1:
                    self.val = 0
        self.init_val = self.val


def run():
    sldr = Slider(100, 100, 300, 20, 50)
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    while True:
        print(sldr.val, sldr.init_val)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                controls.exit_game()
        screen.fill((200, 200, 255))
        sldr.draw(screen)
        sldr.update()
        pg.display.flip()


if __name__ == '__main__':
    run()

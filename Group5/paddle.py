import pygame as pg
from settings import paddle_height, paddle_width


class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = paddle_width
        self.height = paddle_height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = pg.Color("white")

    def appear(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def move_right(self):
        if self.rect.x + self.width <= 550:
            self.rect.x += 2

    def move_left(self):
        if self.rect.x >= 0:
            self.rect.x -= 2
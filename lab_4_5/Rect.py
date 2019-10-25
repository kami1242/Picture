from tkinter import *
from random import randrange as rnd, choice
import math
import time

class Rect:
    def __init__(self, canv):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.a = rnd(30, 50)
        self.vx = rnd(30) - 15
        self.vy = rnd(30) - 15
        self.rect = canv.create_rectangle(self.x, self.y, self.x + self.a, self.y + self.a, fill = 'black')
    def update(self, canv):
        self.vx += rnd(30) - 15 - (self.x - 400)*abs((self.x - 400))*0.0002 - 0.2*self.vx
        self.vy += rnd(30) - 15 - (self.y - 300)*abs((self.y - 300))*0.0002 - 0.2*self.vy
        self.x += self.vx
        self.y += self.vy
        canv.move(self.rect, self.vx, self.vy)

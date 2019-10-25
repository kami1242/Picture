from tkinter import *
from random import randrange as rnd, choice
import math
import time

class Ball:
    def __init__(self, canv):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.vx = rnd(10) - 5
        self.vy = rnd(10) - 5
        self.color = choice(['red', 'orange', 'yellow', 'green', 'blue'])
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width=0)
    def update(self, canv):
        if self.x + self.r > 750:
            self.vx = -abs(self.vx)
        if self.x - self.r < 50:
            self.vx = abs(self.vx)
        if self.y + self.r> 550:
            self.vy = -abs(self.vy)
        if self.y - self.r< 50:
            self.vy = abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.circle, self.vx, self.vy)

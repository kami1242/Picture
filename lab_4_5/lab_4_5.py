from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
points = 0 #user's points
n = 5 #number of the balls
balls = []
rects = []

class Ball:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.vx = rnd(10) - 5
        self.vy = rnd(10) - 5
        self.color = choice(['red', 'orange', 'yellow', 'green', 'blue'])
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width=0)
    def update(self):
        global canv
        if self.x > 700:
            self.vx = -abs(self.vx)
        if self.x < 100:
            self.vx = abs(self.vx)
        if self.y > 500:
            self.vy = -abs(self.vy)
        if self.y < 100:
            self.vy = abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.circle, self.vx, self.vy)

class Rect:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.a = rnd(30, 50)
        self.vx = rnd(30) - 15
        self.vy = rnd(30) - 15
        self.rect = canv.create_rectangle(self.x, self.y, self.x + self.a, self.y + self.a, fill = 'black')
    def update(self):
        global canv
        self.vx += rnd(30) - 15 - (self.x - 400)*abs((self.x - 400))*0.0002 - 0.2*self.vx
        self.vy += rnd(30) - 15 - (self.y - 300)*abs((self.y - 300))*0.0002 - 0.2*self.vy
        self.x += self.vx
        self.y += self.vy
        canv.move(self.rect, self.vx, self.vy)

def dist(x1, y1, x2, y2): #returns distance between two points
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def new_ball():
    balls.append(Ball())

def new_rect():
    rects.append(Rect())

def update():
    for b in balls:
        b.update()
    for r in rects:
        r.update()
    root.after(100, update)

def click(event):
    global points
    global canv
    for b in balls:
        if dist(event.x, event.y, b.x, b.y) < b.r:
            points += 1
            canv.delete(b.circle)
            balls.remove(b)
            new_ball()
    for r in rects:
        if (event.x > r.x) and (event.x < r.x + r.a) and (event.y > r.y) and (event.y < r.y + r.a):
            points += 5
            canv.delete(r.rect)
            rects.remove(r)
            new_rect()
    print(points)

new_ball()
new_ball()
new_rect()
new_rect()
print(rects)
    
update()
canv.bind('<Button-1>', click)

root.mainloop()

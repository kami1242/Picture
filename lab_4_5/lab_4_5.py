from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
points = 0 #user's points
n = 5 #number of the balls
balls = []

class Ball:
    def __init__(self):
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.vx = rnd(10) - 5
        self.vy = rnd(10) - 5
        self.color = choice(['red','orange','yellow','green','blue'])
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width=0)
    def update(self):
        global canv
        if self.x > 700:
            self.vx = -abs(self.vx)
        if self.x < 100:
            self.vx = abs(self.vx)
        if self.y > 500:
            self.vy = -abs(self.vy)
        if self.x < 100:
            self.vy = abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.circle, self.vx, self.vy)

def dist(x1, y1, z1, x2): #returns distance between two points
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def new_ball():
    balls.append(Ball())
    #canv.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=0)

def update():
    for b in balls:
        b.update()
    root.after(100, update)

def click(event):
    print()

new_ball()
new_ball()
update()
canv.bind('<Button-1>', click)

root.mainloop()

from graph import *
import math

def background():
    penColor(0, 200, 0)
    brushColor(0, 200, 0)
    rectangle(0, 200, 500, 400)
    penColor(200, 200, 255)
    brushColor(200, 200, 255)
    rectangle(0, 0, 500, 200)
    
def house(x, y, size):
    penColor("black")
    brushColor(200, 100, 100)
    polygon([(x, y), (x + size, y), (x + size/2, y - size/2), (x, y)])
    brushColor("brown")
    rectangle(x, y, x + size, y + size*2/3)
    penColor(255, 100, 100)
    brushColor(100, 200, 200)
    rectangle(x + size/3, y + size/4, x + size*2/3, y + size/2)

def cloud(x, y, r):
    penColor("black")
    brushColor("white")
    circle(x, y, r)
    circle(x + r, y, r)
    circle(x + 2*r, y, r)
    circle(x + 3*r, y, r)
    circle(x + 2*r, y - r, r)
    circle(x + r, y - r, r)

def tree(x, y, r):
    penColor("black")
    brushColor("black")
    rectangle(x - r/5, y, x + r/5, y + 3*r)
    brushColor("green")
    circle(x, y - 2.5*r, r)
    circle(x - r, y - 2*r, r)
    circle(x + r, y - 2*r, r)
    circle(x, y - r, r)
    circle(x - 0.8*r, y - 0.5*r, r)
    circle(x + 0.8*r, y - 0.3*r, r)

def sun(x, y, r):
    penColor("black")
    brushColor("pink")
    points = []
    phi = 2*math.pi/20
    for i in range(20):
        points.append((x + r * math.cos(phi*i), y + r * math.sin(phi*i)))
        points.append((x + 0.9 * r * math.cos(phi*(i+0.5)),
                       y + 0.9 * r * math.sin(phi*(i+0.5))))
    polygon(points)

windowSize(500, 400)

background()
house(50, 190, 120)
cloud(150, 100, 25)
tree(350, 180, 25)
sun(450, 50, 30)

run()

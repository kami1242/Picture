from graph import *
import math

def ellipse(xc, yc, a, b):
    #xc, yc - coords of the center, a, b - semimajor axises
    changeCoords(circle(0, 0, 10), [(xc - a, yc - b), (xc + a, yc + b)])

def car(x, y, w, h): #x, y - coords of the corner, w - width, h - height
    #exhaust pipe
    penColor("black")
    brushColor("black")
    ellipse(x + 0, y + h*40/60, w*20/180, h*5/60)

    #body
    penColor(100, 100, 250)
    brushColor(100, 100, 250)
    rectangle(x + w*30/180, y + 0, x + w*100/180, y + h*20/60)
    rectangle(x + 0, y + h*20/60, x + w*180/180, y + h*50/60)
    penColor("white")
    brushColor("white")
    rectangle(x + w*35/180, y + h*5/60, x + w*60/180, y + h*20/60)
    rectangle(x + w*70/180, y + h*5/60, x + w*95/180, y + h*20/60)

    #wheels
    penColor("black")
    brushColor("black")
    ellipse(x + w*40/180, y + h*50/60, w*20/180, h*15/60)
    ellipse(x + w*140/180, y + h*50/60, w*20/180, h*15/60)

def background(x, y, w, h):
    #general background
    penColor(100, 100, 100)
    brushColor(100, 100, 100)
    rectangle(x, y, x + w, y + h)

    penSize(5)
    penColor("white")
    brushColor(150, 150, 150)
    rectangle(x, y, x + w, y + h*9/15)
    penSize(1)

    penColor(190, 190, 190)
    brushColor(190, 190, 190)
    ellipse(x + w*7/9, y + h*15/15, w, h/5)

    #buildings and clouds
    penColor(200, 200, 200)
    brushColor(200, 200, 200)
    rectangle(x + w*6/9, y + h*1/15, x + w*8/9, y + h*10/15)

    penColor(190, 190, 190)
    brushColor(190, 190, 190)
    ellipse(x + w*6/9, y + h*3/15, w/2, h/10)

    penColor(180, 180, 180)
    brushColor(180, 180, 180)
    ellipse(x + w*2/9, y + h*4/15, w/2, h/10)

    penColor(130, 150, 130)
    brushColor(130, 150, 130)
    rectangle(x + w*3/9, y + h*2/15, x + w*5/9, y + h*10/15)

    penColor(130, 130, 150)
    brushColor(130, 130, 150)
    rectangle(x + w*0.5/9, y + h*0.5/15, x + w*2.5/9, y + h*9.5/15)

    penColor(100, 100, 100)
    brushColor(100, 100, 100)
    rectangle(x + w*3/9, y + h*2/15, x + w*5/9, y + h*10/15)

    penColor(160, 160, 160)
    brushColor(160, 160, 160)
    rectangle(x + w*2/9, y + h*4/15, x + w*4/9, y + h*11/15)

    #fumes
    penColor(170, 170, 170)
    brushColor(170, 170, 170)
    ellipse(x + w*3/9, y + h*13/15, w/10, h/50)
    
    penColor(170, 170, 170)
    brushColor(170, 170, 170)
    ellipse(x + w*3/9, y + h*12/15, w/10, h/50)

    penColor(170, 170, 170)
    brushColor(170, 170, 170)
    ellipse(x, y + h*11.5/15, w/10, h/50)
    

windowSize(300, 500)

background(0, 0, 300, 500)
car(150, 420, 120, 40)

run()

from tkinter import *
from random import randrange as rnd, choice
import math
import time
from Ball import *
from Rect import *

username = ''
points = 0 #user's points
n = 5 #number of the balls
balls = []  
rects = []

def dist(x1, y1, x2, y2): #returns distance between two points
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def savescore():
    global username
    global points
    scoretable = {}

    file = open('scores', 'r')
    for line in file:
        fields = line.split()
        scoretable[fields[0]] = int(fields[1])
    file.close()

    print(scoretable)

    if username in scoretable:
        if points > scoretable[username]:
            scoretable[username] = points
    else:
        scoretable[username] = points

    print(scoretable)

    printer = open('scores', 'w')
    for name in scoretable:
        printer.write(name + ' ' + str(scoretable[name]) + '\n')
    printer.close()

def new_ball():
    global canv
    balls.append(Ball(canv))

def new_rect():
    global canv
    rects.append(Rect(canv))

def update():
    global canv
    global scorelabel
    global points
    global username
    for b in balls:
        b.update(canv)
    for r in rects:
        r.update(canv)
    scorelabel['text'] = username + ': ' +str(points) + ' points'
    root.after(100, update)

def click(event):
    global canv
    global points
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

def main():
    global canv
    global points
    new_ball()
    new_ball()
    new_rect()
    new_rect()
    
    update()
    canv.bind('<Button-1>', click)

    root.mainloop()

#----------------------------------------user init------------------------

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
frame = Frame(root)
scorelabel = Label(frame, text = '0')
bsave = Button(frame, text = 'save', command=savescore)

def Enter():
    global canv
    global linit
    global einit
    global binit
    global scorelabel
    global username
    username = einit.get()
    linit.destroy()
    einit.destroy()
    binit.destroy()
    #quit()
    canv.pack(fill = BOTH, expand = 1)
    canv.create_rectangle(50, 50, 750, 550, outline='black')
    frame.pack(side=BOTTOM)
    scorelabel.pack(side=LEFT)
    bsave.pack(anchor = E)
    main()

linit = Label(text="Enter your name:")#.grid(row=0)
einit = Entry(width=20)#.grid(row=0, column=1)
binit = Button(text='Enter', command=Enter)#.grid(row=0, column=2)

linit.pack(side=LEFT)
einit.pack(side=LEFT)
binit.pack(side=LEFT)

root.mainloop()

savescore()







from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g = 1.0
points = 0
textpoints = canv.create_text(30,30,text = points,font = '28')

def dist(x1, y1, x2, y2): #returns distance between two points
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

class Ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def update(self):
        global g
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME############################################################################################
        if self.x + self.r > 800:
            self.vx = -0.8*abs(self.vx)
            self.vy *= 0.8
            self.x = 800 - self.r
        if self.y + self.r >= 600:
            self.vy = 0.5 * abs(self.vy)
            self.vx *= 0.5
            self.y = 600 - self.r + 1
            self.live -= 1
        else:
            self.vy -= g
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

        if self.live < 0:
            balls.remove(self)
            canv.delete(self.id)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME############################################################################################
        if dist(self.x, self.y, obj.x, obj.y) < self.r + obj.r:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, shots
        shots += 1
        new_ball = Ball()
        new_ball.r += 5
        self.angle = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = - self.f2_power * math.sin(self.angle)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.angle),
                    450 + max(self.f2_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        self.x = rnd(600, 750)
        self.y = rnd(300, 500)
        self.vx = rnd(10) - 5
        self.vy = rnd(10) - 5
        self.r = rnd(10, 30)
        color = self.color = 'red'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

    def update(self):
        if self.x > 750:
            self.vx = -abs(self.vx)
        if self.x < 600:
            self.vx = abs(self.vx)
        if self.y > 500:
            self.vy = -abs(self.vy)
        if self.y < 300:
            self.vy = abs(self.vy)

        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)

tars = []
for i in range(3):
    tars.append(Target())
screen1 = canv.create_text(400, 300, text='', font='28')
gun = Gun()
shots = 0
balls = []

def new_game(event=''):
    global gun, tars, screen1, balls, shots, points, textpoints
    for t in tars:
        t.new_target()
    numberoftargets = 3
    shots = 0
    balls = []
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)
    canv.itemconfig(screen1, text='')

    while numberoftargets > 0 or balls:
        for t in tars:
            t.update()
        for b in balls:
            b.update()
            for t in tars:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    numberoftargets -= 1
                    points += 1
                    canv.itemconfig(textpoints, text=points)
                    if numberoftargets == 0:
                        canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(shots) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    canv.delete(gun)
    root.after(750, new_game)

new_game()

root.mainloop()

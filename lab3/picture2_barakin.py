from graph import *
import math

obj = []
cnt = 1

def ellipse(xc, yc, a, b, col):
	penColor(col)
	brushColor('')
	obj.append(changeCoords(circle(0, 0, 10), [(xc - a, yc - b), (xc + a, yc + b)]))

def coloredellipse(xc, yc, a, b, col):
        #xc, yc - coords of the center, a, b - semimajor axises
        penColor(col)
        brushColor(col)
        obj.append(changeCoords(circle(0, 0, 10), [(xc - a, yc - b), (xc + a, yc + b)]))

def background():
	ax=600
	ay=0
	bx=0
	by=250
	x0=0
	y0=0
	brushColor("lightblue")
	obj.append(polygon([(x0,y0), (x0+ax,y0+ay), (x0+ax+bx,y0+ay+by), (x0+bx,y0+by)]))
	ax=600
	ay=0
	bx=0
	by=400
	x0=0
	y0=250
	brushColor("green")
	obj.append(polygon([(x0,y0), (x0+ax,y0+ay), (x0+ax+bx,y0+ay+by), (x0+bx,y0+by)]))

def fence(x0, y0, n, a, b):
	penSize(1)
	brushColor(255, 164, 21)
	for i in range(1, n + 1):
		obj.append(polygon([(x0+(i-1)*a,y0), (x0+i*a,y0),
                         (x0+i*a,y0+b), (x0+(i-1)*a,y0+b)]))

def dog_house(x0, y0, bvx, bvy, hl, hr1, hr2, k, a, b):
	penSize(1)
	brushColor(255, 193, 12)
	obj.append(polygon([(x0,y0), (x0+bvx,y0+bvy), (x0+bvx,y0+bvy+hr1), (x0,y0+hl)]))
	hx = bvx/2
	hy = hl/2
	obj.append(polygon([(x0,y0), (x0+bvx,y0+bvy), (x0+hx,y0-hy)]))
	x1 = x0 + bvx
	y1 = y0 + bvy
	bvx1 = bvx/2
	bvy1 = -bvy/2
	penSize(1)
	brushColor(255, 193, 12)
	obj.append(polygon([(x1,y1), (x1+bvx1,y1+bvy1), (x1+bvx1,y1+bvy1+hr2), (x1,y1+hr1)]))
	obj.append(polygon([(x1,y1), (x1+bvx1,y1+bvy1), (x0+hx+bvx1,y0-hy+bvy1), (x0+hx,y0-hy)]))
	obj.append(coloredellipse(x0+bvx/2, y0+(bvy+hr1)/2, a, b, "black"))
	for number in range(1,10+1):
		obj.append(ellipse(x0+bvx/2-8*number,y0+(hl+hr1)/2+(number)**0.9,5,7,"black"))

def psina(x0,y0,x,y,r,a,dalf,k,ori, red, green, blue):
        #k=sizemeasure, ori=orientation 1 for left -1 for right
        #red, green, blue - the color of eyes
	#body
	obj.append(coloredellipse(x0+x*k, y0+y*k, 20*k, 45*k, "grey"))
	obj.append(coloredellipse(x0+x*k*7/4, y0+y*k*3/4, 20*k, 30*k, "grey"))
	#front legs
	obj.append(coloredellipse(x0, y0+y*k*4/3, 30*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k, y0+y*k*3/2, 30*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k*0.6, y0+y*k*6/3, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k*0.9, y0+y*k*6/3, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0-x*k*0.1, y0+y*k*9.5/5, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0-x*k*0.4, y0+y*k*9.5/5, 6*k, 13*k, "grey"))
	#hind legs
	obj.append(coloredellipse(x0+x*k*7/4, y0+y*k*4/3, 20*k, 7*k, "grey"))
	brushColor("grey")
	obj.append(circle(x0+x*k*7/4,y0+y*k*3/4,10*k))
	obj.append(circle(x0+x*k*7/4+x*k*0.6,y0+y*k*3/4,10*k))
	obj.append(coloredellipse(x0+x*k*6/4+x*k, y0+y*k*5/4, 20*k, 7*k, "grey"))
	obj.append(coloredellipse(x0+x*k*6/4+x*k*0.6, y0+y*k*5/3, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k*6/4+x*k*0.9, y0+y*k*5/3, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k*7/4-x*k*0.1, y0+y*k*9/5, 6*k, 13*k, "grey"))
	obj.append(coloredellipse(x0+x*k*7/4-x*k*0.4, y0+y*k*9/5, 6*k, 13*k, "grey"))
	#head
	brushColor("grey")
	penColor("black")
	obj.append(circle(x0,y0+r*k,r*k))
	obj.append(circle(x0+x*k,y0+r*k,r*k))
	obj.append(rectangle(x0,y0,x0+x*k,y0+y*k))
	#eyes
	coloredellipse(x0+x*k*0.3, y0+y*k*0.3, 4*k, 7*k, (red, green, blue))
	ellipse(x0+x*k*0.3,y0+y*k*0.3,5*k,7*k,"black")
	coloredellipse(x0+x*k*0.3,y0+y*k*0.3,1*k,2*k,"black")
	coloredellipse(x0+x*k*0.7,y0+y*k*0.3,4*k,7*k, (red, green, blue))
	ellipse(x0+x*k*0.7,y0+y*k*0.3,5*k,7*k,"black")
	coloredellipse(x0+x*k*0.7,y0+y*k*0.3,1*k,2*k,"black")
	brushColor("white")
	#mouth
	obj.append(polygon([(x0+0.24*x*k,y0+y*k*0.75),(x0+0.24*x*k+3*k,y0+y*k*0.75-10*k),(x0+0.24*x*k+2*3*k,y0+y*k*0.75)]))
	obj.append(polygon([(x0+0.64*x*k,y0+y*k*0.75),(x0+0.64*x*k+3*k,y0+y*k*0.75-10*k),(x0+0.64*x*k+2*3*k,y0+y*k*0.75)]))
	penSize(3)
	i1=0
	i2=0
	j=0
	step=x*0.4/dalf/100
	for alf in range(1,2*314*dalf+1):
		j=j+step*alf/1000/3
		i1=i1+step/8
		obj.append(point(x0+x*k/2-i1*k,y0+y*k*2/3+j*k))
		i2=i2+step/8
		obj.append(point(x0+x*k/2+i2*k,y0+y*k*2/3+j*k))

def eyes(r, g, b):
        obj.append(coloredellipse(x0+x*k*0.3,y0+y*k*0.3,0,4*k,7*k, (red, green, blue)))
        obj.append(ellipse(x0+x*k*0.3,y0+y*k*0.3,5*k,7*k,"black"))
        obj.append(coloredellipse(x0+x*k*0.3,y0+y*k*0.3,1*k,2*k,"black"))
        obj.append(coloredellipse(x0+x*k*0.7,y0+y*k*0.3,4*k,7*k, (red, green, blue)))
        obj.append(ellipse(x0+x*k*0.7,y0+y*k*0.3,5*k,7*k,"black"))
        obj.append(coloredellipse(x0+x*k*0.7,y0+y*k*0.3,1*k,2*k,"black"))
        brushColor("white")

def picture():
        global cnt
        cnt += 1
        for ob in obj:
                deleteObject(ob)
        obj.clear()
        obj.append(background())
        obj.append(fence(0,140,50,10,200))
        obj.append(dog_house(320,330,90,20,90,120,100,0.4,35,25))
        obj.append(psina(75, 400, 50, 50, 8, 60, 1, 1 + math.sin(cnt/10), 1,
              int(255/2*(1 + math.sin(cnt/10))), int(150/2*(1 + math.sin(cnt/17))), int(150/2*(1 + math.sin(cnt/30)))))

onTimer(picture, 50)
                
run()






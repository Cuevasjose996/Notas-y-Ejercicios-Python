import turtle 
import time
import random

retraso=0.1
marcador=0
marcador_alto=0
s=turtle.Screen()
s.setup(1080,720)

s.bgcolor("silver")
s.title("la culebrita")

serpiente=turtle.Turtle()
serpiente.speed()
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
serpiente.color("green")

manzana= turtle.Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.goto(0,100)
manzana.speed(0)

texto=turtle.Turtle()
texto.speed()
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-360)
texto.write("Marcador:0\tMarcador mas alto: 0", align="center", font=("verdana", 24, "normal"))

def arriba():
    serpiente.direction="up"

def abajo(): 
    serpiente.direction="down"

def derecha():
    serpiente.direction="right"

def izquierda():
    serpiente.direction="left"

def movimiento():
    if serpiente.direction=="up":
        y=serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction=="down":
        y=serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction=="right":
        x=serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction=="left":
        x=serpiente.xcor()
        serpiente.setx(x-20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

cuerpo=[]

while True:
    s.update()
    if 540 < serpiente.xcor() or serpiente.xcor() < -540 or 360 < serpiente.ycor() or serpiente.ycor() < -360:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
            serpiente.home()
            serpiente.direction="Stop"
            cuerpo.clear()
            
            marcador=0
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))
        
    if serpiente.distance(manzana) < 20:
        x=random.randint(-520,520)
        y=random.randint(-340,340)
        manzana.goto(x,y)
        cuerpo2 = turtle.Turtle()
        cuerpo2.shape("square")
        cuerpo2.color("green")
        cuerpo2.penup()
        cuerpo2.goto(0,0)
        cuerpo2.speed(0)
        cuerpo.append(cuerpo2)

        marcador+=10
        if marcador>marcador_alto:
            marcador_alto=marcador
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))

    total=len(cuerpo)
    for index in range(total -1 ,0, -1):
        x=cuerpo[index-1].xcor()
        y=cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x=serpiente.xcor()
        y=serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente)<20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            serpiente.direction="Stop"
            cuerpo.clear()

            marcador=0
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto: {}".format(marcador,marcador_alto), align="center", font=("verdana", 24, "normal"))
    time.sleep(retraso)

turtle.done()
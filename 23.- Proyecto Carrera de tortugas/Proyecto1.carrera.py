import turtle
import random

s=turtle.Screen()
s.bgcolor("silver")


s.title("Proyecto 1")

player1=turtle.Turtle()
player2=turtle.Turtle()

player1.hideturtle()
player1.shape("turtle")
player1.shapesize(1.5,1.5,1.5)
player1.pensize(3)

player2.hideturtle()
player2.shape("turtle")
player2.shapesize(1.5,1.5,1.5)
player2.pensize(3)
player2.color("red", "red")

player1.color("green", "green")
player1.penup()
player1.goto(350,200)
player1.pendown()
player1.circle(35)
player1.penup()
player1.goto(-350,220)
player1.pendown()
player1.showturtle()

player2.penup()
player2.penup()
player2.goto(350,-200)
player2.pendown()
player2.circle(35)
player2.penup()
player2.goto(-350,-160)
player2.pendown()
player2.showturtle()

# player1.pos(332.5,217.5)
# player2.pos(332.5,-182.5)

dice=[1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (332.5,220):
        print("The turtle Green is the winner")
        break
    elif player2.pos() >= (332.5,-160):
        print("The turtle Blue is the winner")
        break
    else:
        turno1=input("Presiona la tecla enter para avanzar jugador 1.")
        turno1= random.choice(dice)
        print("Tu numero es: {} \n Avanzas: {}".format(turno1,turno1*20))
        player1.forward(20*turno1)

        turno2=input("Presiona la tecla enter para avanzar jugador 2.")
        turno2= random.choice(dice)
        print("Tu numero es: {} \n Avanzas: {}".format(turno2,turno2*20))
        player2.forward(20*turno2)

turtle.done()
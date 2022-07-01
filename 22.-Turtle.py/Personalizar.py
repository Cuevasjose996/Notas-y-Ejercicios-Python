import turtle

s= turtle.Screen()
t= turtle.Turtle()

s.bgcolor("red")
s.title("Proyecto 1")

t.shapesize(10,5,1) #ancho, largo, borde
t.shapesize(5,10,1)
t.shapesize(3,3,3)

t.fillcolor("green") #cambiar color de la tortuga
t.pencolor("white")
t.forward(100)

t.color ("blue")
t.pensize(5)
turtle.forward(100)

turtle.done()
import turtle

s=turtle.Screen()
t=turtle.Turtle()

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# for i in range(4):
#     t.forward(100)
#     t.right(90)

i=0

resultado=input("Quieres imprimir una figura?: ")
if resultado.lower() == "si":
    while i<=100:
        t.circle(i)
        i+=10
else:
    print("oka")


turtle.done()
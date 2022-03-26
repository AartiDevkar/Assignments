import turtle

flo = turtle.Turtle()
flo.speed(100)
flo.color("#612897","#781C68")

flo.begin_fill()

for i in range(100):
    flo.forward(200)
    flo.left(168.5)
    flo.forward(168.5)
flo.end_fill()


turtle.done()

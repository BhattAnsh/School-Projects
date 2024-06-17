import turtle

w = turtle.Turtle()
w.pensize(2)
w.speed(10)
c = ["cyan", "blue"]
turtle.bgcolor("black")
l = 0
for i in range(100):
    l += 2
    for j in range(2):
        w.pencolor(c[j])
        w.right(60+1)
        w.forward(l)
turtle.done()
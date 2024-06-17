import turtle

window = turtle.Turtle()
window.fillcolor("red")
window.speed(10)
window.begin_fill()
window.pensize(2)

for j in range(4):
    if j == 0 or j == 2:
        f = 100
    else:
        f = 200
    for i in range(4):
        window.right(25-2.5)
        window.forward(10)
    window.forward(f)
window.end_fill()
window.penup()
window.right(180)
window.forward(130)
window.left(90)
window.forward(40)
window.pendown()
window.pencolor("black")
window.fillcolor("white")
window.begin_fill()
for i in range(3):
    window.forward(70)
    window.left(120)
window.end_fill()


turtle.done()
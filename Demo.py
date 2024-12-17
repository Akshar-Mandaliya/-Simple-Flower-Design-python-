import turtle

t = turtle.Turtle()
t.speed(0)
t.color("blue")

for i in range(36):
    t.circle(100)
    t.left(10)

t.hideturtle()
turtle.done()

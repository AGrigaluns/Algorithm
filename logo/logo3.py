import turtle

pen = turtle.Turtle()

pen.begin_fill()

# ==========================> loop 1

for i in range(2):
    pen.left(90)
    pen.forward(100)

# ==========================> loop 2

for i in range(3):
    pen.right(30)
    pen.forward(60)
    pen.right(120)
    pen.forward(60)
    pen.right(30)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

pen.forward(100)

# =========================> loop 3

for i in range(3):
    pen.left(90)
    pen.forward(100)
    pen.right(30)
    pen.forward(60)
    pen.right(120)
    pen.forward(60)
    pen.right(30)
    pen.forward(100)

pen.left(90)
pen.forward(100)

pen.end_fill()

turtle.done()

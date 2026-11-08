import turtle

def draw_square(length, pen):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length, pen):
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b, pen):
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    pen = turtle.Turtle()
    pen.speed(5)
    
    pen.penup()
    pen.goto(-100, 100)
    pen.pendown()
    draw_square(50, pen)

    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    draw_square(50, pen)
    
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    draw_triangle(50, pen)

    pen.penup()
    pen.goto(100, 0)
    pen.pendown()
    draw_triangle(50, pen)

    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    draw_rectangle(60, 30, pen)

    pen.penup()
    pen.goto(100, -100)
    pen.pendown()
    draw_rectangle(60, 30, pen)

    pen.hideturtle()
    window.mainloop()
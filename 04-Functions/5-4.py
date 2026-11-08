import turtle

def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()

if __name__ == "__main__":
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    draw_square(100)
    window.mainloop()
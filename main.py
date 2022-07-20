import turtle
tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    new_heading = tim.heading() + 10
    tim.seth(new_heading)


def move_right():
    new_heading = tim.heading() - 10
    tim.seth(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear_screen)


screen.exitonclick()

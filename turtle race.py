import turtle
import random
names = ["tim", "tayo", "donald", "duke", "buhari", "trump", "biden"]
colors = ["green", "blue", "red", "orange", "yellow", "salmon", "violet"]
screen = turtle.Screen()
screen.screensize(canvheight=500, canvwidth=500)
x_cor = -250
y_cor = -200
user_bet = screen.textinput("bet", f"What color you think is going to win amongst {colors}??: ")


turtles = []
for name in names:
    newturtle = turtle.Turtle()
    newturtle.shape("turtle")
    newturtle.color(colors[names.index(name)])
    newturtle.penup()
    y_cor += 50
    newturtle.setposition(x_cor, y_cor)
    turtles.append(newturtle)
if user_bet:
    is_on = True
while is_on:
    for tins in turtles:
        if tins.xcor() < 280:
            tins.forward(random.randint(1, 10))
        else:
            is_on = False
            print(tins.pencolor())
            if user_bet == tins.pencolor():
                print("You won")
            else:
                print("you loose")


screen.exitonclick()

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose? There are six turtles: red, yellow, green, black, "
                                                          "purple, and pink. Which is the winner?")
colors = ["red", "yellow", "green", "black", "purple", "pink"]
y_positions = [-75, -45, -15, 15, 45, 75]
turtles = []
for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    turtles.append(turtle)

is_game_running = True
while is_game_running:
    for tur in turtles:
        tur.forward(random.randint(5, 10))
        if tur.xcor() >= 220:
            color = tur.color()[0]
            if user_bet == color:
                print("You win.")
            else:
                print("You lose. The winner is the {} turtle.".format(color))
            is_game_running = False
            break

screen.exitonclick()

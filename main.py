from turtle import Turtle, Screen
import random
isRacing = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []
for turtleIndex in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.color(colors[turtleIndex])
    turt.goto(x=-230, y=yPositions[turtleIndex])
    allTurtles.append(turt)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if userBet:
    isRacing = True
while isRacing:
    for turtle in allTurtles:        
        if turtle.xcor() > 230:
            isRacing = False
            winner = turtle.pencolor()
            if winner == userBet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")        
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)

screen.exitonclick()
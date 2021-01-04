# Intermediate - Build the Snake Game

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)  # 設定視窗寬高
screen.bgcolor("black")  # 設定視窗背景顏色
screen.title("Snake Game")  # 設定視窗 Title
screen.tracer(0)


# Create a snake body
# Move the snake
# Create snake food
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()  # 每個方塊都移動完再 update 視窗
    time.sleep(0.2)  # 控制每次 update 視窗的間隔時間

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)













screen.exitonclick()

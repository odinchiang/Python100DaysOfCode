# Intermediate - Build the Snake Game

from day020_Snake import Snake
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

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # 每個方塊都移動完再 update 視窗
    time.sleep(0.1)  # 控制每次 update 視窗的間隔時間
    snake.move()













screen.exitonclick()

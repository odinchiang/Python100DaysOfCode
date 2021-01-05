# Intermediate - Build the Snake Game

from day020_021_Snake import Snake
from day021_Food import Food
from day021_Scoreboard import Scoreboard
from turtle import Screen
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
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over
    # 輪詢時，head 要跳過不判斷，否則一開始就 Game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
